"""Aula 05 · Fig. 1 "A gradação democrática" rebuilt on the course map frame (same as the front and Aula 06).
Four amnesties, four grades of democratic legitimacy (Gargarella). Each panel: the country, the city and year,
a four-step scale filled to that grade, and the verdict in one phrase."""
import sys
sys.path.insert(0, '/Users/benecles/Developer/ordenacoes-filipinas-workshop/work/latam-build')
from maps import Frame, HALO
from fk import T, H, L, R, dot, replace_panels, PHONE

F = Frame('courts')
BUE, LIM, MVD = (-58.38, -34.6), (-77.04, -12.05), (-56.2, -34.9)
G = [  # pid, iso, city pt, pin label, grade, tone, law, context, verdict
    ('p-gr0', 'ARG', BUE, 'Buenos Aires · 1983', 1, 'conc', 'AUTOANISTIA DE BIGNONE', 'a ditadura perdoa a si mesma', 'ilegitimidade máxima'),
    ('p-gr1', 'PER', LIM, 'Lima · 1995', 2, 'conc', 'LEI DE FUJIMORI', 'Congresso pós-autogolpe', 'presunção muito baixa'),
    ('p-gr2', 'ARG', BUE, 'Buenos Aires · 1986–87', 3, 'dif', 'LEIS DE ALFONSÍN', 'Congresso livre, sob pressão', 'legítimas, mas golpeadas'),
    ('p-gr3', 'URY', MVD, 'Montevidéu · 1986', 4, 'dif', 'LEI DE CADUCIDADE', 'mais referendo e plebiscito', 'o topo da escala'),
]

def land(focus, tone):
    o = f'<g clip-path="url(#f{F.name}-frame-clip)">'
    for k in F.ct:
        on = k == focus
        fill = f'var(--{tone}-wash)' if on else 'color-mix(in srgb,var(--ink) 7%,var(--paper))'
        o += f'<use href="#f{F.name}-{k}" style="fill:{fill};stroke:{"var(--" + tone + ")" if on else "var(--paper)"};stroke-width:{1.4 if on else .9};stroke-linejoin:round"/>'
    return o + '</g>'

def scale(grade, tone, x=40, y=330):
    o = T(x, y - 16, 'LEGITIMIDADE DEMOCRÁTICA', 13, 'muted')
    for i in range(4):
        h = 14 + i * 12
        fill = (f'{tone}s' if i + 1 == grade else tone) if i + 1 <= grade else 'paper'
        o += R(x + i * 44, y + 50 - h, 34, h, fill, 'ink', 1.2)
    o += T(x, y + 74, 'MENOS', 12, 'muted') + T(x + 166, y + 74, 'MAIS', 12, 'muted', 'end')
    return o

def panel(pid, iso, pt, pin, grade, tone, law, ctx, verdict, on=False):
    x, y = F.xy(*pt)
    body = land(iso, tone)
    body += dot(x, y, 5) + f'<text x="{x + 12}" y="{y + 5}" class="t-small" style="font-size:14px;font-weight:600;fill:var(--ink);{HALO}">{pin}</text>'
    body += scale(grade, tone)
    body += T(40, 452, f'GRAU {grade} DE 4', 15, tone, weight=700)
    body += T(40, 480, law, 14, 'ink', weight=600) + T(40, 506, ctx, 14, 'ink2', cls='t-small')
    body += H(40, 546, verdict, 22, tone)
    return (f'<svg class="panel fig figkit lt{" on" if on else ""}" id="{pid}" viewBox="0 0 {F.W} {F.H}" role="img" aria-label="{law}: grau {grade}">{PHONE}'
            f'{body}<text x="{F.W - 30}" y="34" text-anchor="end" class="t-small" style="font-size:14px;letter-spacing:.1em">QUATRO ANISTIAS, QUATRO GRAUS</text></svg>')

PANELS = {g[0]: panel(*g, on=(i == 0)) for i, g in enumerate(G)}
DEFS = f'<svg width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true">{F.defs()}</svg>'

if __name__ == '__main__':
    p = sys.argv[1]
    h = open(p).read()
    h = replace_panels(h, PANELS)
    i = h.index('id="p-gr0"'); s = h.rindex('<div class="scrolly">', 0, i)
    h = h[:s] + DEFS + '\n' + h[s:]
    open(p, 'w').write(h)
    print('a05 fig1 ok')
