#!/usr/bin/env python3
"""Append one S2 source chapter or PDF-page range to a lesson compendium."""

import argparse
import json
import re
from pathlib import Path

from build_compendia import PIPELINE_ROOT, chapter_catalog, make_record, page_label, safe_name, table_row


PAGE_MARKER = re.compile(r"^===== p\. (.+?) \(PDF (\d+)\) =====\s*$", re.M)
PAGE_RANGE = re.compile(r"^(?:pdf\s*)?(\d+)\s*(?:-|–|:)\s*(\d+)$", re.I)


def lesson_slug(value, lessons):
    normalized = value if value.endswith(".html") else f"{value}.html"
    for lesson in lessons:
        if lesson.get("id") == normalized:
            return Path(normalized).stem
    raise ValueError(f"unknown lesson {value!r}; expected an S0 lesson id")


def extract_page_range(source_id, first, last, catalog):
    pieces = []
    records = []
    found_pages = set()
    for (candidate_source, chapter_id), (entry, text_path) in sorted(catalog.items()):
        if candidate_source != source_id or entry.get("locator", "page") != "page":
            continue
        text = text_path.read_text(encoding="utf-8")
        markers = list(PAGE_MARKER.finditer(text))
        for index, marker in enumerate(markers):
            page = int(marker.group(2))
            if first <= page <= last:
                start = marker.start()
                end = markers[index + 1].start() if index + 1 < len(markers) else len(text)
                pieces.append((page, chapter_id, text[start:end].rstrip()))
                records.append((chapter_id, page_label(entry), text_path))
                found_pages.add(page)
    expected = set(range(first, last + 1))
    if found_pages != expected:
        absent = sorted(expected - found_pages)
        raise ValueError(f"PDF page range is not fully present for {source_id}; missing pages: {absent}")
    pieces.sort(key=lambda item: (item[0], item[1]))
    content = "\n\n".join(piece[2] for piece in pieces) + "\n"
    # Keep one provenance row for every S2 chapter contributing selected pages.
    contributors = sorted({(chapter_id, page_span) for chapter_id, page_span, _ in records})
    return content, contributors


def pull(course, lesson, source_id, chapter_or_pages, why):
    root = PIPELINE_ROOT / course
    map_path = root / "course-map.json"
    map_data = json.loads(map_path.read_text(encoding="utf-8"))
    slug = lesson_slug(lesson, map_data.get("lessons", []))
    compendium_dir = root / "compendium" / slug
    index_path = compendium_dir / "00-index.md"
    if not index_path.is_file():
        raise FileNotFoundError(f"missing {index_path}; build S4 compendia first")
    catalog = chapter_catalog(root / "chapters")
    output_content = ""
    provenance = []
    selector = chapter_or_pages.strip()
    exact = (source_id, selector)
    if exact in catalog:
        entry, text_path = catalog[exact]
        output_content = text_path.read_text(encoding="utf-8")
        provenance = [(selector, page_label(entry))]
    else:
        match = PAGE_RANGE.fullmatch(selector)
        if not match:
            known = sorted(chapter_id for candidate_source, chapter_id in catalog if candidate_source == source_id)
            raise ValueError(f"unknown chapter/pages selector {selector!r} for {source_id}; known chapter ids: {known[:12]}")
        first, last = map(int, match.groups())
        if last < first:
            raise ValueError("page range end must be greater than or equal to its start")
        output_content, contributors = extract_page_range(source_id, first, last, catalog)
        provenance = [(chapter_id, pages) for chapter_id, pages in contributors]
        if not provenance:
            raise ValueError(f"no S2 text found for {source_id} PDF {first}-{last}")

    existing = list(compendium_dir.glob("30-pulled-*.txt"))
    sequence = len(existing) + 1
    file_name = f"30-pulled-{sequence:03d}-{safe_name(source_id)}-{safe_name(selector)}.txt"
    destination = compendium_dir / file_name
    if destination.exists():
        raise FileExistsError(destination)
    destination.write_text(output_content, encoding="utf-8")

    index = index_path.read_text(encoding="utf-8")
    rows = []
    for chapter_id, pages in provenance:
        record = make_record(destination, source_id, chapter_id, pages, "supporting (pulled)", why)
        rows.append(table_row(record))
    index_path.write_text(index.rstrip() + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Appended {destination.relative_to(root)} and one provenance row to {index_path.relative_to(root)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", help="S0 lesson id, for example aula-30 or aula-30.html")
    parser.add_argument("source_id", help="S1 source id whose S2 chapter text is requested")
    parser.add_argument("chapter_or_pages", help="S2 chapter id or PDF page range such as PDF 12-14")
    parser.add_argument("why", help="Reason this material is needed")
    parser.add_argument("--course", default="controle-de-constitucionalidade")
    args = parser.parse_args()
    pull(args.course, args.lesson, args.source_id, args.chapter_or_pages, args.why)


if __name__ == "__main__":
    main()
