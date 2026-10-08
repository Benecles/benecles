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

def spec(title: str, body: str, href: str | None = None, cls: str = "") -> str:
    link = f'<a href="{esc(href)}">open ↗</a>' if href else ""
    return f'<figure class="spec {cls}"><header><span>{title}</span>{link}</header><div class="b">{body}</div></figure>'


def stage(no: str, model: str, title: str, text: str, chips: list[tuple[str, str]], art: str, extra: str = "") -> str:
    ch = "".join(f'<span class="chip {c}">{esc(t)}</span>' for t, c in chips)
    return (f'<div class="stage"><div class="no">{no}<small>{esc(model)}</small></div>'
            f'<div><h3>{title}</h3><p>{text}</p><div class="chips">{ch}</div></div>'
            f'<div>{art}</div>{extra}</div>')


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


def build() -> str:
    days, total_commits = git_days()
    tc = triage_counts()
    triage_total = sum(tc.values())
    shelf = lift_svg(ROOT / "backstage/index.html", '<svg viewBox="0 0 1200 430"')
    routing = lift_svg(ROOT / "backstage/index.html", '<svg viewBox="0 0 1200 600"')
    items, pages, words, nsrc = intake()
    proc_pages = sorted((ROOT / "courses/processo-civil-i").glob("aula-*.html"))
    proc_lessons = len(proc_pages)
    _m = [int(x) for p in proc_pages for x in re.findall(r'≈ *(\d+) *min', p.read_text(encoding='utf-8'))[:1]]
    mins = (min(_m), max(_m))

    pile = "".join(f'<li><span>{esc(SHORT_TITLES.get(t, t))}</span><span>{fmt(n)} pp.</span></li>' for n, t in items[:6])
    rest = nsrc - 6

    s0 = spec("course-map.json · aula-06-citacao", (
        '<dl><dt>syllabus</dt><dd>Comunicação dos atos. Intimação. Citação. Processo Eletrônico. Cartas…</dd>'
        '<dt>reader_task</dt><dd>Ler AR, edital, mandado e certidão de nota de expediente e identificar o ato de comunicação registrado.</dd>'
        '<dt>week</dt><dd>7</dd><dt>exam</dt><dd>P1</dd></dl>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/course-map.md")
    s1 = spec(f"shelf.csv · one row of {nsrc}", (
        '<dl><dt>source_id</dt><dd>didier-curso-vol1-2017</dd><dt>role</dt><dd>book_base</dd>'
        '<dt>title</dt><dd>Didier Jr., Curso de direito processual civil, vol. 1, 19ª ed. (2017)</dd>'
        '<dt>sha256</dt><dd>4afef9ce79a…</dd><dt>text</dt><dd>text layer</dd></dl>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/shelf.csv")
    s2 = spec("chapters/didier-curso-vol1-2017/ch17", (
        '<div><span class="dim">index.json · ch17 · Citação · PDF 681–698 · printed 683–700 · 7,399 words</span>\n\n'
        '<span class="hl">===== p. 684 (PDF 682) =====</span>\n  CAPÍTULO 17 · Citação\n  Sumário · 1. Generalidades – 2. A citação como “pressuposto processual” …</div>'))
    s3 = spec(f"triage.csv · one decision of {fmt(triage_total)}", (
        '<dl><dt>chapter</dt><dd>didier-curso-vol1-2017 · ch17</dd><dt>lesson</dt><dd>aula-06-citacao</dd>'
        '<dt>role</dt><dd><span class="limit">primary</span></dd>'
        '<dt>why</dt><dd class="q">Didier’s bounded chapter on citação supplies the essential-book doctrine for identifying the summons; the Moodle models are the assigned documents this lesson teaches readers to interpret.</dd></dl>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/triage.csv")
    s4 = spec("compendium/aula-06-citacao/", (
        '<ul class="files">'
        '<li><span>00-index.md</span><span>provenance</span></li>'
        '<li><span>10-slides.txt</span><span>slides</span></li>'
        '<li><span class="pr">20-primary-001-didier…-ch17.txt</span><span>PDF 681–698</span></li>'
        '<li><span class="pr">20-primary-002…006 · five Moodle records</span><span>whole</span></li>'
        '<li><span class="su">30-supporting-001…029 · CPC arts. 238–275</span><span>by article</span></li>'
        '<li><span class="su">30-supporting-030…036 · doctrine, exports</span><span>bounded</span></li>'
        '<li><span>40-background-001…003</span><span>pages named</span></li>'
        '<li><span>50-exercises-and-exams.txt</span><span>P1 2015 Q11</span></li></ul>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-06-citacao/00-index.md")
    s5 = spec("blueprint.md · A1 reader brief", (
        '<div class="q"><span class="n">Can do after reading</span> <span class="dim">(tasks a question could ask, not topics)</span>\n'
        '1. Read an AR, edital, mandado or Nota de Expediente certificate and name the communication act recorded.\n'
        '2. Separate a completed citation from a failed attempt, and identify which sentence in the record supports that reading.</div>'
        '<div style="margin-top:10px">Source ratio: 73,495 compendium words : 4,000 target words = <span class="hl">18.4 : 1</span></div>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-06-citacao/blueprint.md")
    s6 = (spec("panel.md · aula-13 · first round",
               '<span class="v rev">REVISE</span><div class="q">The section architecture and source ledger are strong, but the chosen real case cannot carry the proposed CPC/2015 route as written.</div>',
               BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-13/panel.md")
          + '<div style="height:16px"></div>'
          + spec("panel.md · aula-06-citacao · second round",
                 '<span class="v ok">APPROVED</span><div class="q">Figures 1, 2 and 4 use the actual records as inspectable objects.</div>',
                 BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-06-citacao/panel.md"))
    s7 = ('<a class="thumb" href="courses/direito-latino-americano/aula-05.html"><img src="assets/gallery/chapter.jpg" alt="A step of the Gelman lesson: the map of four amnesties with Argentina marked, beside the paragraph that explains its grade" width="1400" height="750" loading="lazy"></a>')
    s8 = ('<a class="thumb" href="specimen/casa.html"><img src="backstage/thumbs/casa.jpg" alt="The house style specimen: marks, source blocks and figures on one page" width="720" height="450" loading="lazy"></a>')

    checks = (
        '<table class="checks"><thead><tr><th>Script</th><th>Holds the page back when</th><th>Runs</th></tr></thead><tbody>'
        '<tr><td>quote_check</td><td>a quotation cannot be found in the source texts</td><td>before the pull request</td></tr>'
        '<tr><td>slop_lint</td><td>the prose pads with hedge stacks, staged objections or ritual conclusions (32 rules)</td><td>while writing, and before the pull request</td></tr>'
        '<tr><td>house_check</td><td>the page lacks the shared marks, source blocks or figures</td><td>before the pull request</td></tr>'
        '<tr><td>marks_lint</td><td>a mark is overused, or plain bold stands where a mark belongs</td><td>before the pull request</td></tr>'
        '<tr><td>breakscan</td><td>text clips or overflows at 1,280 pixels</td><td>at Claude’s reading</td></tr>'
        '<tr><td>check_all</td><td>a course front fails to regenerate byte for byte, or a link breaks</td><td>CI, on every push</td></tr>'
        '<tr><td>offline build</td><td>the offline copy of the site differs from the published files</td><td>CI, on every push</td></tr>'
        '</tbody></table>')

    steps = "".join([
        stage("01", "Sol · high", "The syllabus is read in its own order",
              "Each topic becomes a lesson, with one line on what the student must be able to do afterwards and links to the earlier lessons it builds on.",
              [("Claude reads the map", "gt")], s0),
        stage("02", "Luna · high", "Every source is catalogued",
              "Each book, slide deck, decision and exam gets a row with its edition, its file and a SHA-256 fingerprint of that file. A book that never arrives stays listed as missing, and nothing from memory stands in for it.",
              [(f"{nsrc} sources", "c"), ("local OCR for scans", "")], s1),
        stage("03", "Luna · high", "Books are cut into chapters",
              "Each book is cut along its own table of contents, and every page keeps its printed number. A script then confirms that no page is missing or counted twice.",
              [("1,283 chapters", "c"), ("pipeline_check s2", "")], s2),
        stage("04", "Luna · xhigh", "Each chapter is matched to the lessons it serves",
              "Every chapter is weighed against every lesson, and each decision is written down with its reason, rejections included.",
              [(f"{fmt(triage_total)} decisions", "c"), ("pipeline_check s3", "")], s3,
              extra=(f'<div class="wide"><div class="bp"><div class="cap"><span>Processo Civil I · which chapter feeds which lesson</span>'
                     f'<span><span class="n">{fmt(tc["primary"])}</span> primary · {fmt(tc["supporting"])} supporting · {fmt(tc["unused"])} set aside</span></div>{routing}</div></div>')),
        stage("05", "script", "Each lesson's material goes into one folder",
              "A script copies the chosen chapters, statute articles and exam questions into the lesson's folder and writes an index tracing every file to its page.",
              [("84 folders", "c"), ("pull_source.py", "")], s4),
        stage("06", "Luna · max", "The lesson is planned before it is written",
              "The plan names the tasks a student can do after reading, the exam traps, each section with its source pages, and each figure with the claim it carries.",
              [("36 plans", "c")], s5),
        stage("07", "Sol · high", "A second reader checks the plan",
              "A different model reads the plan against the syllabus and the exam questions. It approves the plan or returns it with at most five numbered objections, and a plan returned twice goes to Claude.",
              [("30 reviews", "c"), ("7-point rubric", "")], s6),
        stage("08", "Luna · xhigh", "Text and figures are written together",
              "One writer drafts the prose and draws the figures in a single sitting, from the plan. As the student reads, the figure beside the text moves to the case the paragraph is about.",
              [("Claude reads the page", "gt")], s7),
        stage("09", "Luna · xhigh", "Every page gets the same finish",
              "Marks, source blocks and type are shared across the site. <span class=\"held\">Blue marks what a court decided</span> and <span class=\"limit\">orange marks where a rule stops</span>, on every page.",
              [("casa.css", "")], s8),
        stage("10", "CI", "Scripts read the page before it goes live",
              "A pull request waits until every script below passes, and the main branch is the live site.",
              [("Claude merges", "gt")], "", extra=f'<div class="wide">{checks}</div>'),
    ])

    commits = commits_svg(days)
    first = days[0][0]

    return f'''<!doctype html>
<html lang="en">
<head>
<script>(function(){{var k='ordenacoes-theme',r=document.documentElement;try{{if(localStorage.getItem(k)==='dark')r.dataset.theme='dark'}}catch(e){{}}document.addEventListener('DOMContentLoaded',function(){{var b=document.querySelector('.theme-toggle');if(!b)return;function sync(){{b.setAttribute('aria-pressed',r.dataset.theme==='dark')}}sync();b.addEventListener('click',function(){{var d=r.dataset.theme!=='dark';if(d)r.dataset.theme='dark';else delete r.dataset.theme;try{{localStorage.setItem(k,d?'dark':'light')}}catch(e){{}}sync()}})}})}})()</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Benecles.dev</title>
<meta name="description" content="Benecles.dev builds study websites from the material a course already has: books, slides, decisions, statutes and past exams, published as short lessons with drawn figures and checked quotations. Built with Claude.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Benecles.dev">
<meta property="og:title" content="Benecles.dev">
<meta property="og:description" content="A course's books, slides and exams, turned into one study website. Built with Claude.">
<meta property="og:url" content="https://benecles.dev/">
<meta property="og:image" content="https://benecles.dev/assets/benecles-og.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico">
<link rel="stylesheet" href="assets/benecles.css">
</head>
<body>
<header class="top"><a class="mark" href="./">Benecles.dev</a>
<nav aria-label="Sections"><a class="opt" href="#make">What a course contains</a><a class="opt" href="#for">Who it is for</a><a class="opt" href="#made">How it is made</a><a class="opt" href="#work">How we work</a><a href="#prior">Prior work</a><a href="{GH}">GitHub ↗</a>
<button class="theme-toggle" type="button" aria-pressed="false" title="Night mode"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="sr">Night mode</span></button></nav></header>

<main class="wrap">
<div class="lead"><h1>Benecles.dev builds study websites from the material a course already has.</h1>
<p>We take the books, slide decks, court decisions, statutes and past exams a course uses and publish them as one website of short lessons. Each lesson covers one topic of the syllabus, carries figures drawn for it, and quotes a source only after a script has found the quoted words in it. Professors, universities, companies and tutoring schools send us their material, and their students or staff get the site.</p></div>
<div class="hero2">
<figure class="pile"><header><span>Processo Civil I · UFRGS · what the syllabus assigns</span></header>
<ul>{pile}<li class="more"><span>+ {rest} more: assigned articles, the CPC by article, Moodle case records, past exams</span><span></span></li></ul>
<footer><span>{nsrc} sources</span><span>{fmt(pages)} pages</span></footer></figure>
<figure class="page"><header><span>What a student opens · aula 06 of {proc_lessons}</span><a href="courses/processo-civil-i/aula-06-citacao.html">open ↗</a></header>
<a href="courses/processo-civil-i/aula-06-citacao.html"><img src="assets/lesson-aula06.png" alt="The opening of the lesson Citação e intimação: title, the lesson's one-sentence summary, and a timeline of the civil procedure with this lesson's step marked" width="1280" height="860"></a>
<footer><span>{proc_lessons} lessons published</span><span>≈ 23 minutes to read</span></footer></figure>
</div>
<p class="deck">Processo Civil I at UFRGS assigns {fmt(pages)} pages across {nsrc} sources. Its students read the same material as {proc_lessons} lessons of {mins[0]} to {mins[1]} minutes each.</p>
<div class="cta"><a class="btn" href="#made">How it is made ↓</a><a class="btn ghost" href="mailto:benecles@benecles.dev">benecles@benecles.dev</a></div>

<section id="make">
<p class="kick">01 <i>What a course contains</i></p>
<h2>Taken from the courses already published</h2>
<div class="gal">
<a class="g g-map" href="courses/direito-latino-americano/index.html"><img src="assets/gallery/map.jpg" alt="Map of South America with five courts and numbered routes between their decisions" width="1252" height="1208" loading="lazy"><span><span class="gk">Maps</span>Five courts on one map, each route a lesson where one court answered another.</span></a>
<a class="g g-plan" href="courses/controle-de-constitucionalidade/index.html"><img src="assets/gallery/planta.jpg" alt="The semester plan of Controle de Constitucionalidade: every lesson placed as a piece of one drawing" width="1600" height="1353" loading="lazy"><span><span class="gk">Course indexes</span>The semester drawn as one plan. Each piece opens its lesson.</span></a>
<a class="g g-reg" href="courses/processo-civil-i/index.html"><img src="assets/gallery/register.jpg" alt="The class register of Processo Civil I: numbered lessons, each with its task and reading time" width="1600" height="1067" loading="lazy"><span><span class="gk">The register</span>Every lesson in syllabus order, with the task it trains and its reading time.</span></a>
<a class="g g-cal" href="specimen/instrumentos.html"><img src="assets/gallery/calendar.jpg" alt="April 2015 calendar with fifteen working days counted from the 6th to the 27th, holidays hatched" width="1600" height="905" loading="lazy"><span><span class="gk">Instruments</span>A 15-day deadline counted on the April 2015 calendar, holidays skipped.</span></a>
<a class="g g-bal" href="specimen/instrumentos.html"><img src="assets/gallery/balance.jpg" alt="Article 373 of the CPC drawn as a balance: the plaintiff's fact on one pan, the defendant's facts on the other" width="1600" height="1141" loading="lazy"><span><span class="gk">Instruments</span>Art. 373 as a balance, with each party's facts on its own pan.</span></a>
<a class="g g-seat" href="specimen/instrumentos.html"><img src="assets/gallery/seating.jpg" alt="A two-by-two chart of joinder types with the parties of an exam question seated in their cells" width="1600" height="890" loading="lazy"><span><span class="gk">Instruments</span>The parties of a 2015 exam question seated in the joinder chart.</span></a>
<a class="g g-atlas" href="courses/direito-latino-americano/aula-01.html"><img src="assets/gallery/atlas.jpg" alt="The Americas in 1808, Spanish and Portuguese territories shaded, with a timeline from 1791 to 1824" width="1070" height="1070" loading="lazy"><span><span class="gk">Maps</span>The Americas in 1808, on a timeline that runs to 1824.</span></a>
<a class="g g-fonte" href="courses/direito-latino-americano/aula-05.html"><img src="assets/gallery/fonte.jpg" alt="A source block quoting the Inter-American Court in Spanish, with its reference in the header and a translation toggle" width="1600" height="237" loading="lazy"><span><span class="gk">Source blocks</span>The court's own words in its own language, the reference in the header, a translation one click away.</span></a>
</div>
</section>

<section id="for">
<p class="kick">02 <i>Who it is for</i></p>
<h2>Professors, universities, companies and tutoring schools</h2>
<div class="clients">
<div><span class="k">A professor</span><p>Your books, slide decks and assigned decisions become one site your students browse by class. A quotation from your book carries the book's page in its header.</p></div>
<div><span class="k">A university</span><p>Every course in a curriculum follows the same lesson format, figures and sourcing, so a student who has read one course knows how to read the next.</p></div>
<div><span class="k">A company</span><p>Contracts, reports, regulations and case files become one compendium, cut into parts, filed under the questions they answer and traceable to the page.</p></div>
<div><span class="k">A tutoring school</span><p>Your syllabus and your students' past exams become a course whose lessons close with the exam's own questions.</p></div>
</div>
</section>

<section id="made">
<p class="kick">03 <i>How it is made</i></p>
<h2>From a reading list to a published lesson</h2>
<p class="intro">The specimens beside each step come from one lesson, Processo Civil I, Aula 06, on <i>citação</i> and <i>intimação</i>, the court acts that tell a party it is being sued and keep it informed of each step that follows.</p>
<div class="stages">{steps}</div>
<div class="two">
<div><div class="bp" style="margin:0"><div class="cap"><span>slop_lint, measured on human legal writing</span><span><span class="n">0.5</span> cap</span></div>{slop_svg()}</div>
<p class="note">In 368 texts of human legal doctrine, negated inference (phrases like “não basta”) ran at 0.14 per thousand words; on 170 of our pages it ran at 2.43. The rule now caps it at 0.5, and every other rule in slop_lint has its limit where no more than one human text in ten would be flagged. <a href="{BLOB}workshop/work/slop-bench/BACKTEST.md">Method and numbers</a>.</p></div>
<div><p class="note" style="margin-top:0">A script is trusted only after it has held back a page known to be bad.</p></div>
</div>
</section>

<section id="work">
<p class="kick">04 <i>How we work</i></p>
<h2>Who does what, and how mistakes stay fixed</h2>
<div class="roles">
<div><span class="k">Direction</span><h3>Benecles</h3><p>Chooses the courses, sets the priorities and decides what gets cut. The open decisions listed in CEO.md are his.</p></div>
<div><span class="k">Editor and designer</span><h3>Claude</h3><p>Writes the brief for each step, owns the writing standard and the design system, draws figures, rebuilds reference lessons by hand and signs off every step. Anthropic’s model, working through Claude Code.</p></div>
<div><span class="k">Volume</span><h3>Codex</h3><p>An orchestrator splits each brief into units of six or fewer and runs up to sixteen workers at once, Sol for the course map and the review and Luna for the other steps. OpenAI’s models.</p></div>
<div><span class="k">Checks</span><h3>Scripts</h3><p>Each step has a script that can hold the work back. The scripts live in the repository beside the pages they read.</p></div>
</div>
<div class="bp"><div class="cap"><span>Who works at each step</span><span>● works · <span class="n">◆</span> signs off · ○ reads</span></div>{relay_svg()}</div>
<div class="two">
<div>{spec("BUGS.md · 53 rows · symptom → cause → fix → check", '<dl><dt>symptom</dt><dd>Prose hugs the left edge of a wide screen (x = 0) while headings sit centred</dd><dt>cause</dt><dd>&lt;div class="prosa"&gt; placed directly in &lt;body&gt;</dd><dt>fix</dt><dd>Wrap in &lt;div class="wide"&gt;</dd><dt>catches it</dt><dd>anatomy_check LOOSE-PROSA, in check_all</dd></dl>', BLOB + "workshop/BUGS.md")}
<div style="height:20px"></div>
{spec("FLIGHT-LOG.md · F-022 of 32", '<dl><dt>found</dt><dd>A fictional “Comunidade C” carried the lesson while real Brazilian material exists</dd><dt>rule</dt><dd class="q">Carriers are real: an article of the CF, a case, a statute.</dd><dt>applies to</dt><dd>S5a, S5</dd></dl>', BLOB + "workshop/FLIGHT-LOG.md")}</div>
<div><p class="note" style="margin-top:0">When a script or a reader catches a fault, two records change. The bug catalogue gains a row naming the check that now catches it, and the flight log gains a numbered rule that every lesson in progress applies before its next step.</p>
{spec("CEO.md · mandate 8", '<div class="q">The CEO’s job is the WHAT: take the chairman’s thin idea and develop it to the fullest (what it is, what it looks like, where it sits, how it behaves, what it must never do, how it fits the house and its ethos), then hand that to the orchestrator as a master brief. The HOW is the orchestrator’s.</div>', BLOB + "workshop/CEO.md")}
<p class="note">A new Claude session reads CEO.md first and continues from where the previous session stopped.</p></div>
</div>
<div class="plate"><div class="cap"><span>Commits per day since {first.day} {first:%B} · {fmt(total_commits)} in all</span><span>■ site · <span class="sw">■</span> workshop</span></div>{commits}</div>
<p class="note"><span class="k">Standards and logs</span> <a href="{BLOB}workshop/protocols/Source%20Pipeline.md">Source Pipeline</a> · <a href="{BLOB}workshop/protocols/Writing%20Standard.md">Writing Standard</a> · <a href="{BLOB}workshop/protocols/House%20Manual.md">House Manual</a> · <a href="{BLOB}workshop/protocols/Visual%20Genres.md">Visual Genres</a> · <a href="{BLOB}workshop/CEO.md">CEO.md</a> · <a href="{BLOB}workshop/FLIGHT-LOG.md">Flight log</a> · <a href="{BLOB}workshop/BUGS.md">Bugs</a></p>
</section>

<section id="prior">
<p class="kick">05 <i>Prior work</i></p>
<h2>Ordenações Filipinas, law courses for UFRGS</h2>
<a class="prod" href="ordenacoes-filipinas/"><div class="img"><img src="assets/og.png" alt="The Ordenações Filipinas course shelf" width="1200" height="630" loading="lazy"></div>
<div class="body"><span class="k">UFRGS · 2026/2 · in Portuguese</span><h3>Ordenações Filipinas</h3><p>Seven law courses, from constitutional review to civil procedure. Law students at UFRGS and USP study with it.</p>
<div class="reg"><div><span>Courses</span><span class="n">7</span></div><div><span>Lessons</span><span class="n">149</span></div><div><span>Figures</span><span class="n">919</span></div></div><span class="go">Open the courses →</span></div></a>
<div class="bp"><div class="cap"><span>Every lesson in Ordenações Filipinas, one spine each</span></div>{shelf}</div>
</section>

<footer class="foot"><span>Benecles.dev · <a href="mailto:benecles@benecles.dev">benecles@benecles.dev</a></span><span><a href="{GH}">GitHub ↗</a><span>Built with Claude</span></span></footer>
</main>
</body>
</html>
'''


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
