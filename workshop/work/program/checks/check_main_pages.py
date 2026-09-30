#!/usr/bin/env python3
"""Mechanical gate for the home and seven course-front capture set."""
import json
import sys
import re
from pathlib import Path

R = Path("/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29")
if len(sys.argv) == 3 and sys.argv[1].endswith("gate-report.json"):
    # Queue invocation: provide the fresh report and its handoff note directly.
    report = Path(sys.argv[1])
    gate = Path(sys.argv[2])
    order_id = gate.stem.removesuffix("-GATE")
    expected_report = R / "program" / f"{order_id}-captures" / "gate-report.json"
    expected_gate = R / "program" / f"{order_id}-GATE.md"
    if report != expected_report or gate != expected_gate:
        raise SystemExit("capture report/GATE paths do not match this staging order")
else:
    order_id = sys.argv[1] if len(sys.argv) > 1 else "main-pages"
    report = None
    gate = None
if not re.fullmatch(r"main-pages(?:-r[12])?", order_id):
    raise SystemExit("usage: check_main_pages.py [main-pages-r1|main-pages-r2]")
report = report or (R / "program" / f"{order_id}-captures" / "gate-report.json")
gate = gate or (R / "program" / f"{order_id}-GATE.md")
if not report.is_file() or not gate.is_file():
    raise SystemExit("main-pages capture report or GATE note is missing")

courses = [
    "controle-de-constitucionalidade",
    "direito-constitucional-i",
    "processo-civil-i",
    "teoria-do-delito",
    "teoria-geral-dos-contratos",
    "direito-latino-americano",
    "metodologia-juridica",
]
expected = {"/"} | {f"/courses/{course}/index.html" for course in courses}
data = json.loads(report.read_text())
results = data.get("results", [])
states = set()
failures = []
for item in results:
    page = item.get("page")
    viewport = item.get("viewport", {}).get("name")
    theme = item.get("theme")
    states.add((page, viewport, theme))
    geometry = item.get("geometry", {})
    if geometry.get("documentOverflow"):
        failures.append(f"{page} {viewport}/{theme}: document overflow")
    if geometry.get("duplicateIds"):
        failures.append(f"{page} {viewport}/{theme}: duplicate IDs")
    if geometry.get("svgTextCollisions"):
        failures.append(f"{page} {viewport}/{theme}: SVG text collisions")
    if item.get("jsErrors"):
        failures.append(f"{page} {viewport}/{theme}: JavaScript errors")
    for svg in geometry.get("svgs", []):
        if svg.get("hostHorizontalOverflow"):
            failures.append(f"{page} {viewport}/{theme}: SVG overflow")
        if svg.get("textOutsideViewBox"):
            failures.append(f"{page} {viewport}/{theme}: SVG text outside viewBox")

missing_pages = expected - {page for page, _, _ in states}
if missing_pages:
    failures.append("missing pages: " + ", ".join(sorted(missing_pages)))
for page in expected:
    got = {(v, t) for p, v, t in states if p == page}
    if got != {("desktop", "light"), ("desktop", "dark"), ("phone", "light"), ("phone", "dark")}:
        failures.append(f"{page}: expected desktop/phone in light/dark; got {sorted(got)}")

if failures:
    print("\n".join(failures))
    raise SystemExit(1)
print(f"PASS: {len(expected)} pages, {len(states)} viewport/theme states, no measured overflow, collisions, duplicate IDs, or JS errors")
