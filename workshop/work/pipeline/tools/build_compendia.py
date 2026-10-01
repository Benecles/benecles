#!/usr/bin/env python3
"""Assemble lesson compendia from the S0 map, S1 shelf, S2 chapters and S3 triage."""

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def safe_name(value):
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value)).strip("-._")
    value = value or "source"
    if len(value) > 40:
        digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:8]
        value = f"{value[:31]}-{digest}"
    return value


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chapter_catalog(chapters_root):
    catalog = {}
    for index_path in sorted(chapters_root.glob("*/index.json")):
        source_id = index_path.parent.name
        data = json.loads(index_path.read_text(encoding="utf-8"))
        for entry in data.get("chapters", []):
            key = (source_id, str(entry.get("id", "")))
            if not key[1] or key in catalog:
                raise ValueError(f"missing or duplicate chapter id: {source_id}/{key[1]}")
            text_path = index_path.parent / entry["path"]
            if not text_path.is_file():
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


def build(course):
    root = PIPELINE_ROOT / course
    map_path = root / "course-map.json"
    shelf_path = root / "shelf.csv"
    triage_path = root / "triage.csv"
    chapters_root = root / "chapters"
    for required in (map_path, shelf_path, triage_path):
        if not required.is_file():
            raise FileNotFoundError(required)

    course_map = json.loads(map_path.read_text(encoding="utf-8"))
    shelf_rows = read_csv(shelf_path)
    s4_assignments_path = root / "s4-assignments.csv"
    triage_rows = read_csv(s4_assignments_path if s4_assignments_path.is_file() else triage_path)
    catalog = chapter_catalog(chapters_root)
    shelf_by_id = {row["source_id"]: row for row in shelf_rows if row.get("source_id")}
    compendium = root / "compendium"
    compendium.mkdir(parents=True, exist_ok=True)
    lesson_count = 0
    file_count = 0
    provenance_count = 0

    for lesson in course_map.get("lessons", []):
        lesson_id = lesson["id"]
        slug = Path(lesson_id).stem
        output_dir = compendium / slug
        output_dir.mkdir(parents=True, exist_ok=True)
        records = preserved_pulls(output_dir / "00-index.md")

        slide_rows = [row for row in shelf_rows if row.get("role") == "slides" and row.get("lesson_id") == lesson_id]
        slide_texts = []
        slide_meta = []
        for row in slide_rows:
            source_id = row["source_id"]
            matches = sorted((key, item) for key, item in catalog.items() if key[0] == source_id)
            if row.get("text_status") in {"text layer", "OCR done"} and matches:
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
            status = shelf_by_id.get(source_id, {}).get("text_status", "")
            why = "Lesson slide deck from S1." if status in {"text layer", "OCR done"} else f"S1 records `{source_id}` as missing; placeholder documents the source gap."
            records.append(make_record(slides_path, source_id, chapter_id, pages, "slides", why))

        assigned = [
            row for row in triage_rows
            if row.get("lesson_id") == lesson_id and row.get("role") in {"primary", "supporting", "background"}
        ]
        exercise_pieces = []
        exercise_meta = []
        counters = {"primary": 0, "supporting": 0, "background": 0}
        for row in assigned:
            source_id = row["source_id"]
            chapter_id = row["chapter_id"]
            key = (source_id, chapter_id)
            if key not in catalog:
                raise ValueError(f"S3 references unknown chapter {source_id}/{chapter_id}")
            entry, text_path = catalog[key]
            if source_id == "constituicao-federal-1988" or source_id.startswith("lei-") or shelf_by_id.get(source_id, {}).get("role") == "statute":
                if entry.get("locator") != "article" or chapter_id == "whole":
                    raise ValueError(f"S4 legal sources must be assembled by article: {source_id}/{chapter_id}")
            shelf_role = shelf_by_id.get(source_id, {}).get("role", "")
            is_exercise = shelf_role in {"past_exam", "exercise", "exercises"} or bool(re.search(r"exam|exerc", source_id, re.I))
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
    args = parser.parse_args()
    build(args.course)


if __name__ == "__main__":
    main()
