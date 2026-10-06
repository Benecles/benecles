#!/usr/bin/env python3
"""Assemble lesson compendia from the S0 map, S1 shelf, S2 chapters and S3 triage."""

import argparse
import csv
import hashlib
from html.parser import HTMLParser
import json
import re
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE = PIPELINE_ROOT.parents[1].parent / "ordenacoes-filipinas"
DOSSIER_SOURCE_ID = "dossier-atividade-05-10"
DOSSIER_INSTRUCTIONS_ID = "01-00-instrucoes"
ANSWER_INSTRUCTION = re.compile(
    r"Ao treinar o aluno, proponha perguntas no formato dos eixos e cobre respostas que usem os casos: "
    r"tribunal, ano, o que foi decidido, por quê, quem divergiu e como o caso responde ao eixo\."
)


class VisibleTextParser(HTMLParser):
    """Extract deterministic, reader-visible text from a lesson HTML page."""

    BLOCK_TAGS = {
        "address", "article", "blockquote", "br", "dd", "details", "div", "dl", "dt",
        "figcaption", "figure", "footer", "h1", "h2", "h3", "h4", "h5", "h6", "header",
        "hr", "li", "main", "nav", "ol", "p", "section", "summary", "table", "td", "th", "tr", "ul",
    }
    SKIP_TAGS = {"head", "script", "style", "noscript", "template"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0
        self.closed_details = []

    @staticmethod
    def attrs_dict(attrs):
        return {key.lower(): (value or "") for key, value in attrs}

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attr = self.attrs_dict(attrs)
        if tag == "summary" and self.closed_details:
            self.closed_details[-1]["summary"] = True
        explicitly_hidden = (
            "hidden" in attr
            or attr.get("aria-hidden", "").lower() == "true"
            or bool(re.search(r"(?:^|;)\s*(?:display\s*:\s*none|visibility\s*:\s*hidden)", attr.get("style", ""), re.I))
        )
        if tag == "details":
            self.closed_details.append({"open": "open" in attr, "summary": False})
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        elif tag in {"span", "strong", "em", "b", "i", "a", "text"}:
            self.parts.append(" ")
        if self.hidden or tag in self.SKIP_TAGS or explicitly_hidden:
            self.hidden += 1

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        elif tag in {"span", "strong", "em", "b", "i", "a", "text"}:
            self.parts.append(" ")
        if tag in self.SKIP_TAGS:
            self.hidden = max(0, self.hidden - 1)
        elif self.hidden:
            self.hidden -= 1
        if tag == "details" and self.closed_details:
            self.closed_details.pop()
        if tag == "summary" and self.closed_details:
            self.closed_details[-1]["summary"] = False

    def handle_data(self, data):
        if self.hidden:
            return
        if any(not item["open"] and not item["summary"] for item in self.closed_details):
            return
        self.parts.append(data)

    def text(self):
        lines = []
        for line in "".join(self.parts).splitlines():
            line = re.sub(r"\s+", " ", line).strip()
            if line and (not lines or lines[-1] != line):
                lines.append(line)
        return "\n".join(lines).strip() + "\n"


def visible_page_text(path):
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser.text()


def dossier_answer_instruction(chapters_root):
    source = chapters_root / DOSSIER_SOURCE_ID / f"{DOSSIER_INSTRUCTIONS_ID}.txt"
    normalized = " ".join(source.read_text(encoding="utf-8").split())
    match = ANSWER_INSTRUCTION.search(normalized)
    if not match:
        raise ValueError(f"dossier answer-evaluation instruction not found in {source}")
    return match.group(0)


def eixo_markdown(lesson, answer_instruction):
    lines = [f"# Eixo de discussão — {lesson['id']}", ""]
    axes = lesson.get("eixos_verbatim", [])
    if axes:
        lines.extend(["## Eixos retomados", ""])
        for item in axes:
            axis = item.get("eixo_de_discussao", "") if isinstance(item, dict) else str(item)
            if axis:
                lines.extend([f"- {axis}", ""])
    elif lesson.get("eixo_de_discussao"):
        lines.extend(["## Eixo", "", lesson["eixo_de_discussao"], ""])
    else:
        lines.extend(["## Eixo", "", "O programa não designa um eixo de discussão em forma de pergunta para este encontro.", ""])
    lines.extend(["## Instrução de avaliação do dossiê", "", answer_instruction, ""])
    return "\n".join(lines)


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def shelf_role(row):
    return row.get("source_role") or row.get("role", "")


def shelf_text_status(row):
    return row.get("text_status") or row.get("text status", "")


def shelf_source_is_available(row):
    status = shelf_text_status(row).strip().casefold()
    return not (status.startswith("missing") or status.startswith("not found"))


def safe_name(value):
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value)).strip("-._")
    value = value or "source"
    if len(value) > 40:
        digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:8]
        value = f"{value[:31]}-{digest}"
    return value


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chapter_catalog(chapters_root, require_text=True):
    catalog = {}
    for index_path in sorted(chapters_root.glob("*/index.json")):
        source_id = index_path.parent.name
        data = json.loads(index_path.read_text(encoding="utf-8"))
        for entry in data.get("chapters", []):
            key = (source_id, str(entry.get("id", "")))
            if not key[1] or key in catalog:
                raise ValueError(f"missing or duplicate chapter id: {source_id}/{key[1]}")
            text_path = index_path.parent / entry["path"]
            if require_text and not text_path.is_file():
                raise FileNotFoundError(text_path)
            catalog[key] = (entry, text_path)
    return catalog


def page_label(entry):
    start, end = entry.get("pdf_start"), entry.get("pdf_end")
    if isinstance(start, int) and isinstance(end, int):
        return f"PDF {start}" if start == end else f"PDF {start}–{end}"
    locator = entry.get("locator", "page")
    if locator == "article":
        chapter_id = entry.get("id", "")
        if chapter_id == "whole":
            return "whole document"
        return chapter_id if str(chapter_id).startswith(("Art. ", "ADCT Art. ")) else f"Art. {chapter_id}"
    if locator == "section":
        return f"§ {entry.get('id', '')}"
    return "whole document"


def table_row(record):
    cells = [record.get(key, "") for key in ("file", "source", "chapter", "pages", "role", "why", "sha256")]
    return "| " + " | ".join(str(cell).replace("|", "\\|").replace("\n", " ") for cell in cells) + " |"


def preserved_pulls(index_path):
    if not index_path.is_file():
        return []
    records = []
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if len(cells) != 7 or not cells[4].startswith("supporting (pulled)"):
            continue
        path = index_path.parent / cells[0]
        if not path.is_file():
            continue
        records.append({
            "file": cells[0], "source": cells[1], "chapter": cells[2], "pages": cells[3],
            "role": cells[4], "why": cells[5], "sha256": sha256(path),
        })
    return records


def make_record(path, source_id, chapter_id, pages, role, why):
    return {
        "file": path.name,
        "source": source_id,
        "chapter": chapter_id,
        "pages": pages,
        "role": role,
        "why": why,
        "sha256": sha256(path),
    }


def blueprint_statute_articles(path):
    """Return article numbers explicitly listed for the 60-statute packet."""
    if not path.is_file():
        return []
    numbers = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if "`60-statute.txt`" not in line or not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or "course statute packet" not in cells[0].casefold():
            continue
        if len(cells) > 1:
            numbers.extend(re.findall(r"\bart\.\s*(\d+)\b", cells[1], re.I))
    return list(dict.fromkeys(numbers))


def build(course, site=DEFAULT_SITE):
    root = PIPELINE_ROOT / course
    map_path = root / "course-map.json"
    shelf_path = root / "shelf.csv"
    triage_path = root / "triage.csv"
    chapters_root = root / "chapters"
    for required in (map_path, shelf_path):
        if not required.is_file():
            raise FileNotFoundError(required)

    course_map = json.loads(map_path.read_text(encoding="utf-8"))
    shelf_rows = read_csv(shelf_path)
    s4_assignments_path = root / "s4-assignments.csv"
    if s4_assignments_path.is_file():
        triage_rows = read_csv(s4_assignments_path)
    elif triage_path.is_file():
        triage_rows = read_csv(triage_path)
    else:
        lesson_triage_dir = root / "triage"
        triage_paths = sorted(lesson_triage_dir.glob("*.csv"))
        if not triage_paths:
            raise FileNotFoundError(triage_path)
        triage_rows = [row for path in triage_paths for row in read_csv(path)]
    catalog = chapter_catalog(chapters_root, require_text=False)
    shelf_by_id = {row["source_id"]: row for row in shelf_rows if row.get("source_id")}
    compendium = root / "compendium"
    compendium.mkdir(parents=True, exist_ok=True)
    lesson_count = 0
    file_count = 0
    provenance_count = 0
    is_latam = course == "direito-latino-americano"
    answer_instruction = dossier_answer_instruction(chapters_root) if is_latam else ""

    for lesson in course_map.get("lessons", []):
        lesson_id = lesson["id"]
        slug = Path(lesson_id).stem
        output_dir = compendium / slug
        output_dir.mkdir(parents=True, exist_ok=True)
        records = preserved_pulls(output_dir / "00-index.md")

        if is_latam:
            eixo_path = output_dir / "05-eixo.md"
            eixo_path.write_text(eixo_markdown(lesson, answer_instruction), encoding="utf-8")
            records.append(make_record(
                eixo_path, "course-map.json", "eixo_de_discussao", "—", "workbench metadata",
                "Verbatim eixo(s) from the S0 course map, paired with the dossier's answer-evaluation instruction.",
            ))
            dossier_entry = catalog.get((DOSSIER_SOURCE_ID, DOSSIER_INSTRUCTIONS_ID))
            if dossier_entry:
                records.append(make_record(
                    eixo_path, DOSSIER_SOURCE_ID, DOSSIER_INSTRUCTIONS_ID,
                    page_label(dossier_entry[0]), "workbench metadata",
                    "Exact answer-evaluation instruction reproduced from dossier Part 0, item 2.",
                ))
            page_path = site / "courses" / course / lesson_id
            if not page_path.is_file():
                raise FileNotFoundError(f"current live lesson page not found: {page_path}; pass --site")
            live_path = output_dir / "60-live-page.txt"
            live_path.write_text(visible_page_text(page_path), encoding="utf-8")
            records.append(make_record(
                live_path, "live-page", lesson_id, "—", "live page snapshot",
                "Visible text extracted from the current live lesson page.",
            ))

        def mapped_lessons(row):
            values = [value.strip() for value in row.get("lesson_ids", "").split(";") if value.strip()]
            if values:
                return values
            legacy = row.get("lesson_id", "").strip()
            return [legacy] if legacy else []

        slide_rows = [
            row for row in shelf_rows
            if shelf_role(row) == "slides"
            and lesson_id in mapped_lessons(row)
        ]
        slide_texts = []
        slide_meta = []
        for row in slide_rows:
            source_id = row["source_id"]
            matches = sorted((key, item) for key, item in catalog.items() if key[0] == source_id)
            if shelf_source_is_available(row) and matches:
                for (matched_source, chapter_id), (entry, text_path) in matches:
                    slide_texts.append(text_path.read_text(encoding="utf-8"))
                    slide_meta.append((matched_source, chapter_id, page_label(entry)))
            else:
                slide_texts.append(
                    f"[Slides unavailable: S1 marks source `{source_id}` as `{row.get('text_status', 'unknown')}`; "
                    "no slide text was copied.]\n"
                )
                slide_meta.append((source_id, "—", "—"))
        if not slide_rows:
            slide_texts.append("[No slide source is mapped to this lesson in S1.]\n")
            slide_meta.append(("—", "—", "—"))
        slides_path = output_dir / "10-slides.txt"
        slides_path.write_text("\n\n".join(text.rstrip() for text in slide_texts) + "\n", encoding="utf-8")
        for source_id, chapter_id, pages in slide_meta:
            status = shelf_text_status(shelf_by_id.get(source_id, {}))
            why = "Lesson slide deck from S1." if shelf_source_is_available(shelf_by_id.get(source_id, {})) else f"S1 records `{source_id}` as missing; placeholder documents the source gap."
            records.append(make_record(slides_path, source_id, chapter_id, pages, "slides", why))

        assigned = [
            row for row in triage_rows
            if row.get("lesson_id") == lesson_id and row.get("role") in {"primary", "supporting", "background"}
        ]
        exercise_pieces = []
        exercise_meta = []
        statute_pieces = []
        statute_meta = []
        counters = {"primary": 0, "supporting": 0, "background": 0}
        for row in assigned:
            source_id = row["source_id"]
            chapter_id = row["chapter_id"]
            key = (source_id, chapter_id)
            if key not in catalog:
                raise ValueError(f"S3 references unknown chapter {source_id}/{chapter_id}")
            entry, text_path = catalog[key]
            source_role = shelf_role(shelf_by_id.get(source_id, {}))
            if source_id == "constituicao-federal-1988" or source_id.startswith("lei-") or source_role == "statute":
                if entry.get("locator") != "article" or chapter_id == "whole":
                    raise ValueError(f"S4 legal sources must be assembled by article: {source_id}/{chapter_id}")
            if source_role == "statute" and entry.get("locator") == "article":
                statute_pieces.append(f"===== {source_id} / {chapter_id} =====\n\n{text_path.read_text(encoding='utf-8').rstrip()}\n")
                statute_meta.append((source_id, chapter_id, page_label(entry), row["role"], row["why"]))
            is_exercise = source_role in {"past_exam", "exercise", "exercises"} or bool(re.search(r"exam|exerc", source_id, re.I))
            if is_exercise:
                exercise_pieces.append(f"===== {source_id} / {chapter_id} =====\n\n{text_path.read_text(encoding='utf-8').rstrip()}\n")
                exercise_meta.append((source_id, chapter_id, page_label(entry), row["role"], row["why"]))
                continue
            role = row["role"]
            counters[role] += 1
            prefix = {"primary": "20-primary", "supporting": "30-supporting", "background": "40-background"}[role]
            file_name = f"{prefix}-{counters[role]:03d}-{safe_name(source_id)}-{safe_name(chapter_id)}.txt"
            destination = output_dir / file_name
            destination.write_bytes(text_path.read_bytes())
            records.append(make_record(destination, source_id, chapter_id, page_label(entry), role, row["why"]))

        known_statutes = {(source_id, chapter_id) for source_id, chapter_id, *_ in statute_meta}
        blueprint_path = output_dir / "blueprint.md"
        cpc_sources = [source_id for source_id, shelf_row in shelf_by_id.items() if shelf_role(shelf_row) == "statute" and source_id.startswith("cpc-")]
        if cpc_sources:
            cpc_source_id = cpc_sources[0]
            for article_number in blueprint_statute_articles(blueprint_path):
                chapter_id = f"Art. {article_number}"
                key = (cpc_source_id, chapter_id)
                if key in known_statutes or key not in catalog:
                    continue
                entry, text_path = catalog[key]
                if entry.get("locator") != "article":
                    continue
                statute_pieces.append(f"===== {cpc_source_id} / {chapter_id} =====\n\n{text_path.read_text(encoding='utf-8').rstrip()}\n")
                statute_meta.append((cpc_source_id, chapter_id, page_label(entry), "blueprint locator", "Explicitly listed in the lesson blueprint's Course statute packet locator."))
                known_statutes.add(key)

        if exercise_pieces:
            exercises_path = output_dir / "50-exercises-and-exams.txt"
            exercises_path.write_text("\n\n".join(exercise_pieces).rstrip() + "\n", encoding="utf-8")
            for source_id, chapter_id, pages, role, why in exercise_meta:
                records.append(make_record(exercises_path, source_id, chapter_id, pages, f"{role}; exercises/exams", why))
        else:
            exercises_path = output_dir / "50-exercises-and-exams.txt"
            exercises_path.write_text(
                "[No exercise or past-exam chapter is assigned to this lesson in S3.]\n",
                encoding="utf-8",
            )
            records.append(make_record(
                exercises_path,
                "course-map.json",
                "exam",
                "—",
                "exercises/exams (no assigned source)",
                "S0 leaves lesson-specific assessment mapping undetermined; S3 assigns no exercise or exam chapter to this lesson.",
            ))

        statute_path = output_dir / "60-statute.txt"
        if statute_pieces:
            statute_path.write_text("\n\n".join(statute_pieces).rstrip() + "\n", encoding="utf-8")
            for source_id, chapter_id, pages, role, why in statute_meta:
                records.append(make_record(statute_path, source_id, chapter_id, pages, f"statute packet; {role}", why))
        else:
            statute_path.write_text("[No CPC article is assigned to this lesson in S3.]\n", encoding="utf-8")
            records.append(make_record(
                statute_path, "course-map.json", "statute", "—", "statute packet",
                "S3 assigns no CPC article to this lesson.",
            ))

        records.sort(key=lambda row: (row["file"], row["source"], row["chapter"]))
        lines = [
            f"# Compendium — {lesson_id}",
            "",
            "Provenance index assembled from `course-map.json` (S0), `shelf.csv` (S1), `chapters/` (S2), and `triage.csv` (S3).",
            "",
            "| File | Source | Chapter | Pages | Role | Why | SHA-256 |",
            "|---|---|---|---|---|---|---|",
        ]
        lines.extend(table_row(record) for record in records)
        (output_dir / "00-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        lesson_count += 1
        file_count += len({record["file"] for record in records})
        provenance_count += len(records)

    print(f"Built {lesson_count} lesson compendia, {file_count} files, {provenance_count} provenance rows.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course", nargs="?", default="controle-de-constitucionalidade")
    parser.add_argument("--site", type=Path, default=DEFAULT_SITE, help="current site checkout used for live-page snapshots")
    args = parser.parse_args()
    build(args.course, site=args.site)


if __name__ == "__main__":
    main()
