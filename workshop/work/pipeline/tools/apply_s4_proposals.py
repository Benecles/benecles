#!/usr/bin/env python3
"""Merge bounded per-lesson S4 proposals into a reproducible assignment CSV."""
import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = "controle-de-constitucionalidade"


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proposals", nargs="+", type=Path)
    parser.add_argument("--course", default=COURSE)
    args = parser.parse_args()
    root = ROOT / args.course
    course_map = json.loads((root / "course-map.json").read_text(encoding="utf-8"))
    lessons = course_map.get("lessons", [])
    lesson_by_id = {lesson["id"]: lesson for lesson in lessons}
    shelf = read_csv(root / "shelf.csv")
    shelf_by_id = {row["source_id"]: row for row in shelf if row.get("source_id")}
    catalog = {}
    for index_path in (root / "chapters").glob("*/index.json"):
        source_id = index_path.parent.name
        index = json.loads(index_path.read_text(encoding="utf-8"))
        for entry in index.get("chapters", []):
            catalog[(source_id, str(entry.get("id", "")))] = (entry, index_path.parent / entry["path"])

    chosen = {}
    for path in args.proposals:
        data = json.loads(path.read_text(encoding="utf-8"))
        for lesson in data.get("lessons", []):
            lesson_id = lesson.get("id", "")
            if lesson_id not in lesson_by_id or lesson_id in chosen:
                raise ValueError(f"unknown or duplicate proposed lesson: {lesson_id}")
            assignments = lesson.get("assignments", [])
            primary_total = supporting_total = 0
            support_rows = []
            for assignment in assignments:
                source_id, chapter_id = assignment.get("source_id", ""), assignment.get("chapter_id", "")
                role, why = assignment.get("role", ""), assignment.get("why", "")
                if role not in {"primary", "supporting"} or not why:
                    raise ValueError(f"{lesson_id}: assignment requires a primary/supporting role and rationale")
                key = (source_id, chapter_id)
                if key not in catalog:
                    raise ValueError(f"{lesson_id}: unknown S2 atom {source_id}/{chapter_id}")
                entry, text_path = catalog[key]
                text = text_path.read_text(encoding="utf-8")
                word_count = len(re.sub(r"(?m)^===== (?:p\. .*? \(PDF \d+\)|§ .*?|Art\. .*?) =====\s*$", "", text).split())
                legal = source_id == "constituicao-federal-1988" or source_id.startswith("lei-") or shelf_by_id.get(source_id, {}).get("role") == "statute"
                if legal and (entry.get("locator") != "article" or chapter_id == "whole"):
                    raise ValueError(f"{lesson_id}: legal text must use an exact article atom: {source_id}/{chapter_id}")
                if role == "supporting":
                    if word_count > 10_000:
                        raise ValueError(f"{lesson_id}: supporting atom {source_id}/{chapter_id} has {word_count} words")
                    supporting_total += word_count
                    support_rows.append((source_id, chapter_id, word_count))
                else:
                    primary_total += word_count
            if supporting_total > 30_000:
                raise ValueError(f"{lesson_id}: supporting total {supporting_total} exceeds 30,000")
            if primary_total < 5_000:
                reason = lesson_by_id[lesson_id].get("thin_primary_reason", "")
                if len(reason.split()) < 8:
                    raise ValueError(f"{lesson_id}: only {primary_total} primary words and no explicit thin_primary_reason")
            chosen[lesson_id] = assignments
    expected = set(lesson_by_id)
    if set(chosen) != expected:
        missing = sorted(expected - set(chosen))
        extra = sorted(set(chosen) - expected)
        raise ValueError(f"proposal lesson coverage mismatch; missing={missing}, extra={extra}")

    rows = []
    for lesson_id, assignments in chosen.items():
        for item in assignments:
            rows.append({"source_id": item["source_id"], "chapter_id": item["chapter_id"], "lesson_id": lesson_id, "role": item["role"], "why": item["why"]})
        # Preserve assessment practice from the fixed S3 data; the S4 policy checker excludes these from reading-load totals.
        for row in read_csv(root / "triage.csv"):
            if row.get("lesson_id") == lesson_id and row.get("role") in {"primary", "supporting"}:
                source_id = row.get("source_id", "")
                shelf_role = shelf_by_id.get(source_id, {}).get("role", "")
                if shelf_role in {"past_exam", "exercise", "exercises"} or re.search(r"exam|exerc", source_id, re.I):
                    rows.append(dict(row))
    # Background rows are the exact closure of each prerequisite's new S4 primary atoms.
    for lesson in lessons:
        lesson_id = lesson["id"]
        for prereq in lesson.get("prerequisites", []):
            prior = prereq["id"]
            for row in rows:
                if row["lesson_id"] == prior and row["role"] == "primary":
                    rows.append({
                        "source_id": row["source_id"],
                        "chapter_id": row["chapter_id"],
                        "lesson_id": lesson_id,
                        "role": "background",
                        "why": f"Prerequisite background from {prior}: selected essential reading supports the lesson prerequisite.",
                    })
    path = root / "s4-assignments.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_id", "chapter_id", "lesson_id", "role", "why"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} S4 assignments for {len(chosen)} lessons to {path}")


if __name__ == "__main__":
    main()
