#!/usr/bin/env python3
"""Validate the CUFRGS source pipeline's S0–S3 stage artifacts.

Usage: pipeline_check.py {s0,s1,s2,s3} COURSE [--map PATH] [--shelf PATH]
       [--chapters PATH] [--triage PATH] [--site PATH]

S1 shelf.csv columns: source_id, role, path, sha256, format, text_status,
and optional lesson_id (for a slide deck). A missing source uses text_status=missing.
S2 chapters/<source_id>/index.json has a chapters list; each item has id,
path, pdf_start, pdf_end, word_count. Text uses ===== p. N (PDF M) =====.
S3 triage.csv columns: source_id, chapter_id, lesson_id, role, why.
Roles are primary, supporting, background, unused, no_book_covers. The
no_book_covers row has lesson_id but no chapter_id; unused has chapter_id but
no lesson_id. A background row must be exactly the closure of prerequisite
lessons' primary chapter rows. Slide coverage comes from shelf.csv.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

WORKSHOP = Path(__file__).resolve().parents[3]
SITE = WORKSHOP.parent / "ordenacoes-filipinas"
MARKER = re.compile(r"^===== p\. (.+?) \(PDF (\d+)\) =====$", re.M)
SECTION_MARKER = re.compile(r"^===== § ([^=]+?) =====$", re.M)
ARTICLE_MARKER = re.compile(r"^===== Art\. ([^=]+?) =====$", re.M)
ROLES = {"primary", "supporting", "background", "unused", "no_book_covers"}


def read_json(path, errors):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        errors.append(f"cannot read JSON {path}: {exc}")
        return {}


def read_csv(path, errors):
    try:
        with path.open(newline="") as handle:
            return list(csv.DictReader(handle))
    except OSError as exc:
        errors.append(f"cannot read CSV {path}: {exc}")
        return []


def course_map(path, errors):
    data = read_json(path, errors)
    lessons = data.get("lessons", [])
    if not isinstance(lessons, list) or not lessons:
        errors.append("course map has no lessons")
        return []
    return lessons


def check_s0(args, errors):
    lessons = course_map(args.map, errors)
    live = args.site / "courses" / args.course
    pages = {p.name for p in live.glob("aula-*.html")}
    if not pages:
        errors.append(f"no live lesson pages found in {live}")
    ids = [lesson.get("id") for lesson in lessons]
    if len(ids) != len(set(ids)):
        errors.append("duplicate lesson IDs in course map")
    missing = sorted(pages - set(ids))
    extra = sorted(set(ids) - pages)
    if missing:
        errors.append("live pages absent from map: " + ", ".join(missing))
    if extra:
        errors.append("map IDs without live pages: " + ", ".join(map(str, extra)))
    positions = {lesson_id: i for i, lesson_id in enumerate(ids)}
    for i, lesson in enumerate(lessons):
        lesson_id = lesson.get("id", f"row {i+1}")
        for field in ("syllabus_line", "learning_outcome", "exam"):
            if not lesson.get(field):
                errors.append(f"{lesson_id}: missing {field}")
        prereqs = lesson.get("prerequisites", [])
        if not isinstance(prereqs, list):
            errors.append(f"{lesson_id}: prerequisites must be a list")
            continue
        for prereq in prereqs:
            target = prereq.get("id") if isinstance(prereq, dict) else None
            reason = prereq.get("reason") if isinstance(prereq, dict) else None
            if target not in positions:
                errors.append(f"{lesson_id}: unknown prerequisite {target}")
            elif positions[target] >= i:
                errors.append(f"{lesson_id}: prerequisite {target} does not point backward")
            if not reason:
                errors.append(f"{lesson_id}: prerequisite {target} lacks a reason")
    bibliography = read_json(args.map, []).get("bibliography", {})
    if not bibliography.get("base") or not bibliography.get("supplementary"):
        errors.append("bibliography must contain base and supplementary lists")
    return f"{len(lessons)} mapped / {len(pages)} live lessons"


def check_s1(args, errors):
    rows = read_csv(args.shelf, errors)
    if not rows:
        errors.append("shelf has no sources")
        return "0 sources"
    required = {"source_id", "role", "path", "sha256", "format", "text_status"}
    for n, row in enumerate(rows, 2):
        absent = sorted(required - row.keys())
        if absent:
            errors.append(f"shelf row {n}: missing columns {', '.join(absent)}")
            break
        if not row["source_id"] or not row["role"]:
            errors.append(f"shelf row {n}: source_id and role required")
        if row["text_status"] not in {"text layer", "OCR done", "needs OCR", "missing"}:
            errors.append(f"shelf row {n}: invalid text_status")
        if row["text_status"] != "missing" and not row["path"]:
            errors.append(f"shelf row {n}: available source lacks path")
    return f"{len(rows)} shelf sources"


def chapter_catalog(args, errors, validate_text):
    catalog = {}
    indexes = sorted(args.chapters.glob("*/index.json"))
    if not indexes:
        errors.append(f"no chapter indexes in {args.chapters}")
    for index_path in indexes:
        source_id = index_path.parent.name
        entries = read_json(index_path, errors).get("chapters", [])
        if not entries:
            errors.append(f"{source_id}: empty chapter index")
        # Section-split chapters can share a PDF page at a heading boundary.
        # Treat all children with one `parent` as a single page-span unit while
        # still validating every child's own marker sequence below.
        parent_groups = {}
        for entry in entries:
            if entry.get("locator", "page") != "page" or not entry.get("parent"):
                continue
            parent_groups.setdefault(entry["parent"], []).append(entry)
        page_units = []
        seen_parents = set()
        for entry in entries:
            if entry.get("locator", "page") != "page":
                continue
            parent = entry.get("parent")
            if parent:
                if parent in seen_parents:
                    continue
                seen_parents.add(parent)
                siblings = parent_groups[parent]
                spans = [(e.get("pdf_start"), e.get("pdf_end")) for e in siblings]
                spans = [(start, end) for start, end in spans if isinstance(start, int) and isinstance(end, int) and end >= start]
                if spans:
                    page_units.append((min(start for start, _ in spans), max(end for _, end in spans), parent))
            else:
                start, end = entry.get("pdf_start"), entry.get("pdf_end")
                if isinstance(start, int) and isinstance(end, int) and end >= start:
                    page_units.append((start, end, entry.get("id")))
        prior_end = None
        for start, end, chapter_id in page_units:
            if prior_end is not None and start != prior_end + 1:
                errors.append(f"{source_id}/{chapter_id}: gap or overlap after PDF {prior_end}")
            prior_end = end
        parent_markers = {}
        parent_ranges = {}
        for entry in entries:
            chapter_id = entry.get("id")
            key = (source_id, chapter_id)
            if not chapter_id or key in catalog:
                errors.append(f"{source_id}: absent or duplicate chapter id {chapter_id}")
                continue
            catalog[key] = entry
            if not validate_text:
                continue
            rel_path = entry.get("path", "")
            text_path = index_path.parent / rel_path
            try:
                content = text_path.read_text()
            except OSError as exc:
                errors.append(f"{source_id}/{chapter_id}: cannot read text: {exc}")
                continue
            locator = entry.get("locator", "page")
            if locator == "page":
                start, end = entry.get("pdf_start"), entry.get("pdf_end")
                if not isinstance(start, int) or not isinstance(end, int) or end < start:
                    errors.append(f"{source_id}/{chapter_id}: invalid PDF span")
                    continue
                markers = [int(m.group(2)) for m in MARKER.finditer(content)]
                if markers != list(range(start, end + 1)):
                    errors.append(f"{source_id}/{chapter_id}: page markers do not cover its PDF span continuously")
                parent = entry.get("parent")
                if parent:
                    parent_markers.setdefault(parent, set()).update(markers)
                    parent_ranges.setdefault(parent, []).append((start, end))
                body = MARKER.sub("", content)
            elif locator == "section":
                sections = [m.group(1).strip() for m in SECTION_MARKER.finditer(content)]
                if sections != [str(chapter_id)]:
                    errors.append(f"{source_id}/{chapter_id}: section marker does not match its index id")
                body = SECTION_MARKER.sub("", content)
            elif locator == "article":
                if not ARTICLE_MARKER.search(content):
                    errors.append(f"{source_id}/{chapter_id}: no article markers found")
                body = ARTICLE_MARKER.sub("", content)
            elif locator == "document":
                body = content
            else:
                errors.append(f"{source_id}/{chapter_id}: unsupported locator {locator}")
                continue
            actual_words = len(body.split())
            stated_words = entry.get("word_count")
            if not isinstance(stated_words, int) or actual_words < 1 or abs(actual_words - stated_words) > max(10, actual_words * 0.1):
                errors.append(f"{source_id}/{chapter_id}: implausible word count ({stated_words} stated, {actual_words} found)")
        for parent, spans in parent_ranges.items():
            expected = set(range(min(start for start, _ in spans), max(end for _, end in spans) + 1))
            if parent_markers.get(parent, set()) != expected:
                errors.append(f"{source_id}/{parent}: child page markers do not cover the parent span continuously")
    return catalog


def check_s2(args, errors):
    shelf = read_csv(args.shelf, errors)
    for row in shelf:
        if row.get("text_status") in {"text layer", "OCR done"}:
            source_id = row.get("source_id", "")
            if source_id and not (args.chapters / source_id / "index.json").is_file():
                errors.append(f"{source_id}: available shelf source has no chapter index")
    catalog = chapter_catalog(args, errors, True)
    return f"{len(catalog)} indexed chapters"


def check_s3(args, errors):
    lessons = course_map(args.map, errors)
    ids = {lesson.get("id") for lesson in lessons}
    catalog = chapter_catalog(args, errors, False)
    rows = read_csv(args.triage, errors)
    if not rows:
        errors.append("triage has no rows")
    verdicts = set()
    primary = {lesson_id: set() for lesson_id in ids}
    background = {lesson_id: set() for lesson_id in ids}
    no_book = set()
    for n, row in enumerate(rows, 2):
        role = row.get("role", "")
        lesson_id = row.get("lesson_id", "")
        key = (row.get("source_id", ""), row.get("chapter_id", ""))
        if role not in ROLES:
            errors.append(f"triage row {n}: invalid role {role}")
        if not row.get("why"):
            errors.append(f"triage row {n}: missing reason")
        if role == "no_book_covers":
            if lesson_id not in ids or key != ("", ""):
                errors.append(f"triage row {n}: malformed no_book_covers note")
            no_book.add(lesson_id)
            continue
        if key not in catalog:
            errors.append(f"triage row {n}: unknown chapter {key}")
            continue
        if role == "unused":
            if lesson_id:
                errors.append(f"triage row {n}: unused chapter must have blank lesson_id")
            verdicts.add(key)
            continue
        if lesson_id not in ids:
            errors.append(f"triage row {n}: unknown lesson {lesson_id}")
            continue
        if role in {"primary", "supporting"}:
            verdicts.add(key)
        if role == "primary":
            primary[lesson_id].add(key)
        if role == "background":
            background[lesson_id].add(key)
    for key in catalog.keys() - verdicts:
        errors.append(f"chapter {key} has no primary/supporting/unused verdict")
    shelf = read_csv(args.shelf, errors)
    slides = {row.get("lesson_id") for row in shelf if row.get("role") == "slides" and row.get("text_status") != "missing"}
    for lesson in lessons:
        lesson_id = lesson.get("id")
        if lesson_id not in slides:
            errors.append(f"{lesson_id}: no available slide deck in shelf")
        if not primary[lesson_id] and lesson_id not in no_book:
            errors.append(f"{lesson_id}: no primary book chapter or no_book_covers note")
        expected = set().union(*(primary.get(p.get("id"), set()) for p in lesson.get("prerequisites", [])))
        if background[lesson_id] != expected:
            errors.append(f"{lesson_id}: background differs from prerequisite primaries")
    return f"{len(rows)} triage rows / {len(catalog)} chapters"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("s0", "s1", "s2", "s3"))
    parser.add_argument("course")
    parser.add_argument("--map", type=Path)
    parser.add_argument("--shelf", type=Path)
    parser.add_argument("--chapters", type=Path)
    parser.add_argument("--triage", type=Path)
    parser.add_argument("--site", type=Path, default=SITE)
    args = parser.parse_args()
    root = WORKSHOP / "work" / "pipeline" / args.course
    args.map = args.map or root / "course-map.json"
    args.shelf = args.shelf or root / "shelf.csv"
    args.chapters = args.chapters or root / "chapters"
    args.triage = args.triage or root / "triage.csv"
    errors = []
    result = {"s0": check_s0, "s1": check_s1, "s2": check_s2, "s3": check_s3}[args.stage](args, errors)
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if errors:
        print(f"{args.stage.upper()} FAIL: {len(errors)} error(s); {result}", file=sys.stderr)
        return 1
    print(f"{args.stage.upper()} PASS: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
