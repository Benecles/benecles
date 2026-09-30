#!/usr/bin/env python3
"""Mechanical capture gate for the three redrawn course-front diagrams."""
import json
from pathlib import Path

R = Path("/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29")
report = R / "program/front-drawings-r1-captures/gate-report.json"
gate = R / "program/front-drawings-r1-GATE.md"
if not report.is_file() or not gate.is_file():
    raise SystemExit("front-drawings-r1 capture report or GATE note is missing")

courses = ["direito-constitucional-i", "processo-civil-i", "controle-de-constitucionalidade"]
expected = {f"/courses/{course}/index.html" for course in courses}
data = json.loads(report.read_text())
results = data.get("results", [])
states = set()
errors = []
for item in results:
    page = item.get("page")
    viewport = item.get("viewport", {}).get("name")
    theme = item.get("theme")
    states.add((page, viewport, theme))
    g = item.get("geometry", {})
    if g.get("documentOverflow") or g.get("duplicateIds") or g.get("svgTextCollisions") or item.get("jsErrors"):
        errors.append(f"{page} {viewport}/{theme}: page errors, duplicate IDs, or collisions")
    for svg in g.get("svgs", []):
        if svg.get("hostHorizontalOverflow") or svg.get("textOutsideViewBox"):
            errors.append(f"{page} {viewport}/{theme}: SVG overflow or text outside viewBox")

pages = {p for p, _, _ in states}
if pages != expected:
    errors.append(f"expected exactly {sorted(expected)}, captured {sorted(pages)}")
for page in expected:
    got = {(v, t) for p, v, t in states if p == page}
    required = {("desktop", "light"), ("desktop", "dark"), ("phone", "light"), ("phone", "dark")}
    if got != required:
        errors.append(f"{page}: expected four viewport/theme states, got {sorted(got)}")
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print(f"PASS: {len(expected)} front drawings in {len(states)} viewport/theme states; no measured overflow, SVG spill, duplicate IDs, JS errors, or collisions")
