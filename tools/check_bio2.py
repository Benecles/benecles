#!/usr/bin/env python3
"""BIO-2 contract check: source records, shared rendering and required surfaces."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "fronts"))
import professor_card


def main() -> int:
    errors: list[str] = []
    data_dir = ROOT / "tools" / "fronts" / "data"
    profiles = json.loads((data_dir / "professors.json").read_text(encoding="utf-8"))
    courses = {p.stem for p in data_dir.glob("*.json") if p.name != "professors.json"}
    assigned: set[str] = set()
    for profile in profiles:
        bio = profile.get("bio", "")
        sentences = [s for s in re.split(r"(?<=[.!?])\s+", bio.strip()) if s]
        words = bio.split()
        if len(sentences) > 2:
            errors.append(f'{profile.get("name")}: bio has {len(sentences)} sentences')
        if len(words) > 40:
            errors.append(f'{profile.get("name")}: bio has {len(words)} words')
        if bio.casefold().startswith(profile.get("name", "").casefold()):
            errors.append(f'{profile.get("name")}: bio starts with the card heading')
        if re.match(r"^é\s+(?:mestre|doutor|graduad[oa])\b", bio, re.I):
            errors.append(f'{profile.get("name")}: bio opens with a CV credential')
        if not profile.get("sources") or not profile.get("checked"):
            errors.append(f'{profile.get("name")}: sources or checked date missing')
        for slug in profile.get("courses", []):
            if slug not in courses:
                errors.append(f'{profile.get("name")}: unknown course {slug}')
            if slug in assigned:
                errors.append(f"more than one profile is assigned to {slug}")
            assigned.add(slug)

    public_path = ROOT / "assets" / "professors-data.js"
    expected_public = professor_card.public_data_script()
    if not public_path.is_file() or public_path.read_text(encoding="utf-8") != expected_public:
        errors.append("assets/professors-data.js is stale; run python3 tools/professors.py")
    public = public_path.read_text(encoding="utf-8") if public_path.is_file() else ""
    if '"sources"' in public or '"checked"' in public:
        errors.append("private source/check metadata leaked into the public profile asset")

    def current_assets(source: str, root: str) -> bool:
        return (professor_card.stylesheet_link(root) in source and
                professor_card.script_tags(root) in source)

    for slug in sorted(courses):
        front = ROOT / "courses" / slug / "index.html"
        if not front.is_file():
            errors.append(f"missing course front: {slug}")
            continue
        source = front.read_text(encoding="utf-8")
        if f'data-professor-course="{slug}"' not in source:
            errors.append(f"course front has no professor slot: {slug}")
        if not current_assets(source, "../../"):
            errors.append(f"course front has missing or stale shared professor assets: {slug}")
        found_pages = 0
        for page in (ROOT / "courses" / slug).rglob("*.html"):
            if page.name == "index.html":
                continue
            text = page.read_text(encoding="utf-8")
            if '<header class="hero">' not in text or 'class="kicker label"' not in text:
                continue
            found_pages += 1
            if text.count(f'data-professor-course="{slug}"') != 1:
                errors.append(f"{page.relative_to(ROOT)}: expected one professor slot")
            if not current_assets(text, "../../"):
                errors.append(f"{page.relative_to(ROOT)}: shared professor assets missing or stale")
        if not found_pages:
            errors.append(f"no lesson hero kickers found for {slug}")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    if not current_assets(home, ""):
        errors.append("home page has missing or stale shared professor assets")
    for slug in sorted(courses):
        if f'<article class="prancha" data-course="{slug}">' not in home:
            errors.append(f"home course card missing or not keyboard-safe: {slug}")
        if f'data-professor-course="{slug}"' not in home:
            errors.append(f"home course card has no professor slot: {slug}")
    const_i = json.loads((data_dir / "direito-constitucional-i.json").read_text(encoding="utf-8"))
    if "Vivian Caminha" not in const_i.get("prof", ""):
        errors.append("Const I professor no longer matches the established Vivian Caminha record")
    if "direito-constitucional-i" in next((p.get("courses", []) for p in profiles if p.get("name") == "Roberta Camineiro Baggio"), []):
        errors.append("Baggio is still attributed to Const I despite the current course record")

    specimen = (ROOT / "specimen" / "professor.html").read_text(encoding="utf-8") if (ROOT / "specimen" / "professor.html").exists() else ""
    if not current_assets(specimen, "../"):
        errors.append("professor specimen has missing or stale shared professor assets")
    for state in ("closed", "open", "phone", "two-course", "dark"):
        if f'data-state="{state}"' not in specimen:
            errors.append(f"specimen missing {state} state")
    if "exemplo estrutural fictício" not in specimen.casefold():
        errors.append("specimen two-course example is not identified as fictional")

    if errors:
        print("BIO-2 FAIL")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"BIO-2 PASS: {len(profiles)} sourced profiles; {len(courses)} course fronts; lesson kickers, home cards and five specimen states")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
