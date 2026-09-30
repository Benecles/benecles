#!/usr/bin/env python3
"""Check a plan-scoped curation build against its immutable live baseline."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path("/Users/benecles/Documents/Codex/2026-09-23/you-h/work")
R = ROOT / "relay-design-2026-09-29"
FIGURE = re.compile(rb"<figure\b[^>]*>[\s\S]*?</figure\s*>", re.IGNORECASE)


def outside_figures(data: bytes) -> bytes:
    return FIGURE.sub(b"", data)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--baseline", required=True, type=Path, help="course-level immutable baseline root")
    ap.add_argument("--pages", nargs="+", required=True, help="planned lesson basenames for this chunk")
    args = ap.parse_args()

    plan = R / "curation" / f"{args.course}-plan.csv"
    stage_root = R / "site" / "courses" / args.course
    if not plan.is_file():
        print(f"FAIL: plan not found: {plan}")
        return 1
    with plan.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_page: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_page.setdefault(row["page"].strip(), []).append(row)
    selected = set(args.pages)
    unknown = selected - by_page.keys()
    if unknown:
        print(f"FAIL: pages absent from plan: {', '.join(sorted(unknown))}")
        return 1

    failed = False
    for page in sorted(selected):
        baseline_path = args.baseline / page
        stage_path = stage_root / page
        if not baseline_path.is_file() or not stage_path.is_file():
            print(f"FAIL {page}: baseline={baseline_path.is_file()}, staged={stage_path.is_file()}")
            failed = True
            continue
        baseline, staged = baseline_path.read_bytes(), stage_path.read_bytes()
        actions = [row["action"].strip().lower() for row in by_page[page]]
        invalid = [action for action in actions if action not in {"keep", "add", "remove", "delete", "redraw", "reclassify", "reclassify/redraw"}]
        expected = len(FIGURE.findall(baseline)) + actions.count("add") - actions.count("remove") - actions.count("delete")
        count = len(FIGURE.findall(staged))
        text_matches = outside_figures(baseline) == outside_figures(staged)
        passed = not invalid and count == expected and text_matches
        failed |= not passed
        extra = f"; invalid actions={invalid}" if invalid else ""
        if not text_matches:
            extra += "; bytes outside figure blocks changed"
        print(f"{'PASS' if passed else 'FAIL'} {page}: baseline={len(FIGURE.findall(baseline))}, expected={expected}, actual={count}{extra}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
