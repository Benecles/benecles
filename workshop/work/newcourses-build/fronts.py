"""Course-front drawings for the new courses (Claude). FRONTS[cname]() returns (svg_html, phone_note) and build.py puts it
on the front in place of the generic station track. Content only from the lessons: every place below is named in the
Metodologia drafts (lesson numbers in the labels)."""
import sys
sys.path.insert(0, '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/latam-build')
from maps import Frame, HALO

FRONTS = {}

def _label(x, y, name, aulas, href, anchor='start', dx=12, dy=4, lead=False):
    lx, ly = x + dx, y + dy
    ld = (f'<path d="M{x} {y}L{lx - (4 if anchor == "start" else -4)} {ly - 5}" style="fill:none;stroke:var(--ink-2);stroke-width:.9"/>' if lead else '')
    return (f'<a href="{href}" aria-label="{name}: aulas {aulas}">{ld}'
            f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" style="font:600 15px var(--sans);fill:var(--ink);{HALO}">{name}</text>'
            f'<text x="{lx}" y="{ly + 17}" text-anchor="{anchor}" style="font:500 12px var(--mono);letter-spacing:.06em;fill:var(--conc);{HALO}">aulas {aulas}</text></a>')

def mj_front():
    F = Frame('iuscommune')
    europe = {'ITA': 'conc', 'ESP': 'conc', 'PRT': 'conc'}
    indies = {'MEX': 'dif', 'PER': 'dif', 'BOL': 'dif', 'ARG': 'dif', 'BRA': 'dif'}
    o = F.defs() + F.graticule(labels=False) + F.base({**europe, **indies}) + F.grat_labels()
    o += F.sea(-40, 30, 'OCEANO ATLÂNTICO', 15) + F.sea(-100, -22, 'OCEANO PACÍFICO', 15)
    # the journey: from the Italian schools to the Iberian peninsula, then to the Indies and to Brazil
    B, SAL, COI, MAD = (11.34, 44.49), (-5.66, 40.97), (-8.43, 40.21), (-3.70, 40.42)
    MEX, LIMA, CHA, BA = (-99.13, 19.43), (-77.04, -12.05), (-65.26, -19.05), (-58.38, -34.60)
    OLI, SP, RIO, POA = (-34.86, -8.01), (-46.63, -23.55), (-43.17, -22.91), (-51.23, -30.03)
    o += F.flow(B, MAD, bend=.18, tone='conc', d=.3, w=2.4)
    o += F.flow(SAL, MEX, bend=.16, tone='dif', d=.8, w=2.2)
    o += F.flow(SAL, LIMA, bend=.10, tone='dif', d=1.0, w=2.2)
    o += F.flow(COI, OLI, bend=-.12, tone='dif', d=1.2, w=2.2, dash=True)
    for p in (B, SAL, COI, MAD, (-5.99, 37.39), (-9.14, 38.72), MEX, LIMA, CHA, BA, OLI, SP, RIO, POA):
        o += F.pin(*p, r=3.5)
    x, y = F.xy(*B); o += _label(x, y, 'Bolonha', '01 · 02', 'aula-01.html', 'end', -12, -16)
    x, y = F.xy(-9.5, 40.0)
    bx, by = x - 36, y + 34
    o += (f'<a href="aula-02.html" aria-label="Península Ibérica: aulas 02, 05, 06, 08, 14">'
          f'<path d="M{bx + 4} {by - 12}L{x - 4} {y + 2}" style="fill:none;stroke:var(--ink-2);stroke-width:.9"/>'
          f'<text x="{bx}" y="{by}" text-anchor="end" style="font:600 15px var(--sans);fill:var(--ink);{HALO}">Península Ibérica</text>'
          f'<text x="{bx}" y="{by + 17}" text-anchor="end" style="font:500 11.5px var(--mono);fill:var(--ink-2);{HALO}">Salamanca · Coimbra · Lisboa</text>'
          f'<text x="{bx}" y="{by + 32}" text-anchor="end" style="font:500 11.5px var(--mono);fill:var(--ink-2);{HALO}">Madri · Sevilha</text>'
          f'<text x="{bx}" y="{by + 49}" text-anchor="end" style="font:500 12px var(--mono);letter-spacing:.06em;fill:var(--conc);{HALO}">aulas 02 · 05 · 06 · 14</text></a>')
    x, y = F.xy(*MEX); o += _label(x, y, 'México', '05 · 09', 'aula-05.html', 'start', 12, -10)
    x, y = F.xy(*LIMA); o += _label(x, y, 'Lima', '04 · 06 · 07 · 08', 'aula-04.html', 'end', -12, 4)
    x, y = F.xy(*CHA); o += _label(x, y, 'Charcas', '07', 'aula-07.html', 'start', 12, -6)
    x, y = F.xy(*BA); o += _label(x, y, 'Buenos Aires', '04 · 07', 'aula-07.html', 'end', -12, 10)
    x, y = F.xy(*OLI); o += _label(x, y, 'Olinda · São Paulo · Rio', '14', 'aula-14.html', 'start', 12, 2)
    x, y = F.xy(*POA); o += _label(x, y, 'Porto Alegre', '15', 'aula-15.html', 'start', 14, 16)
    o += (f'<text x="28" y="40" style="font:600 13px var(--mono);letter-spacing:.12em;fill:var(--ink)">O PERCURSO DO DIREITO COMUM</text>'
          f'<text x="28" y="60" style="font:italic 15px var(--serif,serif);fill:var(--ink-2)">das escolas de Bolonha às Índias e ao Brasil</text>')
    lx, ly = 28, F.H - 70
    o += (f'<rect x="{lx}" y="{ly}" width="16" height="12" style="fill:var(--conc-wash);stroke:var(--conc)"/><text x="{lx + 24}" y="{ly + 11}" style="font:12px var(--mono);fill:var(--ink-2)">onde o direito comum se forma e é recebido</text>'
          f'<rect x="{lx}" y="{ly + 22}" width="16" height="12" style="fill:var(--dif-wash);stroke:var(--dif)"/><text x="{lx + 24}" y="{ly + 33}" style="font:12px var(--mono);fill:var(--ink-2)">onde ele chega: as Índias e o Brasil</text>')
    svg = (f'<svg class="mj-map" viewBox="0 0 {F.W} {F.H}" role="img" aria-label="Mapa do curso: o percurso do direito comum, de Bolonha à '
           f'Península Ibérica e daí às Índias e ao Brasil; cada lugar leva à aula que o estuda">{o}</svg>')
    return svg, 'Cada lugar do mapa leva à aula que o estuda. No celular, deslize o mapa para o lado.'

FRONTS['metodologia'] = mj_front
