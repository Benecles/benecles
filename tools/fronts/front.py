#!/usr/bin/env python3
"""Render the shared D1 course front from extracted JSON and immutable old fronts."""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent          # tools/fronts
R = HERE.parents[1]                              # repo root (the live site)


def _esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)


def _read_old(course: str) -> str:
    old = HERE / "shell" / f"{course}.html"  # head/script shell captured from the pre-D1 front
    if not old.is_file():
        raise FileNotFoundError(f"Missing immutable old front: {old}")
    return old.read_text(encoding="utf-8")


def _head(old: str) -> str:
    m = re.search(r"<head\b[^>]*>.*?</head\s*>", old, re.I | re.S)
    if not m:
        raise ValueError("Old front has no complete <head>")
    head = m.group(0)
    # front.css lives in the root assets/, which assetver doesn't version: stamp a content hash here
    import hashlib
    ver = hashlib.sha1((R / "assets" / "front.css").read_bytes()).hexdigest()[:10]
    head = re.sub(r'<link rel="stylesheet" href="\.\./\.\./assets/front\.css[^"]*">\n?', "", head)
    head = re.sub(r"</head\s*>", f'<link rel="stylesheet" href="../../assets/front.css?v={ver}">\n</head>', head, flags=re.I)
    return head


def _topbar(old: str, data: dict[str, Any]) -> str:
    m = re.search(r"<nav\b[^>]*class=[\"'][^\"']*topbar[^\"']*[\"'][^>]*>.*?</nav>", old, re.I | re.S)
    nav = m.group(0) if m else '<nav class="topbar" aria-label="Navegação principal"><a href="../../index.html">← Ordenações Filipinas</a><span>' + _esc(data.get("code")) + ' · UFRGS · 2026/2</span></nav>'
    items = data.get("info_items_html") or ""
    biblink = '<a class="bibliografia-link" href="#bibliografia">ver bibliografia completa →</a>' if data.get("bibliografia") else ""
    if items and "fontes-card" in nav:
        replacement = ('<div class="fontes-card" role="dialog" aria-label="Fontes do curso"><h2>Fontes do curso</h2>'
                       f'<ul>{items}</ul>{biblink}</div>')
        nav = re.sub(r'(<details\b[^>]*class=["\'][^"\']*fontes-i[^"\']*["\'][^>]*>.*?<summary\b.*?</summary>).*?(</details>)',
                     lambda m: m.group(1) + replacement + m.group(2), nav, count=1, flags=re.I | re.S)
    elif items:
        fallback = ('<details class="fontes-i front-info-fallback"><summary aria-label="Informações sobre o curso">ⓘ</summary>'
                    '<div class="fontes-card" role="dialog" aria-label="Fontes do curso"><h2>Fontes do curso</h2>'
                    f'{items}{biblink}</div></details>')
        toggle = re.search(r'<button\b[^>]*class=["\'][^"\']*theme-toggle[^"\']*["\'][^>]*>.*?</button>', nav, re.I | re.S)
        nav = nav[:toggle.start()] + fallback + nav[toggle.start():] if toggle else nav.replace('</nav>', fallback + '</nav>')
    # Preserve the original topbar's adjacent behavior (notably the sources-card dismissal).
    tail = old[m.end():] if m else ""
    tailmatch = re.match(r"\s*(<script\b[^>]*>.*?</script>)", tail, re.I | re.S)
    return nav + (tailmatch.group(1) if tailmatch else "")


def _scripts(old: str) -> str:
    """Keep the original page scripts verbatim, including course and offline behavior."""
    found = re.findall(r"<script\b[^>]*>.*?</script\s*>", old, re.I | re.S)
    # The head theme bootstrap and topbar-adjacent script are already retained in place.
    # Retain the old body-end script block and any saved-place script inside the exam row.
    selected: list[str] = []
    for script in found:
        if re.search(r"assets/(?:curso|course)\.js|assets/(?:offline|highlight)", script, re.I):
            if script not in selected:
                selected.append(script)
    return "\n".join(selected)


def _title(data: dict[str, Any]) -> str:
    return (f'<header class="front-title"><div class="front-kicker">'
            f'<span>Guia de estudo · {_esc(data.get("area"))} · {_esc(data.get("n_aulas"))} aulas · {_esc(data.get("prof"))}</span></div>'
            f'<h1>{_esc(data.get("title"))}</h1><p class="front-deck">{_esc(data.get("deck"))}</p></header>')


def _drawing(data: dict[str, Any]) -> str:
    drawing = data.get("drawing")
    if not drawing:
        return '<section class="front-drawing" aria-label="Desenho do curso"><div class="front-drawing-empty"><span class="front-label">Desenho do curso</span><p>O percurso visual deste curso será definido na revisão do projeto.</p></div></section>'
    if "inner_html" in drawing:  # reconciled from the live front: markup kept verbatim
        return f'<section class="front-drawing" aria-label="Desenho do curso">{drawing["inner_html"]}</section>'
    art = drawing.get("html", "")
    phone = drawing.get("phone_html") or ""
    if phone:
        art = f'<div class="front-art-desktop">{art}</div><div class="front-art-phone">{phone}</div>'
    # Several preserved drawings already own a framed sheet in their markup/CSS.
    # Keep the shared frame for unframed art only so the new standard adds no second shadow.
    css = drawing.get("css", "")
    owns_frame = bool(re.search(r"border\s*:", css, re.I) and re.search(r"box-shadow\s*:", css, re.I))
    sheet = art if owns_frame else f'<div class="front-sheet">{art}</div>'
    return f'<section class="front-drawing" aria-label="Desenho do curso">{sheet}</section>'


def _exam(data: dict[str, Any], old: str) -> str:
    exam = data.get("exam_html") or ""
    review = data.get("review_href")
    review_row = ""
    if review and not re.search(r'href=[\"\']' + re.escape(str(review)) + r'[\"\']', exam):
        review_row = f'<a class="front-review" href="{_esc(review)}">Abrir revisão <span aria-hidden="true">→</span></a>'
    resume = ""
    # Preserve the saved-place behavior only on fronts that already offered it.
    saved_script = next((s for s in re.findall(r"<script\b[^>]*>.*?</script\s*>", old, re.I | re.S)
                         if "Continuar:" in s or re.search(r"ordenacoes-delito-last|ordenacoes-course-last", s, re.I)), None)
    if saved_script and not re.search(r'class=["\'][^"\']*\bresume\b', exam, re.I):
        resume = '<a class="resume front-resume" href="#" hidden>Continuar: <span></span></a>'
    if not exam and not review and not resume:
        return '<section class="front-exam" aria-label="Avaliações"></section>'
    # Existing exam_html usually already contains the paper card; keep its markup verbatim.
    card = exam if re.search(r'class=["\'][^"\']*\bexam-card\b', exam, re.I) else f'<div class="front-exam-card">{exam}{resume}</div>'
    return (f'<section class="front-exam" aria-label="Avaliações"><div class="front-exam-content">{card}'
            f'{review_row}</div>{saved_script or ""}</section>')


def _lessons(data: dict[str, Any]) -> str:
    if not data.get("units") and data.get("lessons"):
        rows = []
        for lesson in data["lessons"]:
            label = _esc(lesson.get("label", ""))
            title = _esc(lesson.get("title", ""))
            href = _esc(lesson.get("href", "#"))
            extra = ' <span class="complementary-mark">Complementar</span>' if lesson.get("complementary") else ""
            desc = f'<span class="front-lesson-desc">{html.escape(lesson["desc"])}</span>' if lesson.get("desc") else ""
            rows.append(f'<a class="front-lesson-row{" is-complementary" if lesson.get("complementary") else ""}" href="{href}"><span>{label} · {title}{desc}</span>{extra}</a>')
        return ('<section class="front-lessons" id="aulas" aria-labelledby="front-lessons-title">'
                '<div class="front-section-head"><span class="front-label">Caderno de estudo</span><h2 id="front-lessons-title">Aulas</h2></div>'
                '<div class="front-unit-lessons front-flat-lessons">' + "".join(rows) + '</div></section>')
    cards = []
    for unit in data.get("units", []):
        rows = []
        for lesson in unit.get("lessons", []):
            label = _esc(lesson.get("label", ""))
            title = _esc(lesson.get("title", ""))
            href = _esc(lesson.get("href", "#"))
            extra = ' <span class="complementary-mark">Complementar</span>' if lesson.get("complementary") else ""
            desc = f'<span class="front-lesson-desc">{html.escape(lesson["desc"])}</span>' if lesson.get("desc") else ""
            rows.append(f'<a class="front-lesson-row{" is-complementary" if lesson.get("complementary") else ""}" href="{href}"><span>{label} · {title}{desc}</span>{extra}</a>')
        cards.append('<article class="front-unit"><span class="front-unit-label">' + _esc(unit.get("label")) + '</span>'
                     '<h3>' + _esc(unit.get("title")) + '</h3><p class="front-unit-desc">' + _esc(unit.get("desc")) + '</p>'
                     '<div class="front-unit-lessons">' + "".join(rows) + '</div></article>')
    return ('<section class="front-lessons" id="aulas" aria-labelledby="front-lessons-title">'
            '<div class="front-section-head"><span class="front-label">Caderno de estudo</span><h2 id="front-lessons-title">Aulas</h2></div>'
            '<div class="front-unit-grid">' + "".join(cards) + '</div></section>')


def _bibliografia(data: dict[str, Any]) -> str:
    bib = data.get("bibliografia")
    if not bib:
        return ""  # no syllabus found: no section (and no ⓘ link), never a visible "not found" note
    groups = []
    for key, label in (("basica", "Básica"), ("complementar", "Complementar")):
        entries = bib.get(key) or []
        if not entries: continue
        groups.append(f'<div class="front-bib-group"><h3>{label}</h3><ul>' + "".join(f'<li>{_esc(item)}</li>' for item in entries) + '</ul></div>')
    return '<section class="front-bibliografia" id="bibliografia"><h2>Bibliografia</h2>' + "".join(groups) + '</section>'


def render(data: dict[str, Any], slug: str | None = None) -> str:
    """Return one complete front page, using the immutable original as head/script source."""
    # The source JSON's `course` field may be a public course name. CLI callers
    # provide the stable directory slug; hand-written samples can use a slug.
    course = slug or str(data["course"])
    old = _read_old(course)
    drawing = data.get("drawing")
    inline_drawing_css = f'<style data-front-drawing-css>{drawing.get("css", "")}</style>' if drawing and drawing.get("css") else ""
    head_match = re.search(r"<head\b", old, re.I)
    doc_open = old[:head_match.start()] if head_match else '<!doctype html>\n<html lang="pt-BR">\n'
    page_head = _head(old)
    if inline_drawing_css:
        page_head = page_head.replace("</head>", inline_drawing_css + "\n</head>")
    body = (f'{doc_open}{page_head}\n<body>\n{_topbar(old, data)}\n{_title(data)}\n<main class="front-main">'
            f'{_drawing(data)}{_exam(data, old)}{_lessons(data)}{_bibliografia(data)}'
            f'</main>\n<p class="endnote">{data.get("endnote_html") or ""}</p>\n{_scripts(old)}\n</body>\n</html>')
    return body


def write(course: str) -> Path:
    data_path = HERE / "data" / f"{course}.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    rendered = render(data, slug=course)
    target = R / "courses" / course / "index.html"
    target.write_text(rendered, encoding="utf-8")
    print(f"rendered {target.relative_to(R)}")
    return target


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: python3 tools/fronts/front.py <course-slug> [<course-slug> ...]")
    for slug in sys.argv[1:]:
        write(slug)
