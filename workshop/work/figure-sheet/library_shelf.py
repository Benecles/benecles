#!/usr/bin/env python3
"""The library on one shelf (backstage hero, CEO 07/10): every lesson on the site as a book spine.
Height = words · a band across the spine = one figure · a pale cap = source blocks (house style in).
Hover shows the title; each spine links to its lesson. Uses the host page's CSS variables.
  python3 library_shelf.py SITE_REPO > shelf.svg   (links are written relative to backstage/)"""
import re, glob, json, os, sys, html, pathlib
SITE = pathlib.Path(sys.argv[1]).expanduser()
COURSES = [('controle-de-constitucionalidade', 'Controle'), ('direito-constitucional-i', 'Constitucional I'), ('teoria-do-delito', 'Delito'),
           ('teoria-geral-dos-contratos', 'Contratos'), ('direito-latino-americano', 'Latam'), ('processo-civil-i', 'Processo'),
           ('metodologia-juridica', 'Metodologia')]
def words(s):
    t = re.sub(r'(?is)<(script|style|svg|head)\b.*?</\1>', ' ', s)
    return len(re.sub(r'<[^>]+>', ' ', t).split())
books = []
for slug, short in COURSES:
    d = SITE / 'courses' / slug
    if slug == 'teoria-do-delito':
        cat = json.load(open(d / 'catalogue.json'))
        for u in cat['units']:
            books.append((short, u['title'], int(u.get('word_count') or 0), 0, 0, f'../courses/{slug}/guia-de-estudo.html#{u["id"]}'))
        continue
    def key(f):
        m = re.match(r'aula-(\d+)(.*)\.html', os.path.basename(f)); return (int(m.group(1)), m.group(2)) if m else (999, f)
    for f in sorted(glob.glob(str(d / 'aula-*.html')), key=key):
        s = open(f, encoding='utf-8').read()
        t = re.search(r'<title>([^<·]+)', s); title = html.unescape(t.group(1).strip()) if t else os.path.basename(f)
        books.append((short, title, words(s), len(re.findall(r'<figure\b', s)), len(re.findall(r'class="fonte', s)), f'../courses/{slug}/{os.path.basename(f)}'))

W, H, X0, BASE = 1200, 430, 30, 360
SPW, GAP, CGAP = 5.3, 1.5, 15
maxw = max(b[2] for b in books)
def h(w): return 30 + 280 * (w / maxw) ** .9
out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Every lesson on the site as a book spine: {len(books)} lessons in {len(COURSES)} courses, height by words">']
out.append('<style>.ls a:hover rect.sp,.ls a:focus rect.sp{fill:var(--ink);fill-opacity:.55}.ls-k{font:500 10px var(--mono);letter-spacing:.08em;text-transform:uppercase;fill:var(--muted)}.ls-c{font:600 11px var(--mono);letter-spacing:.06em;fill:var(--ink)}</style>')
out.append(f'<line x1="{X0 - 10}" y1="{BASE}" x2="{W - 20}" y2="{BASE}" style="stroke:var(--ink);stroke-width:2"/>')
out.append(f'<line x1="{X0 - 10}" y1="{BASE + 7}" x2="{W - 20}" y2="{BASE + 7}" style="stroke:var(--ink);stroke-width:.8;opacity:.5"/>')
x = X0; cur = None; start = X0
out.append('<g class="ls">')
groups = []
for short, title, w, figs, fonte, href in books:
    if short != cur:
        if cur: groups.append((cur, start, x - GAP)); x += CGAP
        cur, start = short, x
    hh = h(w); y = BASE - hh
    tip = html.escape(f'{short} · {title} · {w:,} words' + (f' · {figs} fig.' if figs else ''))
    out.append(f'<a href="{href}"><title>{tip}</title>'
               f'<rect class="sp" x="{x:.1f}" y="{y:.1f}" width="{SPW}" height="{hh:.1f}" style="fill:var(--ink);fill-opacity:.16;stroke:var(--ink);stroke-width:.7;stroke-opacity:.85"/>')
    for k in range(min(figs, 8)):   # one band per figure, from the top down
        by = y + 8 + k * 7
        out.append(f'<line x1="{x:.1f}" y1="{by:.1f}" x2="{x + SPW:.1f}" y2="{by:.1f}" style="stroke:var(--ink);stroke-width:1.6;pointer-events:none"/>')
    if fonte:
        out.append(f'<rect x="{x:.1f}" y="{y - 4:.1f}" width="{SPW}" height="4" style="fill:var(--dif);pointer-events:none"/>')
    out.append('</a>')
    x += SPW + GAP
groups.append((cur, start, x - GAP))
out.append('</g>')
for name, a, b in groups:
    out.append(f'<line x1="{a:.1f}" y1="{BASE + 16}" x2="{b:.1f}" y2="{BASE + 16}" style="stroke:var(--muted);stroke-width:1"/>')
    out.append(f'<text x="{a:.1f}" y="{BASE + 34}" class="ls-c">{name}</text>')
out.append(f'<text x="{W - 20}" y="{BASE + 58}" text-anchor="end" class="ls-k">height = words · band = figure · cap = source blocks</text>')
out.append('</svg>')
print('\n'.join(out))
print(f'<!-- {len(books)} books, x end {x:.0f} -->', file=sys.stderr)
