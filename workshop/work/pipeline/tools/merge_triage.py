#!/usr/bin/env python3
"""Merge per-lesson S3 files and mark every unselected chapter unused."""

import argparse
import csv
import json
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["source_id", "chapter_id", "lesson_id", "role", "why"]
LESSON_ROLES = {"primary", "supporting", "background", "no_book_covers"}


def read_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            raise ValueError(f"{path}: expected columns {FIELDS}, got {reader.fieldnames}")
        return list(reader)


def merge(course):
    root = PIPELINE_ROOT / course
    course_map_path = root / "course-map.json"
    chapters_root = root / "chapters"
    triage_root = root / "triage"
    course_map = json.loads(course_map_path.read_text(encoding="utf-8"))

    catalog = set()
    for index_path in sorted(chapters_root.glob("*/index.json")):
        source_id = index_path.parent.name
        index = json.loads(index_path.read_text(encoding="utf-8"))
        for chapter in index.get("chapters", []):
            chapter_id = str(chapter.get("id", ""))
            if not chapter_id or (source_id, chapter_id) in catalog:
                raise ValueError(f"missing or duplicate index id: {source_id}/{chapter_id}")
            catalog.add((source_id, chapter_id))

    rows = []
    seen = set()
    for lesson in course_map.get("lessons", []):
        lesson_id = lesson["id"]
        path = triage_root / f"{Path(lesson_id).stem}.csv"
        if not path.is_file():
            raise FileNotFoundError(f"missing lesson triage: {path}")
        for row in read_rows(path):
            if row["role"] not in LESSON_ROLES:
                raise ValueError(f"{path}: invalid per-lesson role {row['role']!r}")
            if not row["why"].strip():
                raise ValueError(f"{path}: empty rationale")
            if row["role"] == "no_book_covers":
                if row["source_id"] or row["chapter_id"] or row["lesson_id"] != lesson_id:
                    raise ValueError(f"{path}: malformed no_book_covers row")
            else:
                key = (row["source_id"], row["chapter_id"])
                if key not in catalog:
                    raise ValueError(f"{path}: unknown indexed chapter {key}")
                if row["lesson_id"] != lesson_id:
                    raise ValueError(f"{path}: row belongs to {row['lesson_id']!r}, expected {lesson_id!r}")
            key = (row["source_id"], row["chapter_id"], row["lesson_id"], row["role"])
            if key in seen:
                raise ValueError(f"duplicate triage row in {path}: {key}")
            seen.add(key)
            rows.append({field: row[field] for field in FIELDS})

    assigned = {
        (row["source_id"], row["chapter_id"])
        for row in rows
        if row["role"] in {"primary", "supporting"}
    }
    background = {
        (row["source_id"], row["chapter_id"])
        for row in rows
        if row["role"] == "background"
    }
    orphan_background = background - assigned
    if orphan_background:
        sample = sorted(orphan_background)[:5]
        raise ValueError(f"background chapters lack a primary/supporting verdict: {sample}")

    unused_count = 0
    for source_id, chapter_id in sorted(catalog - assigned):
        rows.append({
            "source_id": source_id,
            "chapter_id": chapter_id,
            "lesson_id": "",
            "role": "unused",
            "why": "No lesson-specific triage selected this indexed unit for its mapped syllabus or learning outcome.",
        })
        unused_count += 1

    output = root / "triage.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Merged {len(rows) - unused_count} lesson rows; added {unused_count} unused chapters; wrote {output}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course", nargs="?", default="direito-latino-americano")
    args = parser.parse_args()
    merge(args.course)


if __name__ == "__main__":
    main()
