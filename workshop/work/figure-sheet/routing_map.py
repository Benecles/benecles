#!/usr/bin/env python3
"""The routing map: the Processo triage drawn as threads (backstage hero, CEO 07/10).
Top: the CPC as a ruler of its articles. Middle: the books and documents, one tick per chapter.
Bottom: the 22 lessons in syllabus order. Every 'primary' routing is a thread (blue = statute,
ink = doctrine, orange = Moodle documents and exams); 'supporting' routings are faint texture.
Prints an <svg> that uses the host page's CSS variables (--ink, --dif, --conc, --muted, --grid-major).
  python3 routing_map.py > out.svg"""
import csv, json, glob, pathlib, collections, sys
P = pathlib.Path(__file__).resolve().parents[1] / 'pipeline' / 'processo-civil-i'
rows = list(csv.DictReader(open(P / 'triage.csv')))
cm = json.load(open(P / 'course-map.json'))
lessons = [l['id'] for l in cm['lessons']]
exam_of = {l['id']: (l.get('exam_group') or '') for l in cm['lessons']}

order = {}                                   # (source, chapter_id) -> position within the source
for f in glob.glob(str(P / 'chapters/*/index.json')):
    sid = pathlib.Path(f).parent.name
    for i, c in enumerate(json.load(open(f)).get('chapters', [])):
        cid = c.get('id') or c.get('chapter_id') or c.get('file') or str(i)
        order[(sid, cid)] = i
        order[(sid, pathlib.Path(str(cid)).stem)] = i
counts = collections.Counter(s for (s, _), i in order.items())
counts = {s: max(i for (ss, _), i in order.items() if ss == s) + 1 for s in counts}

CPC = 'cpc-lei-13105-capture-2026-09-28'
SHORT = {'didier-curso-vol1-2017': 'Didier v.1', 'marinoni-novo-curso-vol2': 'Novo Curso v.2', 'marinoni-novo-curso-vol1-2017': 'Novo Curso v.1',
         'mitidiero-processo-civil-2022': 'Mitidiero', 'barbosa-moreira-temas-serie4-1989': 'Barbosa Moreira', 'taruffo-la-prova-1992': 'Taruffo',
         'eid-litisconsorcio-unitario': 'Eid', 'didier-resposta-reu-revelia': 'Didier, resposta', 'passos-teoria-nulidades': 'Passos',
         'lucon-cpc-355-357': 'Lucon', 'knijnik-prova-caps1-2': 'Knijnik', 'carpes-onus-da-prova': 'Carpes', 'costa-atos-processuais': 'Costa',
         'koplin-audiencias': 'Koplin'}
def kind(s):
    if s == CPC: return 'law'
    if s.startswith(('moodle', 'exam')): return 'doc'
    return 'doctrine'
used = {r['source_id'] for r in rows if r['role'] in ('primary', 'supporting')}
shelf = [s for s in sorted(counts, key=lambda s: (kind(s) != 'doctrine', -counts[s])) if s != CPC and s in used and not s.startswith('peer')]

W, H = 1200, 600
X0, X1 = 40, 1160
yA, yB, yC = 70, 200, 520
out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Processo Civil triage map: {len(rows):,} decisions, {sum(1 for r in rows if r["role"]=="primary")} primary routes from chapters to 22 lessons">']
out.append('<style>.rm-k{font:500 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase;fill:var(--muted)}.rm-n{font:600 11px var(--mono);fill:var(--ink)}.rm-b{font:500 10px var(--mono);fill:var(--ink);opacity:.8}</style>')

# A: the CPC ruler
cpcN = counts.get(CPC, 1072)
def ax(i): return X0 + (X1 - X0) * i / max(cpcN - 1, 1)
out.append(f'<line x1="{X0}" y1="{yA}" x2="{X1}" y2="{yA}" style="stroke:var(--ink);stroke-width:1;opacity:.5"/>')
ticks = ''.join(f'M{ax(i):.1f} {yA - (6 if i % 100 == 0 else 3)}V{yA}' for i in range(cpcN))
out.append(f'<path d="{ticks}" style="stroke:var(--ink);stroke-width:.5;opacity:.35"/>')
out.append(f'<text x="{X0}" y="{yA - 16}" class="rm-k">CPC · {cpcN:,} articles</text>')

# B: the shelf of books and documents
tot = sum(max(counts[s], 3) for s in shelf); gap = 10
avail = X1 - X0 - gap * (len(shelf) - 1)
pos, x = {}, X0
for s in shelf:
    w = avail * max(counts[s], 3) / tot
    pos[s] = (x, w)
    col = 'var(--conc)' if kind(s) == 'doc' else 'var(--ink)'
    n = counts[s]
    tk = ''.join(f'M{x + w * (i + .5) / n:.1f} {yB - 5}V{yB + 5}' for i in range(n))
    out.append(f'<path d="{tk}" style="stroke:{col};stroke-width:.8;opacity:.55"/>')
    out.append(f'<line x1="{x:.1f}" y1="{yB}" x2="{x + w:.1f}" y2="{yB}" style="stroke:{col};stroke-width:1.2;opacity:.7"/>')
    if w > 46 and kind(s) != 'doc':
        out.append(f'<text x="{x:.1f}" y="{yB + 22}" class="rm-b">{SHORT.get(s, s[:12])}</text>')
    x += w + gap
docs = [s for s in shelf if kind(s) == 'doc']
if docs:
    dx = pos[docs[0]][0]
    out.append(f'<text x="{dx:.1f}" y="{yB + 22}" class="rm-b" style="fill:var(--conc)">Moodle · exams</text>')
out.append(f'<text x="{X0}" y="{yB - 16}" class="rm-k">books and documents · one tick per chapter</text>')

def src_xy(s, cid):
    i = order.get((s, cid), order.get((s, pathlib.Path(cid).stem), 0))
    if s == CPC: return ax(i), yA
    if s in pos:
        x, w = pos[s]; n = counts[s]; return x + w * (i + .5) / n, yB + 5
    return None

# C: lessons
def lx(j): return X0 + 20 + (X1 - X0 - 40) * j / (len(lessons) - 1)
lp = {l: lx(j) for j, l in enumerate(lessons)}

def thread(r, faint):
    p = src_xy(r['source_id'], r['chapter_id'])
    if not p or r['lesson_id'] not in lp: return ''
    x1, y1 = p; x2, y2 = lp[r['lesson_id']], yC - 8
    my = (y1 + y2) / 2
    k = kind(r['source_id'])
    col = {'law': 'var(--dif)', 'doc': 'var(--conc)', 'doctrine': 'var(--ink)'}[k]
    op, sw = (.07, .6) if faint else ((.55, 1.1) if k != 'law' else (.42, .9))
    return f'<path d="M{x1:.1f} {y1}C{x1:.1f} {my:.0f} {x2:.1f} {my:.0f} {x2:.1f} {y2}" style="fill:none;stroke:{col};stroke-width:{sw};opacity:{op}"/>'
out.append('<g>' + ''.join(thread(r, True) for r in rows if r['role'] == 'supporting') + '</g>')
out.append('<g>' + ''.join(thread(r, False) for r in rows if r['role'] == 'primary') + '</g>')

# lesson nodes + P1/P2 split
p2 = next((j for j, l in enumerate(lessons) if not exam_of[l].upper().startswith('P1')), None)
if p2:
    sx = (lx(p2 - 1) + lx(p2)) / 2
    out.append(f'<line x1="{sx:.1f}" y1="{yC - 30}" x2="{sx:.1f}" y2="{yC + 40}" style="stroke:var(--muted);stroke-width:1;stroke-dasharray:3 4"/>')
    out.append(f'<text x="{sx - 8:.1f}" y="{yC + 52}" text-anchor="end" class="rm-k">P1</text><text x="{sx + 8:.1f}" y="{yC + 52}" class="rm-k">P2</text>')
for j, l in enumerate(lessons):
    x = lx(j)
    out.append(f'<circle cx="{x:.1f}" cy="{yC}" r="7" style="fill:var(--bg,var(--paper));stroke:var(--ink);stroke-width:1.4"/>')
    lab = l.replace('aula-', '').replace('.html', '').replace('-citacao', 'c').replace('-revelia', 'r').replace('-estabilizacao', 'e').replace('-merito', 'm')
    out.append(f'<text x="{x:.1f}" y="{yC + 26}" text-anchor="middle" class="rm-n">{lab}</text>')
out.append(f'<text x="{X0}" y="{yC + 52}" class="rm-k">22 lessons, in syllabus order</text>')
out.append('</svg>')
sys.stdout.write('\n'.join(out))
