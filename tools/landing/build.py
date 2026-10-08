#!/usr/bin/env python3
"""Build the Benecles front door (index.html) from real data.

Figures come from the repo itself: the shelf and the triage map are lifted from
backstage/index.html, the commit chart is read from git, the pipeline counts from
workshop/work/pipeline. Run from anywhere: python3 tools/landing/build.py
"""
from __future__ import annotations

import csv
import html
import re
import subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WS = ROOT / "workshop"
OUT = ROOT / "index.html"
GH = "https://github.com/Benecles/benecles"
BLOB = GH + "/blob/main/"
csv.field_size_limit(10**9)

GH_MARK = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def fmt(n: int) -> str:
    return f"{n:,}"


# ---------------------------------------------------------------- data

def git_days() -> tuple[list[tuple[date, int, int]], int]:
    def counts(*args: str) -> Counter:
        out = subprocess.run(["git", "-C", str(ROOT), "log", "--format=%ad", "--date=short", *args],
                             capture_output=True, text=True, check=True).stdout.split()
        return Counter(out)
    allc, ws = counts(), counts("--", "workshop")
    first = min(date.fromisoformat(d) for d in allc)
    last = max(date.fromisoformat(d) for d in allc)
    days, d = [], first
    while d <= last:
        k = d.isoformat()
        days.append((d, allc.get(k, 0) - ws.get(k, 0), ws.get(k, 0)))
        d += timedelta(days=1)
    return days, sum(allc.values())


def triage_counts() -> Counter:
    c: Counter = Counter()
    for f in (WS / "work/pipeline").glob("*/triage.csv"):
        if "processo-civil-i" in str(f):
            for row in csv.DictReader(open(f, encoding="utf-8")):
                c[row["role"]] += 1
    return c


def lift_svg(page: Path, start: str) -> str:
    s = page.read_text(encoding="utf-8")
    i = s.index(start)
    j = s.index("</svg>", i) + len("</svg>")
    svg = s[i:j]
    svg = svg.replace('href="../', 'href="')
    # house floor: no SVG text under 11 px
    return re.sub(r'font:(\d+) (10(?:\.5)?)px', r'font:\1 11px', svg)


# ---------------------------------------------------------------- figures

STATIONS = [
    ("01", "Course map", "Sol · high", "check s0"),
    ("02", "Shelf", "Luna · high", "sha-256"),
    ("03", "Split", "Luna · high", "check s2"),
    ("04", "Triage", "Luna · xhigh", "check s3"),
    ("05", "Folder", "script", "index"),
    ("06", "Plan", "Luna · max", "template"),
    ("07", "Review", "Sol · high", "verdict"),
    ("08", "Write", "Luna · xhigh", "quote_check"),
    ("09", "Finish", "Luna · xhigh", "house_check"),
    ("10", "Check", "CI", "check_all"),
]


def line_svg() -> str:
    w, x0, step, y = 1180, 58, 118, 62
    o = [f'<svg viewBox="0 0 {w} 150" role="img" aria-label="The Benecles line: ten stations from course map to pull request, with a gate after each">']
    o.append('<style>.pl-c{font:600 13px var(--mono);fill:var(--ink)}.pl-n{font:700 15px var(--sans);fill:var(--ink)}'
             '.pl-m{font:500 11px var(--mono);fill:var(--dif)}.pl-k{font:500 11px var(--mono);fill:var(--muted)}'
             '</style>')
    xs = [x0 + i * step for i in range(len(STATIONS))]
    o.append(f'<line x1="{xs[0]}" y1="{y}" x2="{xs[-1]}" y2="{y}" style="stroke:var(--ink);stroke-width:2.5"/>')
    for i, (code, name, model, check) in enumerate(STATIONS):
        x = xs[i]
        if i < len(STATIONS) - 1:
            gx = x + step / 2
            o.append(f'<path d="M{gx} {y-6}L{gx+6} {y}L{gx} {y+6}L{gx-6} {y}Z" style="fill:var(--conc)"/>')
        o.append(f'<circle cx="{x}" cy="{y}" r="9" style="fill:var(--paper);stroke:var(--ink);stroke-width:2.5"/>')
        o.append(f'<text class="pl-c" x="{x}" y="{y-22}" text-anchor="middle">{esc(code)}</text>')
        o.append(f'<text class="pl-n" x="{x}" y="{y+36}" text-anchor="middle">{esc(name)}</text>')
        o.append(f'<text class="pl-m" x="{x}" y="{y+58}" text-anchor="middle">{esc(model)}</text>')
        o.append(f'<text class="pl-k" x="{x}" y="{y+78}" text-anchor="middle">{esc(check)}</text>')
    o.append("</svg>")
    return "".join(o)


ACTORS = ["Benecles", "Claude", "Codex · Sol", "Codex · Luna", "Scripts + CI"]
# per station: actor index -> mark ('w' works, 'g' gates, 'r' reads)
RELAY = [
    {0: "w", 1: "g", 2: "w", 4: "w"},
    {1: "g", 3: "w", 4: "w"},
    {1: "g", 3: "w", 4: "w"},
    {1: "g", 3: "w", 4: "w"},
    {1: "g", 4: "w"},
    {1: "r", 3: "w"},
    {1: "r", 2: "w"},
    {1: "g", 3: "w", 4: "w"},
    {1: "g", 3: "w", 4: "w"},
    {0: "r", 1: "g", 4: "w"},
]


def relay_svg() -> str:
    w, left, top, cw, rh = 1180, 170, 46, 98, 46
    h = top + rh * len(ACTORS) - 4
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Who works at each station: Benecles, Claude, Codex Sol, Codex Luna, and the scripts">']
    o.append('<style>.rg-a{font:600 12px var(--mono);fill:var(--ink)}.rg-s{font:600 12px var(--mono);fill:var(--ink-2)}</style>')
    for j, (code, *_rest) in enumerate(STATIONS):
        cx = left + cw * j + cw / 2
        o.append(f'<text class="rg-s" x="{cx}" y="{top-18}" text-anchor="middle">{esc(code)}</text>')
        o.append(f'<line x1="{cx}" y1="{top-6}" x2="{cx}" y2="{top+rh*len(ACTORS)-14}" style="stroke:var(--ink);stroke-width:.6;opacity:.35"/>')
    for i, a in enumerate(ACTORS):
        cy = top + rh * i + rh / 2 - 6
        o.append(f'<text class="rg-a" x="10" y="{cy+4}">{esc(a)}</text>')
        o.append(f'<line x1="{left}" y1="{cy}" x2="{left+cw*len(STATIONS)}" y2="{cy}" style="stroke:var(--ink);stroke-width:.6;opacity:.35"/>')
        for j, st in enumerate(RELAY):
            m = st.get(i)
            cx = left + cw * j + cw / 2
            if m == "w":
                o.append(f'<circle cx="{cx}" cy="{cy}" r="8" style="fill:var(--ink)"/>')
            elif m == "g":
                o.append(f'<path d="M{cx} {cy-10}L{cx+10} {cy}L{cx} {cy+10}L{cx-10} {cy}Z" style="fill:var(--conc)"/>')
            elif m == "r":
                o.append(f'<circle cx="{cx}" cy="{cy}" r="7" style="fill:none;stroke:var(--dif);stroke-width:2"/>')
    o.append("</svg>")
    return "".join(o)


def commits_svg(days) -> str:
    w, h, base, left = 1180, 230, 186, 40
    n = len(days)
    bw = (w - left - 10) / n
    peak = max(s + k for _, s, k in days)
    sc = (base - 30) / peak
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Commits per day, site and workshop, {days[0][0]:%d %b} to {days[-1][0]:%d %b}">']
    o.append('<style>.cm-k{font:500 11px var(--mono);letter-spacing:.06em;fill:var(--ink-2)}.cm-v{font:600 11px var(--mono);fill:var(--ink)}</style>')
    for frac in (0.5, 1.0):
        yy = base - peak * frac * sc
        o.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{w-10}" y2="{yy:.1f}" style="stroke:var(--ink);stroke-width:.5;opacity:.3"/>')
        o.append(f'<text class="cm-k" x="{left-8}" y="{yy+4:.1f}" text-anchor="end">{round(peak*frac)}</text>')
    for i, (d, s, k) in enumerate(days):
        x = left + i * bw + 2
        bwi = bw - 4
        hs, hk = s * sc, k * sc
        if hs:
            o.append(f'<rect x="{x:.1f}" y="{base-hs:.1f}" width="{bwi:.1f}" height="{hs:.1f}" style="fill:var(--ink)"/>')
        if hk:
            o.append(f'<rect x="{x:.1f}" y="{base-hs-hk:.1f}" width="{bwi:.1f}" height="{hk:.1f}" style="fill:var(--dif)"/>')
        if d.day in (5, 15, 25) or d.day == 1 or i == n - 1:
            o.append(f'<text class="cm-k" x="{x+bwi/2:.1f}" y="{base+20}" text-anchor="middle">{d:%d/%m}</text>')
    o.append(f'<line x1="{left}" y1="{base}" x2="{w-10}" y2="{base}" style="stroke:var(--ink);stroke-width:1.5"/>')
    o.append("</svg>")
    return "".join(o)


def slop_svg() -> str:
    w, h = 560, 190
    rows = [("Human doctrine · 368 texts", 0.14, "ink-2"), ("Our pages, before the rule · 170", 2.43, "conc")]
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Negated inference per thousand words: human doctrine 0.14, our pages 2.43">']
    o.append('<style>.sl-k{font:500 11px var(--mono);letter-spacing:.05em;fill:var(--ink-2)}.sl-v{font:700 22px var(--sans);fill:var(--ink)}</style>')
    sc = 420 / 2.5
    for i, (label, v, tone) in enumerate(rows):
        y = 26 + i * 76
        o.append(f'<text class="sl-k" x="8" y="{y}">{esc(label)}</text>')
        o.append(f'<rect x="8" y="{y+10}" width="{max(v*sc,3):.1f}" height="26" style="fill:var(--{tone})"/>')
        o.append(f'<text class="sl-v" x="{max(v*sc,3)+18:.1f}" y="{y+31}">{v:.2f}</text>')
    o.append(f'<text class="sl-k" x="8" y="{h-8}">PER 1,000 WORDS OF PROSE</text>')
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- page

def intake() -> tuple[list[tuple[int, str]], int, int, int]:
    """The reading list of one job (Processo Civil I), measured from its chapter indexes."""
    import json
    P = WS / "work/pipeline/processo-civil-i"
    rows = list(csv.DictReader(open(P / "shelf.csv", encoding="utf-8")))
    priv = Path.home() / "Developer/ordenacoes-filipinas-workshop/work/pipeline/processo-civil-i/chapters"
    items, pages, words = [], 0, 0
    for r in rows:
        f = priv / r["source_id"] / "index.json"
        if not f.exists():
            continue
        d = json.load(open(f, encoding="utf-8"))
        ch = d.get("chapters", []) if isinstance(d, dict) else d
        pe = [c.get("pdf_end") for c in ch if isinstance(c, dict) and c.get("pdf_end")]
        n = max(pe) if pe else 0
        pages += n
        words += sum(c.get("word_count", 0) for c in ch if isinstance(c, dict))
        items.append((n, r["title"]))
    items.sort(reverse=True)
    return items, pages, words, len(rows)


SHORT_TITLES = {
    "Marinoni/Arenhart/Mitidiero, Novo Curso, vol. 2 (procedimento comum)": "Marinoni et al. · Novo Curso, vol. 2",
    "Didier Jr., Curso de direito processual civil, vol. 1, 19ª ed. (2017)": "Didier Jr. · Curso, vol. 1",
    "Marinoni/Arenhart/Mitidiero, Novo Curso, vol. 1 (2017)": "Marinoni et al. · Novo Curso, vol. 1",
    "Taruffo, La prova dei fatti giuridici (1992)": "Taruffo · La prova dei fatti giuridici",
    "Barbosa Moreira, Temas de Direito Processual: Quarta Série (1989)": "Barbosa Moreira · Temas, 4ª série",
    "Mitidiero, Processo Civil, 2ª ed. (2022)": "Mitidiero · Processo Civil",
}



# ---------------------------------------------------------------- the lesson's own figures

def proc_lessons() -> list[tuple[str, int]]:
    """Published Processo Civil I lessons in syllabus order, with their reading time."""
    out = []
    for p in (ROOT / "courses/processo-civil-i").glob("aula-*.html"):
        m = re.findall(r"≈ *(\d+) *min", p.read_text(encoding="utf-8"))
        if m:
            out.append((p.stem.replace("aula-", ""), int(m[0])))

    def key(item):
        num, _, suffix = item[0].partition("-")
        return (int(num), suffix != "", suffix)
    return sorted(out, key=key)


STEPS = [  # (code, short name, big number, unit, excerpt lines, card title, card text)
    ("01", "Course map", "22", "lessons on the map",
     ["aula-06-citacao · week 7 · exam P1", "task: Ler AR, edital, mandado e certidão",
      "      e identificar o ato registrado"],
     "The syllabus is read in its own order",
     "Each topic of the syllabus becomes a lesson, with one line on what the student must be able to do afterwards and links to the earlier lessons it builds on."),
    ("02", "Shelf", "42", "sources catalogued",
     ["didier-curso-vol1-2017 · book_base", "Curso de direito processual civil, vol. 1", "sha256 4afef9ce79a… · text layer"],
     "Every source is catalogued",
     "Each book, slide deck, decision and exam gets a row with its edition, its file and a SHA-256 fingerprint of that file. A book that never arrives stays listed as missing, and nothing from memory stands in for it."),
    ("03", "Chapters", "1,283", "chapters cut",
     ["===== p. 684 (PDF 682) =====", "CAPÍTULO 17 · Citação", "PDF 681–698 · 7,399 words"],
     "Books are cut into chapters",
     "Each book is cut along its own table of contents, and every page keeps its printed number. A script then confirms that no page is missing or counted twice."),
    ("04", "Triage", "28,285", "decisions written down",
     ["ch17 → aula-06-citacao · primary", "why: the bounded chapter on citação", "     supplies the essential doctrine"],
     "Each chapter is matched to the lessons it serves",
     "Every chapter is weighed against every lesson, and each decision is written down with its reason, rejections included."),
    ("05", "Folder", "76", "files in Aula 06's folder",
     ["20-primary-001-didier…-ch17.txt", "30-supporting-001…029 · CPC arts.", "50-exercises-and-exams.txt"],
     "Each lesson's material goes into one folder",
     "A script copies the chosen chapters, statute articles and exam questions into the lesson's folder and writes an index tracing every file to its page."),
    ("06", "Plan", "18.4 : 1", "source words per lesson word",
     ["Can do after reading:", "1. Read an AR, edital or mandado and", "   name the communication act recorded"],
     "The lesson is planned before it is written",
     "The plan names the tasks a student can do after reading, the exam traps, each section with its source pages, and each figure with the claim it carries."),
    ("07", "Review", "2", "rounds before approval",
     ["round 1 · REVISE · five numbered points", "round 2 · APPROVED", "“Figures use the actual records”"],
     "A second reader checks the plan",
     "A different model reads the plan against the syllabus and the exam questions. It approves the plan or returns it with at most five numbered objections, and a plan returned twice goes to Claude."),
    ("08", "Writing", "≈ 23", "minutes to read Aula 06",
     ["prose and figures in one context", "from the approved plan", "one writer per lesson"],
     "Text and figures are written together",
     "One writer drafts the prose and draws the figures in a single sitting, from the plan, so a figure and the paragraph beside it make the same claim."),
    ("09", "Finish", "≥ 4", "source blocks per lesson",
     ["blue · what a court decided", "orange · where a rule stops", "source block · reference in its header"],
     "Every page gets the same finish",
     "Marks, source blocks and type are shared across the site. Blue marks what a court decided, orange marks where a rule stops, and each quotation sits in a source block with its reference in the header."),
    ("10", "Checks", "7", "scripts before it goes live",
     ["quote_check · slop_lint · house_check", "marks_lint · breakscan", "check_all · offline build"],
     "Scripts read the page before it goes live",
     "A pull request waits until every script passes, and the main branch is the live site."),
]


def planta_svg(lessons, items, pages) -> str:
    """The hero planta: what arrives (bars = pages), the line, what a student opens (bars = minutes)."""
    W, H = 1080, 480
    o = [f'<svg class="planta" viewBox="0 0 {W} {H}" role="img" aria-label="Processo Civil I: {len(items)} sources and {fmt(pages)} pages go down ten steps and come out as {len(lessons)} lessons">']
    o.append('<style>.pk{font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;fill:var(--ink-2)}'
             '.pn{font:400 12px var(--mono);fill:var(--ink)}.pc{font:600 12px var(--mono);fill:var(--ink)}'
             '.ps{font:500 11px var(--mono);fill:var(--muted)}.pt{font:700 15px var(--sans);fill:var(--ink)}'
             '.planta a:hover .pt,.planta a:focus .pt{fill:var(--conc)}</style>')
    # left: the pile, one bar per source, length = pages
    lx, ly, lw = 20, 64, 250
    o.append(f'<text class="pk" x="{lx}" y="30">What arrives</text>')
    o.append(f'<text class="ps" x="{lx}" y="48">{len(items)} sources with page counts · bar = pages</text>')
    mx = max(n for n, _ in items)
    y = ly
    for n, t in items[:6]:
        w = lw * n / mx
        o.append(f'<rect x="{lx}" y="{y:.1f}" width="{w:.1f}" height="16" style="fill:var(--ink);opacity:.85"/>')
        o.append(f'<text class="pn" x="{lx + w + 8:.1f}" y="{y + 12.5:.1f}">{fmt(n)}</text>')
        y += 26
    rest = sum(n for n, _ in items[6:])
    w = lw * rest / mx
    o.append(f'<rect x="{lx}" y="{y:.1f}" width="{w:.1f}" height="16" style="fill:var(--ink);opacity:.4"/>')
    o.append(f'<text class="pn" x="{lx + w + 8:.1f}" y="{y + 12.5:.1f}">{fmt(rest)} · {len(items) - 6} shorter sources together</text>')
    y += 26
    o.append(f'<text class="pc" x="{lx}" y="{y + 22:.1f}">{fmt(pages)} pages</text>')
    pile_bottom = y
    # middle: the line, ten steps, each a link to the chapter that explains it
    cx, top, step = 520, 46, 40
    o.append(f'<text class="pk" x="{cx + 20}" y="30">The line</text>')
    o.append(f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{top + step * 9}" style="stroke:var(--ink);stroke-width:2.5"/>')
    for i, (code, name, big, unit, *_r) in enumerate(STEPS):
        yy = top + step * i
        o.append(f'<a href="#c3"><circle cx="{cx}" cy="{yy}" r="8" style="fill:var(--paper);stroke:var(--ink);stroke-width:2.5"/>')
        o.append(f'<text class="ps" x="{cx - 20}" y="{yy + 4}" text-anchor="end">{code}</text>')
        o.append(f'<text class="pt" x="{cx + 20}" y="{yy + 5}">{esc(name)}</text>')
        o.append(f'<text class="ps" x="{cx + 20 + len(name) * 8.6 + 10:.0f}" y="{yy + 5}">{esc(big)}</text></a>')
    # threads: pile into the line, line out to the lessons (no arrowheads, no text crossed)
    o.append(f'<path d="M{lx + lw + 60} {ly + 8}C{cx - 60} {ly + 8} {cx} {top - 40} {cx} {top - 10}" style="fill:none;stroke:var(--ink-2);stroke-width:1.2;opacity:.6"/>')
    # right: what a student opens, one bar per lesson, length = minutes
    rx, ry, rw = 790, 64, 210
    o.append(f'<text class="pk" x="{rx}" y="30">What a student opens</text>')
    o.append(f'<text class="ps" x="{rx}" y="48">{len(lessons)} lessons · bar = minutes</text>')
    mm = max(m for _, m in lessons)
    for k, (lid, m) in enumerate(lessons):
        yy = ry + k * 19
        w = rw * m / mm
        hot = lid == "06-citacao"
        o.append(f'<a href="courses/processo-civil-i/aula-{lid}.html"><rect x="{rx + 34}" y="{yy}" width="{w:.1f}" height="11" style="fill:var(--{"conc" if hot else "dif"});opacity:{1 if hot else .75}"/>')
        code = lid.split('-')[0] + (lid.split('-')[1][0] if '-' in lid else '')
        o.append(f'<text class="ps" x="{rx + 28}" y="{yy + 10}" text-anchor="end">{code}</text>')
        o.append(f'<text class="pn" x="{rx + 40 + w:.1f}" y="{yy + 10}">{m}′</text></a>')
    end = top + step * 9
    o.append(f'<path d="M{cx} {end + 10}C{cx} {end + 40} {rx - 20} {end + 40} {rx - 20} {end - 20}L{rx - 20} {ry + 6}" style="fill:none;stroke:var(--ink-2);stroke-width:1.2;opacity:.6"/>')
    o.append(f'<text class="pc" x="{rx}" y="{ry + len(lessons) * 19 + 22}">{len(lessons)} lessons · {min(m for _, m in lessons)} to {mm} min</text>')
    o.append("</svg>")
    return "".join(o)


def panel_svg(i: int) -> str:
    """Scrolly panel i: the ten steps as a track, the current one lit, its number and a real excerpt."""
    W, H = 656, 520
    code, name, big, unit, lines, *_ = STEPS[i]
    o = [f'<svg class="panel figkit{" on" if i == 0 else ""}" id="p-st{i}" viewBox="0 0 {W} {H}" role="img" aria-label="Step {code}, {esc(name)}: {esc(big)} {esc(unit)}">']
    o.append('<style>.sk{font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;fill:var(--ink-2)}'
             '.sb{font:800 92px var(--sans);fill:var(--ink)}.su{font:500 13px var(--mono);letter-spacing:.06em;fill:var(--ink-2)}'
             '.sx{font:400 14px var(--mono);fill:var(--ink)}.sc{font:600 12px var(--mono);fill:var(--ink)}</style>')
    x0, x1, y = 36, 620, 70
    o.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" style="stroke:var(--ink);stroke-width:2"/>')
    for j in range(len(STEPS)):
        x = x0 + (x1 - x0) * j / (len(STEPS) - 1)
        if j < i:
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="6" style="fill:var(--ink)"/>')
        elif j == i:
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="11" style="fill:var(--conc)"/>')
        else:
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="6" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.6"/>')
        o.append(f'<text class="sc" x="{x:.1f}" y="{y - 22}" text-anchor="middle" style="fill:var(--{"conc" if j == i else "ink-2"})">{STEPS[j][0]}</text>')
    o.append(f'<text class="sk" x="{x0}" y="150">{code} · {esc(name)}</text>')
    o.append(f'<text class="sb" x="{x0 - 4}" y="250">{esc(big)}</text>')
    o.append(f'<text class="su" x="{x0}" y="284">{esc(unit)}</text>')
    o.append(f'<rect x="{x0}" y="326" width="{x1 - x0}" height="{40 + 26 * len(lines)}" style="fill:var(--paper-2);stroke:var(--ink);stroke-width:1.5"/>')
    o.append(f'<text class="sk" x="{x0 + 16}" y="350">Aula 06 · citação e intimação</text>')
    for k, line in enumerate(lines):
        o.append(f'<text class="sx" x="{x0 + 16}" y="{380 + 26 * k}" xml:space="preserve">{esc(line)}</text>')
    o.append("</svg>")
    return "".join(o)


def fonte(kind: str, head: str, loc: str, body: str, lang: str = "en") -> str:
    cls = "fonte" + (f" {kind}" if kind else "")
    return (f'<aside class="{cls}" aria-label="Fonte: {esc(head)}"><header><span>{head}</span><span class="loc">{loc}</span></header>'
            f'<blockquote lang="{lang}"><p>{body}</p></blockquote></aside>')


def build() -> str:
    days, total_commits = git_days()
    tc = triage_counts()
    items, pages, words, nsrc = intake()
    lessons = proc_lessons()
    routing = lift_svg(ROOT / "backstage/index.html", '<svg viewBox="0 0 1200 600"')
    planta = planta_svg(lessons, items, pages)
    panels = "".join(panel_svg(i) for i in range(len(STEPS)))
    cards = "".join(
        f'<div class="step" data-panel="p-st{i}"><div class="card"><span class="label {"conc" if i == 6 else "dif"}">{s[0]} · {esc(s[1])}</span><h3>{esc(s[5])}</h3><p>{s[6]}</p></div></div>'
        for i, s in enumerate(STEPS))
    first = days[0][0]

    gallery = ''.join(f'<a class="g g-{k}" href="{href}"><img src="assets/gallery/{img}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"><span><span class="gk">{esc(kind)}</span>{esc(cap)}</span></a>' for k, href, img, w, h, kind, cap, alt in [
        ("map", "courses/direito-latino-americano/index.html", "map.jpg", 1252, 1208, "Maps", "Five courts on one map, each route a lesson where one court answered another.", "Map of South America with five courts and numbered routes between their decisions"),
        ("plan", "courses/controle-de-constitucionalidade/index.html", "planta.jpg", 1600, 1353, "Course indexes", "The semester drawn as one plan. Each piece opens its lesson.", "The semester plan of Controle de Constitucionalidade"),
        ("cal", "specimen/instrumentos.html", "calendar.jpg", 1600, 905, "Instruments", "A 15-day deadline counted on the April 2015 calendar, holidays skipped.", "April 2015 calendar with fifteen working days counted"),
        ("reg", "courses/processo-civil-i/index.html", "register.jpg", 1600, 1067, "The register", "Every lesson in syllabus order, with the task it trains and its reading time.", "The class register of Processo Civil I"),
        ("bal", "specimen/instrumentos.html", "balance.jpg", 1600, 1141, "Instruments", "Art. 373 as a balance, with each party's facts on its own pan.", "Article 373 of the CPC drawn as a balance"),
        ("seat", "specimen/instrumentos.html", "seating.jpg", 1600, 890, "Instruments", "The parties of a 2015 exam question seated in the joinder chart.", "A joinder chart with an exam's parties seated"),
        ("atlas", "courses/direito-latino-americano/aula-01.html", "atlas.jpg", 1070, 1070, "Maps", "The Americas in 1808, on a timeline that runs to 1824.", "The Americas in 1808"),
    ])

    body = f'''
<header class="hero">
  <div class="kicker label"><span>Benecles.dev</span><span>Course compilers</span><span>Porto Alegre · 2026</span></div>
  <h1><span class="split">From a reading list</span><span class="split">to a course</span></h1>
  <p class="deck">Benecles.dev builds study websites from the material a course already has. Processo Civil I at UFRGS assigns <strong class="conc">{fmt(pages)} pages</strong>; its students read them as <strong class="dif">{len(lessons)} lessons</strong> of {min(m for _, m in lessons)} to {max(m for _, m in lessons)} minutes.</p>
  <figure class="hero-planta">{planta}<figcaption><span>Fig. 0 · Processo Civil I, from what arrives to what a student opens</span><span>{nsrc} sources · {len(lessons)} lessons</span></figcaption></figure>
  <div class="titleblock label" role="list"><div role="listitem">Founded<b>September 2026</b></div><div role="listitem">Based<b>Porto Alegre, Brazil</b></div><div role="listitem">Contact<b><a href="mailto:benecles@benecles.dev">benecles@benecles.dev</a></b></div><div role="listitem">Reading<b>≈ 10 min</b></div></div>
</header>

<section class="chapter" aria-labelledby="c1"><span class="num dif" aria-hidden="true">01</span><h2 id="c1">What we build</h2><p class="lede">What does a client hand over, and what comes back?</p></section>
<div class="longform"><div>
<div class="bet"><div><span class="bet-k">Before reading, a guess</span><p class="bet-q">For Processo Civil I, every chapter of every assigned source was weighed against every lesson, {fmt(sum(tc.values()))} decisions in all. How many of those decisions made a chapter one of a lesson's primary sources?</p><div class="bet-opts"><button type="button" data-opt="0" aria-pressed="false">About 9,000, roughly one in three.</button><button type="button" data-opt="1" aria-pressed="false">About 2,800, roughly one in ten.</button><button type="button" data-opt="2" data-court aria-pressed="false">{fmt(tc["primary"])}.<span class="who">triage.csv, Processo Civil I</span></button><button type="button" data-opt="3" aria-pressed="false">None. The lessons were written from the slides.</button></div><div class="bet-reveal"><p>{fmt(tc["primary"])}. Another {fmt(tc["supporting"])} decisions made a chapter supporting material, and {fmt(tc["unused"])} set a chapter aside, each with its reason written down. A lesson is built from a few chapters read closely.</p></div></div></div>
<p>A client sends the books, slide decks, court decisions, statutes and past exams a course uses. We return one website of short lessons. Each lesson covers one topic of the syllabus, carries figures drawn for it, and quotes a source only after a script has found the quoted words in it. The first set, seven law courses for the 2026/2 semester at UFRGS, is already read by law students at UFRGS and USP.</p>
<ul class="who-list">
<li><span class="runin">A professor.</span> Your books, slide decks and assigned decisions become one site your students browse by class, and a quotation from your book carries the book's page in its header.</li>
<li><span class="runin">A university.</span> Every course in a curriculum follows the same lesson format, figures and sourcing, so a student who has read one course knows how to read the next.</li>
<li><span class="runin">A company.</span> Contracts, reports, regulations and case files become one compendium, cut into parts, filed under the questions they answer and traceable to the page.</li>
<li><span class="runin">A tutoring school.</span> Your syllabus and your students' past exams become a course whose lessons close with the exam's own questions.</li>
</ul>
</div></div>

<section class="chapter" aria-labelledby="c2"><span class="num dif" aria-hidden="true">02</span><h2 id="c2">What a course contains</h2><p class="lede">What does a student find when the site opens?</p></section>
<div class="wide"><figure class="gal-fig"><div class="gal">{gallery}</div><figcaption><span>Fig. 1 · Taken from the courses already published</span><span>open any piece</span></figcaption></figure></div>

<section class="chapter" aria-labelledby="c3"><span class="num dif" aria-hidden="true">03</span><h2 id="c3">How a course is made</h2><p class="lede">What happens between the reading list and the published lesson?</p></section>
<div class="longform"><div><p>The specimens below follow one lesson, Processo Civil I, Aula 06, on <i>citação</i> and <i>intimação</i>, the court acts that tell a party it is being sued and keep it informed of each step that follows. The course is understood first, its material prepared second, and only then written.</p></div></div>
<div class="scrolly">
 <div class="stage" aria-hidden="true"><figure>{panels}<figcaption><span>Fig. 2 · The ten steps, with Aula 06's record at each</span><span class="stage-step">1 / 10</span></figcaption></figure></div>
 <div class="steps">
{cards}
 </div>
</div>
<div class="wide"><figure class="bp"><div class="cap"><span>Fig. 3 · Processo Civil I · which chapter feeds which lesson</span><span><span class="n">{fmt(tc["primary"])}</span> primary · {fmt(tc["supporting"])} supporting · {fmt(tc["unused"])} set aside</span></div>{routing}</figure></div>

<section class="chapter" aria-labelledby="c4"><span class="num dif" aria-hidden="true">04</span><h2 id="c4">What holds a page back</h2><p class="lede">What stops a bad page from going live?</p></section>
<div class="longform"><div>
<p>Models write the pages and scripts decide whether they ship. A script is trusted only after it has held back a page known to be bad. Seven of them read every lesson: <span class="term" tabindex="0" data-def="The script that finds every quoted passage of six or more words in the course's source texts.">quote_check</span> finds each quotation in the sources, slop_lint measures the prose against human legal writing, house_check and marks_lint confirm the shared finish, breakscan looks for clipped text at desktop width, and two CI checks rebuild the course indexes and the offline copy on every push.</p>
{fonte("lim", "Panel · Processo Civil I, Aula 13", "first round", "<span class=\"key\">Verdict: REVISE.</span> The section architecture and source ledger are strong, but the chosen real case cannot carry the proposed CPC/2015 route as written.")}
<p>A plan can be held back before a word of the lesson exists. The reviewing model reads the plan, the course map, the folder's index and the exam questions, and its verdict binds the writer. A plan returned twice goes to Claude. Aula 06 passed on its second round.</p>
{fonte("dec", "Panel · Processo Civil I, Aula 06", "second round", "<span class=\"key\">APPROVED</span> [...] Figures 1, 2 and 4 use the actual records as inspectable objects.")}
<p>The prose rules were measured before they were trusted. In 368 texts of human legal doctrine, negated inference (phrases like “não basta”) ran at 0.14 per thousand words; on 170 of our pages it ran at 2.43, and the rule now <span class="limit">caps it at 0.5</span>. Every other rule in slop_lint has its limit where no more than one human text in ten would be flagged.</p>
</div></div>
<div class="wide"><figure class="bp"><div class="cap"><span>Fig. 4 · Negated inference per 1,000 words</span><span><a href="{BLOB}workshop/work/slop-bench/BACKTEST.md">method</a></span></div>{slop_svg()}</figure></div>

<section class="chapter" aria-labelledby="c5"><span class="num dif" aria-hidden="true">05</span><h2 id="c5">Who does the work</h2><p class="lede">Who decides, who writes, and who checks?</p></section>
<div class="longform"><div>
<p>Benecles chooses the courses, sets the priorities and decides what gets cut. Claude runs the editorial side through Claude Code. It writes the <span class="term" tabindex="0" data-def="A specification of what a piece of work is, how it must look and what it must never do, written before anyone builds it.">brief</span> for each step, owns the writing standard and the design system, draws figures, rebuilds reference lessons by hand and signs off every step. Codex supplies the volume. An orchestrator splits each brief into units of six or fewer and runs up to sixteen workers at once. The scripts decide what passes.</p>
{fonte("", "CEO.md · mandate 8", "the brief", "The CEO’s job is the WHAT: take the chairman’s thin idea and develop it to the fullest (what it is, what it looks like, where it sits, how it behaves, what it must never do, how it fits the house and its ethos), then hand that to the orchestrator as a master brief. The HOW is the orchestrator’s.")}
<p>A new Claude session reads <a href="{BLOB}workshop/CEO.md">CEO.md</a> first and continues from where the previous session stopped. Claude signs off eight of the ten steps, and the scripts work at the same eight.</p>
</div></div>
<div class="wide"><figure class="bp"><div class="cap"><span>Fig. 5 · Who works at each step</span><span>● works · <span class="n">◆</span> signs off · ○ reads</span></div>{relay_svg()}</figure></div>

<section class="chapter" aria-labelledby="c6"><span class="num dif" aria-hidden="true">06</span><h2 id="c6">How mistakes stay fixed</h2><p class="lede">What happens after a fault is found?</p></section>
<div class="longform"><div>
<p>Two records change. The bug catalogue gains a row naming the symptom, its cause, the fix and the check that now catches it.</p>
{fonte("", "BUGS.md · one row of 53", "Layout and CSS", "<span class=\"bug\"><span>symptom</span>Prose hugs the left edge of a wide screen (x = 0) while headings sit centred</span><span class=\"bug\"><span>cause</span>&lt;div class=\"prosa\"&gt; placed directly in &lt;body&gt;; house prose lives inside .wide</span><span class=\"bug\"><span>fix</span>Wrap in &lt;div class=\"wide\"&gt;; prose then aligns with the chapter heading</span><span class=\"bug\"><span>catches it</span><span class=\"key\">anatomy_check LOOSE-PROSA (in check_all)</span></span>")}
<p>The flight log gains a numbered rule that every lesson in progress applies before its next step.</p>
{fonte("lim", "FLIGHT-LOG.md · F-022 of 32", "S5a, S5", "A fictional “Comunidade C” carried the lesson while real Brazilian material exists. <span class=\"key\">Carriers are real: an article of the CF, a case, a statute.</span>")}
<p>The site and the workshop behind it hold {fmt(total_commits)} commits since {first.day} {first:%B}, merged with their dates intact; the workshop's source texts were removed from every commit, and the ledgers that describe them remain.</p>
</div></div>
<div class="wide"><figure class="plate-fig"><div class="cap"><span>Fig. 6 · Commits per day</span><span>■ site · <span class="sw">■</span> workshop</span></div>{commits_svg(days)}</figure></div>

<section class="chapter" aria-labelledby="c7"><span class="num" aria-hidden="true">07</span><h2 id="c7">Test</h2><p class="lede">Answer before opening.</p></section>
<div class="wide">
<div class="quiz">
<details><summary>What happens to a book a client never sends?</summary><p>It stays on the shelf as a row marked missing, and its place is never filled from a summary or a model's memory.</p></details>
<details><summary>Why does a different model review the plan?</summary><p>The writer knows the material too well to see what the plan leaves out. The reviewer reads only the plan, the course map, the folder's index and the exam questions, the way a thesis committee reads a proposal.</p></details>
<details><summary>Where is a quotation checked?</summary><p>quote_check looks for every quoted passage of six or more words in the course's source texts before the pull request, and a cut without “[...]” counts as a failure.</p></details>
</div>
</div>
<nav class="endnav" aria-label="Next"><a href="{GH}"><span>← Repository</span>github.com/Benecles/benecles</a><a href="ordenacoes-filipinas/" style="text-align:right"><span>First course set →</span>Ordenações Filipinas</a></nav>
'''

    ld = ('{"@context":"https://schema.org","@type":"Organization","name":"Benecles.dev","url":"https://benecles.dev/",'
          '"email":"benecles@benecles.dev","foundingDate":"2026-09","address":{"@type":"PostalAddress","addressLocality":"Porto Alegre","addressCountry":"BR"},'
          '"description":"Benecles.dev builds study websites from the material a course already has, with Claude running the editorial pipeline.",'
          '"sameAs":["https://github.com/Benecles/benecles"]}')

    return f'''<!doctype html>
<html lang="en">
<head>
<script>(function(){{var k='ordenacoes-theme',r=document.documentElement;try{{if(localStorage.getItem(k)==='dark')r.dataset.theme='dark'}}catch(e){{}}document.addEventListener('DOMContentLoaded',function(){{var b=document.querySelector('.theme-toggle');if(!b)return;function sync(){{b.setAttribute('aria-pressed',r.dataset.theme==='dark')}}sync();b.addEventListener('click',function(){{var d=r.dataset.theme!=='dark';if(d)r.dataset.theme='dark';else delete r.dataset.theme;try{{localStorage.setItem(k,d?'dark':'light')}}catch(e){{}}sync()}})}})}})()</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Benecles.dev · from a reading list to a course</title>
<meta name="description" content="Benecles.dev builds study websites from the material a course already has: books, slides, decisions, statutes and past exams, published as short lessons with drawn figures and checked quotations. Built with Claude.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Benecles.dev">
<meta property="og:title" content="Benecles.dev · from a reading list to a course">
<meta property="og:description" content="Study websites built from the material a course already has, with Claude running the editorial pipeline.">
<meta property="og:url" content="https://benecles.dev/">
<meta property="og:image" content="https://benecles.dev/assets/benecles-og.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{ld}</script>
<link rel="icon" href="favicon.ico">
<link rel="stylesheet" href="assets/casa.css">
<link rel="stylesheet" href="courses/direito-latino-americano/assets/curso.css">
<link rel="stylesheet" href="assets/benecles.css">
</head>
<body class="benecles">
<nav class="topbar"><a href="./">Benecles.dev</a><span><a href="#c1">What we build</a> · <a href="#c3">How it is made</a> · <a href="#c5">Who does the work</a> · <a href="ordenacoes-filipinas/">First course set</a> · <a href="{GH}">GitHub ↗</a></span><button class="theme-toggle" type="button" aria-pressed="false" title="Night mode"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Night mode</span></button></nav>
{body}
<footer class="bfoot"><span>Benecles.dev · Porto Alegre, Brazil · <a href="mailto:benecles@benecles.dev">benecles@benecles.dev</a></span><span><a href="{GH}">GitHub ↗</a> · Built with Claude</span></footer>
<script src="courses/direito-latino-americano/assets/curso.js"></script>
<script src="assets/casa.js" defer></script>
</body>
</html>
'''


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
