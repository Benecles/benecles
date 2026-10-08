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
    return svg.replace('href="../', 'href="')


# ---------------------------------------------------------------- figures

STATIONS = [
    ("S0", "Course map", "Sol · high", "check s0"),
    ("S1", "Shelf", "Luna · high", "sha-256"),
    ("S2", "Split", "Luna · high", "check s2"),
    ("S3", "Triage", "Luna · xhigh", "check s3"),
    ("S4", "Compendium", "script", "index"),
    ("S5", "Blueprint", "Luna · max", "template"),
    ("S5a", "Panel", "Sol · high", "verdict"),
    ("S5b", "Write + draw", "Luna · xhigh", "quote_check"),
    ("S5c", "House pass", "Luna · xhigh", "house_check"),
    ("Ship", "Pull request", "CI", "check_all"),
]


def line_svg() -> str:
    w, x0, step, y = 1180, 58, 118, 62
    o = [f'<svg viewBox="0 0 {w} 150" role="img" aria-label="The Benecles line: ten stations from course map to pull request, with a gate after each">']
    o.append('<style>.pl-c{font:600 13px var(--mono);fill:var(--ink)}.pl-n{font:700 15px var(--sans);fill:var(--ink)}'
             '.pl-m{font:500 11px var(--mono);fill:var(--dif)}.pl-k{font:500 10.5px var(--mono);fill:var(--muted)}'
             '.pl-g{font:500 10px var(--mono);letter-spacing:.08em;fill:var(--conc)}</style>')
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
        o.append(f'<text class="rg-a" x="0" y="{cy+4}">{esc(a)}</text>')
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
    o.append('<style>.cm-k{font:500 10.5px var(--mono);letter-spacing:.06em;fill:var(--ink-2)}.cm-v{font:600 11px var(--mono);fill:var(--ink)}</style>')
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
        o.append(f'<text class="sl-k" x="0" y="{y}">{esc(label)}</text>')
        o.append(f'<rect x="0" y="{y+10}" width="{max(v*sc,3):.1f}" height="26" style="fill:var(--{tone})"/>')
        o.append(f'<text class="sl-v" x="{max(v*sc,3)+10:.1f}" y="{y+31}">{v:.2f}</text>')
    o.append(f'<text class="sl-k" x="0" y="{h-6}">PER 1,000 WORDS · “NÃO BASTA”, “NÃO SUBSTITUI”, “NÃO RESOLVE”…</text>')
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


def build() -> str:
    days, total_commits = git_days()
    tc = triage_counts()
    triage_total = sum(tc.values())
    shelf = lift_svg(ROOT / "backstage/index.html", '<svg viewBox="0 0 1200 430"')
    routing = lift_svg(ROOT / "backstage/index.html", '<svg viewBox="0 0 1200 600"')

    s0 = spec("course-map.json · aula-06-citacao", (
        '<dl><dt>syllabus</dt><dd>Comunicação dos atos. Intimação. Citação. Processo Eletrônico. Cartas…</dd>'
        '<dt>reader_task</dt><dd>Ler AR, edital, mandado e certidão de nota de expediente e identificar o ato de comunicação registrado.</dd>'
        '<dt>week</dt><dd>7</dd><dt>exam</dt><dd>P1</dd></dl>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/course-map.md")
    s1 = spec("shelf.csv · one row of forty", (
        '<dl><dt>source_id</dt><dd>didier-curso-vol1-2017</dd><dt>role</dt><dd>book_base</dd>'
        '<dt>title</dt><dd>Didier Jr., Curso de direito processual civil, vol. 1, 19ª ed. (2017)</dd>'
        '<dt>sha256</dt><dd>4afef9ce79a…</dd><dt>text</dt><dd>text layer</dd></dl>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/shelf.csv")
    s2 = spec("chapters/didier-curso-vol1-2017/ch17", (
        '<div><span class="dim">index.json · ch17 · Citação · PDF 681–698 · printed 683–700 · 7,399 words</span>\n\n'
        '<span class="hl">===== p. 684 (PDF 682) =====</span>\n  CAPÍTULO 17 · Citação\n  Sumário · 1. Generalidades – 2. A citação como “pressuposto processual” …</div>'))
    s3 = spec("triage.csv · one verdict of 28,285", (
        '<dl><dt>chapter</dt><dd>didier-curso-vol1-2017 · ch17</dd><dt>lesson</dt><dd>aula-06-citacao</dd>'
        '<dt>role</dt><dd><b class="limit">primary</b></dd>'
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
    s5 = spec("blueprint.md · A1 Reader brief", (
        '<div class="q"><b>Can do after reading</b> <span class="dim">(tasks a question could ask, not topics)</span>\n'
        '1. Read an AR, edital, mandado or Nota de Expediente certificate and name the communication act recorded.\n'
        '2. Separate a completed citation from a failed attempt, and identify which sentence in the record supports that reading.</div>'
        '<div style="margin-top:10px">Source ratio: 73,495 compendium words : 4,000 target words = <span class="hl">18.4 : 1</span></div>'),
        BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-06-citacao/blueprint.md")
    s5a = (spec("panel.md · aula-13 · first round",
                '<span class="v rev">REVISE</span><div class="q">The section architecture and source ledger are strong, but the chosen real case cannot carry the proposed CPC/2015 route as written.</div>',
                BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-13/panel.md")
           + '<div style="height:16px"></div>'
           + spec("panel.md · aula-06-citacao · second round",
                  '<span class="v ok">APPROVED</span><div class="q">Figures 1, 2 and 4 use the actual records as inspectable objects.</div>',
                  BLOB + "workshop/work/pipeline/processo-civil-i/compendium/aula-06-citacao/panel.md"))
    s5b = ('<a class="thumb" href="specimen/instrumentos.html"><img src="backstage/thumbs/instrumentos.jpg" alt="Specimen of the Processo instruments: a deadline counted on the April 2015 calendar" width="720" height="450" loading="lazy"></a>')
    s5c = ('<a class="thumb" href="specimen/casa.html"><img src="backstage/thumbs/casa.jpg" alt="The house style specimen: marks, source blocks and figures on one page" width="720" height="450" loading="lazy"></a>')
    ship = spec("ISSUES.md · one line per merge", (
        '<div>- <b>Custom domain</b> · site moves to https://benecles.dev (repo renamed to `benecles`; `CNAME` added …) · `curl -I https://benecles.dev` 200\n\n'
        '<span class="dim">$ sh tools/check_all.sh</span>\nteoria-geral-dos-contratos: 17 lesson links checked\n<span class="held">check_all: PASS</span></div>'),
        BLOB + "ISSUES.md")

    stages = "".join([
        stage("S0", "Sol · high", "What the course is",
              "The syllabus is read in its own order and turned into lessons. Each lesson gets one line on what the reader must be able to do afterwards, and the earlier lessons it depends on.",
              [("pipeline_check s0", ""), ("◆ Claude reads the map", "g")], s0),
        stage("S1", "Luna · high", "What we have",
              "Every source becomes a row: role, path, format, text status and a hash of the file. A missing book is recorded as missing; a gap is never filled from a summary or from model memory. Scans are read by local OCR only. <b>177 sources</b> across four courses.",
              [("sha-256", ""), ("local OCR", ""), ("◆ gate", "g")], s1),
        stage("S2", "Luna · high", "Books into chapters",
              "Each book is cut at its own table of contents, one file per chapter, every page marked with its printed and PDF number. Chapters are the unit; nothing is cut by keyword. <b>3,355 chapters</b> so far.",
              [("pipeline_check s2", ""), ("no gaps, no overlaps", ""), ("◆ gate", "g")], s2),
        stage("S3", "Luna · xhigh", "Which chapter feeds which lesson",
              f"Every chapter is judged against every lesson it might serve, and every verdict carries a reason, the rejections included. A lesson also inherits the primary chapters of the lessons it depends on. For Processo Civil I that is <b>{fmt(triage_total)} verdicts</b>.",
              [("pipeline_check s3", ""), ("dependency closure", ""), ("◆ gate", "g")], s3,
              extra=(f'<div class="wide"><div class="bp"><div class="cap"><span>Processo Civil I · chapter → lesson</span>'
                     f'<span><b>{fmt(tc["primary"])}</b> primary · {fmt(tc["supporting"])} supporting · {fmt(tc["background"])} background · {fmt(tc["unused"])} set aside, each with a reason</span></div>{routing}</div></div>')),
        stage("S4", "script", "One workbench per lesson",
              "A script stitches each lesson's material into ordered files, every file traced to its source, chapter, pages, role and hash. No model judgment happens here. <b>84 workbenches</b>.",
              [("pull_source.py", ""), ("provenance table", "")], s4),
        stage("S5", "Luna · max", "Plan before writing",
              "One agent owns the lesson's text and every figure on it. It starts with a blueprint: what the reader can do afterwards, the exam traps, the sections with their source pages, and each figure with the claim it carries. <b>36 blueprints</b>.",
              [("lesson template", ""), ("reference blueprint", "")], s5),
        stage("S5a", "Sol · high", "A committee reads the plan",
              "A different model judges the blueprint the way a thesis committee judges a proposal. It reads the plan, the course map, the workbench index and the exam questions, never the chapters, and answers APPROVED or REVISE with at most five numbered points. A second REVISE goes to Claude. <b>30 reviews</b>.",
              [("7-point rubric", ""), ("escalates to Claude", "g")], s5a),
        stage("S5b", "Luna · xhigh", "Text and figures in one pass",
              "The writer follows the blueprint, prose and figures together in one context. Figures are instruments the reader works with: the deadline counted on the real calendar of April 2015, the parties seated around one table, the burden of proof as a balance.",
              [("quote_check", ""), ("slop_gate", ""), ("◆ Claude reads the page", "g")], s5b),
        stage("S5c", "Luna · xhigh", "The house layer",
              "Every page gets the shared marks and source blocks: <span class=\"held\">blue for what a court decided</span>, <span class=\"limit\">orange for where a rule stops</span>, quotations set in source blocks with the reference in the header.",
              [("house_check", ""), ("marks_lint", ""), ("◆ gate", "g")], s5c),
        stage("Ship", "CI", "One change, one pull request",
              "Each change is its own branch and pull request, with a line in the issue log. CI regenerates the course fronts and fails unless they come out byte-identical, and the offline manifest must match the tree. <b>main</b> is the live site.",
              [("check_all", ""), ("offline build", ""), ("◆ Claude merges", "g")], ship),
    ])

    commits = commits_svg(days)
    first = days[0][0]

    return f'''<!doctype html>
<html lang="en">
<head>
<script>(function(){{var k='ordenacoes-theme',r=document.documentElement;try{{if(localStorage.getItem(k)==='dark')r.dataset.theme='dark'}}catch(e){{}}document.addEventListener('DOMContentLoaded',function(){{var b=document.querySelector('.theme-toggle');if(!b)return;function sync(){{b.setAttribute('aria-pressed',r.dataset.theme==='dark')}}sync();b.addEventListener('click',function(){{var d=r.dataset.theme!=='dark';if(d)r.dataset.theme='dark';else delete r.dataset.theme;try{{localStorage.setItem(k,d?'dark':'light')}}catch(e){{}}sync()}})}})}})()</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Benecles · we compile courses</title>
<meta name="description" content="Benecles compiles textbooks, slides and case law into source-checked courses. Ten stations, a gate after each, built with Claude. First output: seven law courses.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Benecles">
<meta property="og:title" content="Benecles · we compile courses">
<meta property="og:description" content="Sources in, checked courses out. Ten stations, a gate after each, built with Claude.">
<meta property="og:url" content="https://benecles.dev/">
<meta property="og:image" content="https://benecles.dev/assets/benecles-og.png">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="640">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico">
<link rel="stylesheet" href="assets/benecles.css">
</head>
<body>
<header class="top"><a class="mark" href="./">Benecles</a>
<nav aria-label="Sections"><a class="opt" href="#sell">What we sell</a><a class="opt" href="#line">The line</a><a class="opt" href="#checks">Checks</a><a class="opt" href="#claude">Claude</a><a href="#products">Products</a><a class="gh" href="{GH}">{GH_MARK}GitHub</a>
<button class="theme-toggle" type="button" aria-pressed="false" title="Night mode"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="sr">Night mode</span></button></nav></header>

<main class="wrap">
<div class="hero">
<h1 class="mast">Benecles</h1>
<p class="lede">We compile courses. Give us a syllabus and the books, slides, decisions and past exams it assigns; we return lessons a student finishes in one sitting, with figures drawn for each lesson and <b>every quotation checked against the page it came from</b>.</p>
<div class="cta"><a class="btn" href="ordenacoes-filipinas/">Open the first course →</a><a class="btn ghost" href="{GH}">{'Read the source'}</a></div>
<div class="reg" aria-label="Output so far"><div><span>Courses</span><b>7</b></div><div><span>Lessons</span><b>149</b></div><div><span>Words</span><b>1.15M</b></div><div><span>Figures</span><b>919</b></div><div><span>Chapters split</span><b>3,355</b></div><div><span>Triage verdicts</span><b>{fmt(triage_total)}</b></div></div>
<div class="bp"><div class="cap"><span>Output so far · one spine per lesson</span></div>{shelf}</div>
</div>

<section id="sell">
<p class="kick">01 <i>What we sell</i></p>
<h2>The course is the output. The compiler is the product.</h2>
<p class="intro">Ordenações Filipinas, seven law courses for the 2026/2 semester at UFRGS, is the first thing the compiler built. What we offer is the run itself: <b>the same stations, standards and checks, pointed at a new syllabus</b>.</p>
<div class="trade">
<div><span class="k">In</span><ul><li>The syllabus, in its own order</li><li>The books, slide decks, decisions and statutes it assigns</li><li>Past exams and exercise lists</li></ul></div>
<div class="out"><span class="k">Out</span><ul><li>One lesson per syllabus topic, 15 to 25 minutes each</li><li>Figures drawn as instruments: a deadline on the real calendar, a statute as a balance</li><li>Every quotation found in its source, by page</li><li>Each exam trap placed once and tested once</li><li>A static site that reads offline and needs no server</li><li>The ledger of which chapter fed which lesson, and why</li></ul></div>
</div>
</section>

<section id="line">
<p class="kick">02 <i>The line</i></p>
<h2>Ten stations, a gate after each.</h2>
<p class="intro">The order is fixed: understand the course, prepare the material, then write. No station starts until the one before it passes its check. Below, one real lesson goes down the line: <b>Processo Civil I, Aula 06, on citação and intimação</b>, the formal notices that bring a party into a lawsuit.</p>
<div class="bp"><div class="cap"><span>The line · models per station · the check that can stop it</span><span><b>◆</b> Claude's gate</span></div>{line_svg()}</div>
<div class="stages">{stages}</div>
</section>

<section id="checks">
<p class="kick">03 <i>Checks</i></p>
<h2>What ships is what passes.</h2>
<p class="intro">Models write; scripts decide. A check counts only after it has failed on a page we knew was bad.</p>
<table class="checks"><thead><tr><th>Check</th><th>Fails when</th><th>Where it runs</th></tr></thead><tbody>
<tr><td>quote_check</td><td>a quotation on the page cannot be found in the source texts</td><td>house pass (S5c), before the PR</td></tr>
<tr><td>slop_lint</td><td>the prose pads: hedge stacks, staged objections, ritual conclusions, our own tics (32 rules)</td><td>writer and house pass · backtested on 368 human doctrine texts</td></tr>
<tr><td>house_check</td><td>a page is missing the house layer</td><td>house pass (S5c), before the PR</td></tr>
<tr><td>marks_lint</td><td>marks lose their meaning: too many per chapter, plain bold where a mark belongs</td><td>house pass · 8 tests</td></tr>
<tr><td>anatomy_check</td><td>prose sits off the grid, panels arrive late, figure squares are uncropped</td><td>CI, every push</td></tr>
<tr><td>breakscan</td><td>text clips or overflows at 1,280 or 375 pixels</td><td>Playwright, at Claude’s gate</td></tr>
<tr><td>check_all</td><td>a course front does not regenerate byte-identical, or a lesson link breaks</td><td>CI, every push</td></tr>
<tr><td>offline build</td><td>the committed tree differs from what the offline builder produces</td><td>CI, every push</td></tr>
</tbody></table>
<div class="two">
<div><div class="bp" style="margin:0"><div class="cap"><span>The prose backtest</span><span><b>18×</b> the human rate</span></div>{slop_svg()}</div>
<p class="note">The backtest found our own habit. Pages used “não basta”, “não substitui” and their kin at 2.43 per thousand words, about eighteen times the rate in human legal doctrine. <b>It became a rule</b>, with its limit set where no more than one human text in ten would trip it. <a href="{BLOB}workshop/work/slop-bench/BACKTEST.md">Method and numbers</a>.</p></div>
<div>{spec("BUGS.md · 53 rows · symptom → cause → fix → check", '<dl><dt>symptom</dt><dd>Prose hugs the left edge of a wide screen (x = 0) while headings sit centred</dd><dt>cause</dt><dd>&lt;div class="prosa"&gt; placed directly in &lt;body&gt;</dd><dt>fix</dt><dd>Wrap in &lt;div class="wide"&gt;</dd><dt>catches it</dt><dd>anatomy_check LOOSE-PROSA, in check_all</dd></dl>', BLOB + "workshop/BUGS.md")}
<div style="height:20px"></div>
{spec("FLIGHT-LOG.md · F-022 of 32", '<dl><dt>found</dt><dd>A fictional “Comunidade C” carried the lesson while real Brazilian material exists</dd><dt>rule</dt><dd class="q">Carriers are real: an article of the CF, a case, a statute.</dd><dt>applies to</dt><dd>S5a, S5</dd></dl>', BLOB + "workshop/FLIGHT-LOG.md")}
<p class="note">Every fix adds a bug row with the check that now catches it. Every lesson learned at a gate becomes a numbered rule that each station in flight applies before its next step.</p></div>
</div>
</section>

<section id="claude">
<p class="kick">04 <i>Built with Claude</i></p>
<h2>Claude runs the house.</h2>
<p class="intro">The work is done by AI agents with defined jobs, coordinated in the open on GitHub. Benecles sets the direction; <b>Claude turns it into briefs and holds the standard</b>; Codex supplies the volume; scripts decide what passes.</p>
<div class="roles">
<div><span class="k">Direction</span><h3>Benecles</h3><p>Chooses the courses and makes the calls no agent should: what to build, what to cut, what the house stands for.</p></div>
<div><span class="k">Editor and designer</span><h3>Claude</h3><p>Writes every brief: what the thing is, how it must look, what it must never do. Owns the writing standard and the design system, draws figures, rebuilds reference lessons by hand and gates each station. Anthropic, through Claude Code.</p></div>
<div><span class="k">The floor</span><h3>Codex</h3><p>An orchestrator splits each brief into units of six or fewer and runs up to sixteen workers at once: Sol for the course map and the panel, Luna for everything else. OpenAI.</p></div>
<div><span class="k">The gate</span><h3>Scripts</h3><p>Every station has a check that can fail, and nothing merges red. The checks are in the repository, next to the pages they judge.</p></div>
</div>
<div class="bp"><div class="cap"><span>Who works at each station</span><span>● works · <b>◆</b> gates · ○ reads</span></div>{relay_svg()}</div>
<div class="two">
<div>{spec("CEO.md · mandate 8 · the brief", '<div class="q">The CEO’s job is the WHAT: take the chairman’s thin idea and develop it to the fullest (what it is, what it looks like, where it sits, how it behaves, what it must never do, how it fits the house and its ethos), then hand that to the orchestrator as a master brief. The HOW is the orchestrator’s.</div>', BLOB + "workshop/CEO.md")}
<p class="note"><b>CEO.md</b> is Claude's running handoff: a new session reads it and continues where the last one stopped.</p></div>
<div>{spec("Source Pipeline.md · why these models", '<div class="q">Sol costs about 20× Luna per token. […] factual risk is handled by the pipeline, not by the model: writers work from the compendium with page markers, and Claude’s gate spot-checks claims against the cited pages.</div>', BLOB + "workshop/protocols/Source%20Pipeline.md")}
<div style="height:20px"></div>
{spec("GitHub issues · one per station per course", '<span class="lbl l1">blocked</span><span class="lbl l2">needs-gate</span><span class="lbl l3">gate:approved</span><div class="dim" style="margin-top:8px">A station finishes, posts its check and stops. Claude answers on the issue.</div>')}</div>
</div>
</section>

<section id="record">
<p class="kick">05 <i>The record</i></p>
<h2>Every commit since the first page.</h2>
<p class="intro">{fmt(total_commits)} commits since {first.day} {first:%B}: the site and the workshop behind it, merged with their dates intact. The workshop's source texts were taken out of every commit; the ledgers that record them stayed.</p>
<div class="plate"><div class="cap"><span>Commits per day</span><span>■ site · <b style="color:var(--dif)">■</b> workshop</span></div>{commits}</div>
<div class="reg"><div><span>Commits</span><b>{fmt(total_commits)}</b></div><div><span>Pull requests merged</span><b>188</b></div><div><span>Coordination issues</span><b>45</b></div><div><span>Bugs catalogued</span><b>53</b></div><div><span>Flight-log rules</span><b>32</b></div><div><span>Words of standards</span><b>18,929</b></div></div>
<p class="note">Read them: <a href="{BLOB}workshop/protocols/Source%20Pipeline.md">Source Pipeline</a> · <a href="{BLOB}workshop/protocols/Writing%20Standard.md">Writing Standard</a> · <a href="{BLOB}workshop/protocols/House%20Manual.md">House Manual</a> · <a href="{BLOB}workshop/protocols/Visual%20Genres.md">Visual Genres</a> · <a href="{BLOB}workshop/CEO.md">CEO.md</a> · <a href="{BLOB}workshop/FLIGHT-LOG.md">Flight log</a> · <a href="{BLOB}workshop/BUGS.md">Bugs</a></p>
</section>

<section id="products">
<p class="kick">06 <i>Products</i></p>
<h2>One so far.</h2>
<a class="prod" href="ordenacoes-filipinas/"><div class="img"><img src="assets/og.png" alt="The Ordenações Filipinas course shelf" width="1200" height="630" loading="lazy"></div>
<div class="body"><span class="k">Law · UFRGS 2026/2 · in Portuguese</span><h3>Ordenações Filipinas</h3><p>Seven law courses, from constitutional review to civil procedure, compiled from the books and decisions each syllabus assigns.</p>
<div class="reg"><div><span>Courses</span><b>7</b></div><div><span>Pages</span><b>187</b></div><div><span>Figures</span><b>919</b></div></div><span class="go">Open the courses →</span></div></a>
</section>

<footer class="foot"><span>Benecles · <a href="mailto:benecles@benecles.dev">benecles@benecles.dev</a></span><span><a class="gh" href="{GH}">{GH_MARK}GitHub</a><span>Built with Claude</span></span></footer>
</main>
</body>
</html>
'''


if __name__ == "__main__":
    OUT.write_text(build(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
