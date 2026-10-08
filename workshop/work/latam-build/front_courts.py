"""Latam course front, v2 (Claude, 05/10): "Quem respondeu a quem".
Five courts on a cropped map (Central America → Río de la Plata). Orange arcs: a national court and the
Corte IDH answered the same question differently. Blue arc: an idea that travelled (the ECI, Bogotá → Brasília).
Each arc and pin carries its lesson number; the dialogue list beside the map (HTML, so it reads on phones and
stacks under the map when the phone is upright) gives the cases, the years and the links.
Writes the drawing into tools/fronts/data/direito-latino-americano.json (inner_html + css)."""
import json, sys
from maps import Frame, HALO

F = Frame('courts')
SJ, BOG, BSB, SUC, MVD = (-84.08, 9.93), (-74.07, 4.71), (-47.9, -15.8), (-65.26, -19.05), (-56.2, -34.9)
COURT_ISO = ('CRI', 'COL', 'BRA', 'BOL', 'URY')

def P(pt): return F.xy(*pt)

def arc(a, b, bend, tone, dash=False):
    (x1, y1), (x2, y2) = P(a), P(b)
    cx, cy = (x1 + x2) / 2 - (y2 - y1) * bend, (y1 + y2) / 2 + (x2 - x1) * bend
    mx, my = .25 * x1 + .5 * cx + .25 * x2, .25 * y1 + .5 * cy + .25 * y2   # midpoint of the quadratic
    da = ';stroke-dasharray:7 5' if dash else ''
    d = f'M{x1} {y1}Q{cx:.1f} {cy:.1f} {x2} {y2}'
    path = (f'<path d="{d}" style="fill:none;stroke:var(--paper);stroke-width:7;stroke-linecap:round;opacity:.9"/>'
            f'<path class="draw" d="{d}" style="fill:none;stroke:var(--{tone});stroke-width:2.6;stroke-linecap:round{da}"/>')
    return path, (mx, my)

def tag(x, y, n, tone, href, label):
    w = 30
    return (f'<a href="{href}" aria-label="{label}"><rect x="{x - w / 2:.1f}" y="{y - 11:.1f}" width="{w}" height="22" '
            f'style="fill:var(--paper);stroke:var(--{tone});stroke-width:1.6"/>'
            f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" style="font:700 13px var(--mono);fill:var(--{tone})">{n}</text></a>')

def city(pt, name, court, dx, dy, anchor='start'):
    x, y = P(pt)
    return (f'<circle cx="{x}" cy="{y}" r="4.5" style="fill:var(--ink)"/>'
            f'<circle cx="{x}" cy="{y}" r="8.5" style="fill:none;stroke:var(--ink);stroke-width:1"/>'
            f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" style="font:600 16px var(--mono);fill:var(--ink);{HALO}">{name}</text>'
            f'<text x="{x + dx}" y="{y + dy + 18}" text-anchor="{anchor}" style="font:14px var(--mono);fill:var(--ink-2);{HALO}">{court}</text>')

# ---- map
o = f'<g clip-path="url(#f{F.name}-frame-clip)">'
# engraved coast rings in the sea (house atlas style): faint rules alternating with paper, under the land
for w, col, op in ((16, 'var(--grid-major)', .5), (12.5, 'var(--paper)', 1), (9, 'var(--grid-major)', .5), (6, 'var(--paper)', 1), (3, 'var(--grid-major)', .6)):
    o += f'<use href="#f{F.name}-coast" style="fill:none;stroke:{col};stroke-width:{w};stroke-linejoin:round;opacity:{op}"/>'
# land on paper; the four national courts in alternating blue/violet washes (neighbours never share one), the Corte IDH's host in orange
WASH = {'COL': 'dif', 'BRA': 'mix', 'BOL': 'dif', 'URY': 'dif', 'CRI': 'conc'}
for k in F.ct:
    t = WASH.get(k)
    st = (f'fill:var(--{t}-wash);stroke:var(--{t});stroke-width:1.1' if t else 'fill:var(--paper);stroke:var(--ink-2);stroke-width:.6;stroke-opacity:.55')
    o += f'<use href="#f{F.name}-{k}" style="{st};stroke-linejoin:round"/>'
o += f'<use href="#f{F.name}-coast" style="fill:none;stroke:var(--ink-2);stroke-width:1;stroke-linejoin:round"/>'
o += '</g>'
o += F.graticule(lats=((0, 'Equador'), (-23.44, 'Trópico de Capricórnio')), labels=False)
ex, ey = F.xy(-31, 0); tx, ty = F.xy(-31, -23.44)
o += (f'<text x="{ex}" y="{ey - 5}" text-anchor="end" style="font:italic 12px var(--serif,serif);fill:var(--muted);{HALO}">Equador</text>'
      f'<text x="{tx}" y="{ty - 5}" text-anchor="end" style="font:italic 12px var(--serif,serif);fill:var(--muted);{HALO}">Trópico de Capricórnio</text>')
o += F.sea(-84, -21, 'OCEANO PACÍFICO', 13) + F.sea(-38, 6, 'OCEANO ATLÂNTICO', 13) + F.sea(-73.5, 15.5, 'MAR DO CARIBE', 12)
arcs = [  # (from, to, bend, tone, lesson, href, aria)
    (SJ, BSB, -.12, 'conc', '03', 'aula-03.html', 'Aula 03: ADPF 153 e Gomes Lund'),
    (SJ, MVD, -.10, 'conc', '05', 'aula-05.html', 'Aula 05: Gelman e a Suprema Corte uruguaia'),
    (SJ, SUC, .10, 'conc', '06', 'aula-06.html', 'Aula 06: Bolívia e OC-28'),
    (BOG, BSB, .16, 'dif', '07', 'aula-07.html', 'Aula 07: o estado de coisas inconstitucional, de Bogotá a Brasília'),
]
paths, tags = '', ''
for a, b, bend, tone, n, href, aria in arcs:
    p, (mx, my) = arc(a, b, bend, tone)
    paths += p
    tags += tag(mx, my, n, tone, href, aria)
o += paths
o += city(SJ, 'San José', 'Corte IDH', -14, -24, 'end')
o += city(BOG, 'Bogotá', 'Corte Constitucional', 14, -26)
o += city(BSB, 'Brasília', 'STF', 14, -6)
o += city(SUC, 'Sucre', 'TCP', -14, 4, 'end')
o += city(MVD, 'Montevidéu', 'SCJ', 14, 4)
# domestic dockets: lesson tags beside the pin
bx, by = P(BOG); sx, sy = P(BSB)
tags += tag(bx + 14 + 6 * 8.6 + 26, by - 31, '04', 'ink', 'aula-04.html', 'Aula 04: Colômbia, paz e Corte Constitucional')
tags += tag(sx + 26, sy + 26, '09', 'ink', 'aula-09.html', 'Aula 09: saúde no STF')
o += tags
o += (f'<text x="{F.W - 28}" y="20" text-anchor="end" class="t-small" style="font:12px var(--mono);letter-spacing:.1em;fill:var(--ink)">QUEM RESPONDEU A QUEM</text>')
svg = (f'<svg class="fig courts-map" viewBox="0 0 {F.W} {F.H}" role="img" '
       f'aria-label="Mapa das cinco cortes do curso e das decisões que dialogaram entre si">{F.defs()}{o}</svg>')

# ---- the dialogue list (HTML)
D = [
    ('03', 'conc', 'aula-03.html', 'Brasília × San José', 'ADPF 153 <i>×</i> Gomes Lund', '2010', 'A mesma Lei de Anistia, lida em abril pelo STF e em novembro pela Corte IDH.'),
    ('04', 'ink', 'aula-04.html', 'Bogotá', 'C-579 · C-694 · C-674', '2013–2017', 'A Corte Constitucional aceita a justiça de transição e impõe limites a cada reforma.'),
    ('05', 'conc', 'aula-05.html', 'Montevidéu × San José', 'Gelman <i>→</i> SCJ 20/2013', '2011–2013', 'Duas votações populares, uma sentença internacional e a resposta da Suprema Corte.'),
    ('06', 'conc', 'aula-06.html', 'Sucre × San José', 'SCP 0084 <i>×</i> OC-28', '2017–2021', 'A Convenção usada para liberar a reeleição, e depois para limitá-la.'),
    ('07', 'dif', 'aula-07.html', 'Bogotá → Brasília', 'T-153 <i>→</i> ADPF 347', '1998–2023', 'O estado de coisas inconstitucional atravessa o continente. Segue na Aula 08 com a T-025.'),
    ('09', 'ink', 'aula-09.html', 'Brasília', 'STA 175 <i>→</i> Temas 6 e 1234', '2010–2024', 'Saúde: do pedido individual ao acordo entre os entes.'),
]
lis = ''.join(
    f'<li class="dlg dlg-{tone}"><a href="{href}"><span class="dlg-n">{n}</span><span class="dlg-who">{who}</span>'
    f'<span class="dlg-cases">{cases} <span class="dlg-yr">{yr}</span></span><span class="dlg-does">{does}</span></a></li>'
    for n, tone, href, who, cases, yr, does in D)
html = (f'<div class="atlas courts"><div class="courts-sheet">{svg}</div>'
        f'<ol class="dialogues" aria-label="As decisões do curso, por aula">{lis}</ol></div>')

css = ('.atlas.courts{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:clamp(22px,3vw,40px);align-items:start}'
       '.courts-sheet{border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major)}'
       '.courts-sheet svg{display:block;width:100%;height:auto}'
       '.courts-map a{cursor:pointer}.courts-map a:hover rect,.courts-map a:focus-visible rect{fill:var(--paper-2)}'
       '.dialogues{list-style:none;margin:0;padding:0;display:grid;gap:0;border-top:1.5px solid var(--ink)}'
       '.dlg a{display:grid;grid-template-columns:44px minmax(0,1fr);column-gap:14px;row-gap:2px;padding:13px 0;border-bottom:1px solid var(--grid-major);color:var(--ink);text-decoration:none}'
       '.dlg a:hover,.dlg a:focus-visible{background:var(--paper-2)}'
       '.dlg-n{grid-row:1/4;align-self:start;font:700 15px var(--mono);text-align:center;border:1.6px solid var(--ink);padding:3px 0}'
       '.dlg-conc .dlg-n{color:var(--conc);border-color:var(--conc)}.dlg-dif .dlg-n{color:var(--dif);border-color:var(--dif)}'
       '.dlg-who{font:12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}'
       '.dlg-cases{font:650 17px/1.25 var(--sans)}.dlg-cases i{font-style:normal;color:var(--muted);padding:0 .1em}'
       '.dlg-yr{font:13px var(--mono);font-weight:400;color:var(--muted);margin-left:.4em}'
       '.dlg-does{font:15px/1.4 var(--serif);color:var(--ink-2)}'
       '@media (max-width:860px) and (orientation:portrait){.atlas.courts{grid-template-columns:1fr}}')

if __name__ == '__main__':
    target = sys.argv[1]
    d = json.load(open(target))
    d['drawing'] = {'inner_html': html, 'css': css}
    json.dump(d, open(target, 'w'), ensure_ascii=False, indent=2)
    print('front drawing', len(html), 'chars')
