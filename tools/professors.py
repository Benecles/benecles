#!/usr/bin/env python3
"""Build the shared professor-card data and decorate generated site surfaces.

Run after lesson page generation and before ``tools/offline_build.py``. Course
fronts use the same slot and assets from ``tools/fronts/front.py``.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from fronts import professor_card


CARD = re.compile(r'<a class="prancha" href="courses/([^"/]+)/">(.*?)</a>', re.S)
HERO = re.compile(r'(<header\b[^>]*class=["\'][^"\']*\bhero\b[^"\']*["\'][^>]*>)(.*?)(</header>)', re.S)
KICKER = re.compile(r'(<div\b[^>]*class=["\'][^"\']*\bkicker\b[^"\']*["\'][^>]*>)(.*?)(</div>)', re.S)


def course_data() -> dict[str, dict]:
    rows = {}
    for path in (ROOT / "tools" / "fronts" / "data").glob("*.json"):
        if path.name == "professors.json":
            continue
        rows[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return rows


def ensure_assets(page: str, root_prefix: str) -> str:
    style = professor_card.stylesheet_link(root_prefix)
    scripts = professor_card.script_tags(root_prefix)
    style_pattern = r'<link\b[^>]*href=["\'][^"\']*professor-card\.css(?:\?[^"\']*)?["\'][^>]*>'
    page, style_count = re.subn(style_pattern, style, page, count=1, flags=re.I)
    if not style_count:
        page = page.replace("</head>", style + "\n</head>", 1)
    data_tag, runtime_tag = scripts.split("\n", 1)
    script_pattern = r'<script\b[^>]*src=["\'][^"\']*professor-card\.js(?:\?[^"\']*)?["\'][^>]*>\s*</script>'
    page, script_count = re.subn(script_pattern, runtime_tag, page, count=1, flags=re.I)
    data_pattern = r'<script\b[^>]*src=["\'][^"\']*professors-data\.js(?:\?[^"\']*)?["\'][^>]*>\s*</script>'
    page, data_count = re.subn(data_pattern, data_tag, page, count=1, flags=re.I)
    missing = []
    if not data_count:
        missing.append(data_tag)
    if not script_count:
        missing.append(runtime_tag)
    if missing:
        page = page.replace("</body>", "\n".join(missing) + "\n</body>", 1)
    return page


def decorate_course_page(page: str, slug: str, fallback: str) -> str:
    if "<header" not in page or not HERO.search(page):
        return page

    def hero_repl(hero_match: re.Match) -> str:
        hero = hero_match.group(2)
        kicker_match = KICKER.search(hero)
        if not kicker_match:
            return hero_match.group(0)
        opener, inner, closer = kicker_match.groups()
        if f'data-professor-course="{slug}"' in inner:
            return hero_match.group(0)

        def replace_prof(m: re.Match) -> str:
            return professor_card.name_slot(slug, m.group(1).strip(), "../../")

        updated, count = re.subn(
            r'<span\b[^>]*>\s*((?:Prof\.|Profa\.)\s*[^<]*?)\s*</span>',
            replace_prof,
            inner,
            count=1,
        )
        if not count:
            first = re.search(r'</span\s*>', inner, re.I)
            if not first:
                return hero_match.group(0)
            slot = professor_card.name_slot(slug, fallback, "../../")
            updated = inner[:first.end()] + slot + inner[first.end():]
        kicker = opener + updated + closer
        hero = hero[:kicker_match.start()] + kicker + hero[kicker_match.end():]
        return hero_match.group(1) + hero + hero_match.group(3)

    page = HERO.sub(hero_repl, page)
    if 'class="professor-fallback"' in page:
        page = ensure_assets(page, "../../")
    return page


def abbreviation(name: str) -> str:
    words = name.split()
    particles = {"de", "da", "do", "das", "dos", "e"}
    core = [word for word in words if word.casefold() not in particles]
    if not core:
        return name
    last = core[-1]
    if last.casefold() in {"filho", "neto", "júnior", "junior"} and len(core) > 2:
        last = core[-2]
    return f"{core[0][0]}. {last}"


def home_card(slug: str, body: str, rows: dict[str, dict], profiles: dict[str, dict]) -> str:
    data = rows[slug]
    profile = profiles.get(slug)
    display = abbreviation(profile["name"]) if profile else abbreviation(data.get("prof", "").removeprefix("Profa. ").removeprefix("Prof. "))
    title = data.get("title", slug)
    link = f'courses/{slug}/'
    if re.search(r'<h2>(.*?)</h2>', body, re.S):
        body = re.sub(r'<h2>(.*?)</h2>', f'<h2><a href="{link}">\\1</a></h2>', body, count=1, flags=re.S)
    body = re.sub(r'<span class="go">(.*?)</span>', f'<a class="go" href="{link}">\\1</a>', body, count=1, flags=re.S)
    label = "Profa." if data.get("prof", "").startswith("Profa.") or (profile and profile.get("title", "").startswith("Professora")) else "Prof."
    slot = professor_card.name_slot(slug, display, "")
    cell = f'<span>{label}<b>{slot}</b></span>'
    stamp = re.search(r'(<div class="stamp">)(.*?)(</div>)', body, re.S)
    if stamp:
        cells = list(re.finditer(r'<span>.*?</span>', stamp.group(2), re.S))
        if cells:
            last = cells[-1]
            content = stamp.group(2)
            content = content[:last.start()] + cell + content[last.end():]
            body = body[:stamp.start()] + stamp.group(1) + content + stamp.group(3) + body[stamp.end():]
    return f'<article class="prancha" data-course="{html.escape(slug, quote=True)}">{body}</article>'


def decorate_home(rows: dict[str, dict], profiles: dict[str, dict]) -> None:
    path = ROOT / "index.html"
    page = path.read_text(encoding="utf-8")

    def card_repl(m: re.Match) -> str:
        slug, body = m.groups()
        if slug not in rows:
            return m.group(0)
        return home_card(slug, body, rows, profiles)

    page = CARD.sub(card_repl, page)
    page = page.replace("a.prancha:hover", ".prancha:hover")
    page = page.replace("a.prancha:focus-visible", ".prancha:focus-within")
    page = page.replace(".prancha .go{", ".prancha .go{")
    page = ensure_assets(page, "")
    path.write_text(page, encoding="utf-8")


def decorate_lessons(rows: dict[str, dict]) -> int:
    changed = 0
    for slug, data in rows.items():
        course_dir = ROOT / "courses" / slug
        for path in course_dir.rglob("*.html"):
            if path.name == "index.html":
                continue
            old = path.read_text(encoding="utf-8")
            new = decorate_course_page(old, slug, data.get("prof", "Professor"))
            if new != old:
                path.write_text(new, encoding="utf-8")
                changed += 1
    return changed


def run() -> tuple[int, int]:
    rows = course_data()
    profiles = professor_card.public_profiles()
    public_script = ROOT / "assets" / "professors-data.js"
    public_script.write_text(professor_card.public_data_script(), encoding="utf-8")
    changed = decorate_lessons(rows)
    decorate_home(rows, profiles)
    return len(profiles), changed


def main() -> None:
    count, changed = run()
    print(f"professors: generated {count} profile assignments; decorated {changed} lesson pages and the home cards")


if __name__ == "__main__":
    main()
