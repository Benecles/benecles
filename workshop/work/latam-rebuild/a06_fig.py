"""Aula 06 · Fig. 1 "Três usos da Convenção" on the course's map frame (the same one as the front).
Replaces a blurred ghost map with one label per panel. Each panel: the country in play, its line to San José,
a dated record in the open Pacific, and whom the Convention protected that time."""
import sys
sys.path.insert(0, '/Users/benecles/Developer/ordenacoes-filipinas-workshop/work/latam-build')
from maps import Frame, HALO
from fk import T, H, L, dot, replace_panels, set_caption, PHONE

F = Frame('courts')
SJ, BOG, SUC, MVD = (-84.08, 9.93), (-74.07, 4.71), (-65.26, -19.05), (-56.2, -34.9)
FOCUS = {'p-us0': 'URY', 'p-us1': 'BOL', 'p-us2': 'COL'}

def land(focus, tone):
    o = f'<g clip-path="url(#f{F.name}-frame-clip)">'
    for k in F.ct:
        fill = f'var(--{tone}-wash)' if k == focus else 'color-mix(in srgb,var(--ink) 7%,var(--paper))'
        stroke = f'var(--{tone})' if k == focus else 'var(--paper)'
        o += f'<use href="#f{F.name}-{k}" style="fill:{fill};stroke:{stroke};stroke-width:{1.4 if k == focus else .9};stroke-linejoin:round"/>'
    return o + '</g>' + F.graticule(lats=((0, ''),), labels=False)

def pin(pt, name, dx, dy, anchor='start', strong=True):
    x, y = F.xy(*pt)
    return (dot(x, y, 4.5 if strong else 3.5, 'ink' if strong else 'muted')
            + f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" class="t-small" style="font-size:14px;font-weight:600;fill:var(--ink);{HALO}">{name}</text>')

def line(a, b, tone, bend=.12, dash=False):
    (x1, y1), (x2, y2) = F.xy(*a), F.xy(*b)
    cx, cy = (x1 + x2) / 2 - (y2 - y1) * bend, (y1 + y2) / 2 + (x2 - x1) * bend
    return L(f'M{x1} {y1}Q{cx:.0f} {cy:.0f} {x2} {y2}', tone, 2.4, 1, '7 5' if dash else '')

def record(rows, protects, tone):
    """rows: [(date, claim)], drawn in the open Pacific (lower left)."""
    o, y = '', 392
    o += L(f'M40 {y - 26}H290', 'ink', 1.2, .5)
    for date, claim in rows:
        o += T(40, y, date, 15, 'ink', weight=700) + T(40, y + 28, claim, 14, 'ink2')
        y += 72
    o += H(40, y + 6, protects, 22, tone)
    return o

def panel(pid, aria, title, body, on=False):
    return (f'<svg class="panel fig figkit lt{" on" if on else ""}" id="{pid}" viewBox="0 0 {F.W} {F.H}" role="img" aria-label="{aria}">{PHONE}'
            f'{body}<text x="{F.W - 30}" y="34" text-anchor="end" class="t-small" style="font-size:14px;letter-spacing:.1em">{title}</text></svg>')

sj = lambda: pin(SJ, 'San José', 10, -14)
P0 = land('URY', 'dif') + line(SJ, MVD, 'dif', -.2) + sj() + pin(MVD, 'Montevidéu', 12, 5) + record(
    [('1989 E 2009', 'O VOTO MANTÉM A LEI'), ('2011 · GELMAN', 'A LEI NÃO VALE')], 'protege as vítimas', 'dif')
P1 = land('BOL', 'conc') + sj() + pin(SUC, 'Sucre', 12, 5) + record(
    [('21/02/2016', 'REFERENDO: NÃO'), ('28/11/2017 · TCP', 'ART. 23 PREVALECE')], 'protege quem governa', 'conc')
P2 = (land('COL', 'dif') + line(BOG, SJ, 'ink', .25, dash=True)
      + sj() + pin(BOG, 'Bogotá', 12, -8) + record(
    [('21/10/2019', 'A COLÔMBIA CONSULTA'), ('07/06/2021 · 5 × 2', 'REELEIÇÃO INDEFINIDA'), ('', 'NÃO É DIREITO')], 'protege a alternância', 'dif'))

PANELS = {
    'p-us0': panel('p-us0', 'Gelman: a Convenção contra a maioria', 'GELMAN · 2011', P0, on=True),
    'p-us1': panel('p-us1', 'Bolívia: a Convenção contra a Constituição', 'SCP 0084 · 2017', P1),
    'p-us2': panel('p-us2', 'OC-28: a Convenção a favor dos limites', 'OC-28 · 2021', P2),
}
DEFS = f'<svg width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true">{F.defs()}</svg>'

if __name__ == '__main__':
    p = sys.argv[1]
    h = open(p).read()
    h = replace_panels(h, PANELS)
    i = h.index('id="p-us0"'); s = h.rindex('<div class="scrolly">', 0, i)
    h = h[:s] + DEFS + '\n' + h[s:]
    open(p, 'w').write(h)
    print('a06 fig ok')
