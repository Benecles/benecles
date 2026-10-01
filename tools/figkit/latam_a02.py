"""Latam Aula 02 · Fig. 1 (Onde cada corte ficou), 4 steps: the thesis as a field, Argentina as a timeline,
Chile/Colômbia as the cooptação loop, Brasil as the activism timeline. Replaces the empty livro-razão ledgers."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Field, Timeline, svg, t, line, TONE, WASH

IDS = ['p-ax0', 'p-ax1', 'p-ax2', 'p-ax3']
LABELS = ['Dois grupos', 'Argentina e Venezuela', 'Chile e Colômbia: cooptação', 'Brasil: nomeação política, corte forte']


def tese(active=None):
    f = Field('a02-tese', x0=170, x1=560, y0=90, y1=450)
    f.region(90, 270, 'dif', .3)
    f.axes([(250, ('nomeação', 'política')), (480, ('cooptação', 'a magistratura escolhe'))],
           [(150, ('alta', 'autonomia')), (390, ('baixa', 'autonomia'))], xtitle='Como o ministro chega à corte', ytitle='Autonomia')
    hot = lambda c: active is None or c in active
    f.o.append('<path d="M292 346L440 182" style="fill:none;stroke:var(--ink-2);stroke-width:1.2;stroke-dasharray:3 5"/>')
    f.o.append(t(386, 300, "o esperado", size=10, fill='var(--ink-2)', italic=True))
    f.point(250, 390, 'Argentina', active=hot('AR'), tone='conc', dx=14, dy=-6)
    f.point(250, 418, 'Venezuela', active=hot('VE'), tone='conc', dx=14, dy=6)
    f.point(480, 140, 'Chile', active=hot('CL'), tone='dif', dx=14, dy=-2)
    f.point(480, 168, 'Colômbia', active=hot('CO'), tone='dif', dx=14, dy=6)
    f.point(250, 150, 'Brasil', active=hot('BR'), tone='mix', dx=14, sub='fora da diagonal: por quê?')
    return f.svg()


def argentina():
    tl = Timeline('a02-ar', 50, 560, 300, 1925, 1985)
    o = t(50, 44, 'Argentina · a Corte valida golpes por acordada', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    for yr, h in ((1930, 90), (1943, 130), (1955, 90), (1962, 130), (1966, 170), (1976, 90)):
        tl.event(yr, h, str(yr), tone='conc')
    tl.span(72, 1947, 1985, 'cada troca de governo troca a Corte inteira', tone='ink', open_end=True)
    tl.link(1947, 1930, 70, '1947 · Perón destitui 4 dos 5 ministros', sub='por terem validado o golpe de 1930')
    o += tl.svg()
    o += f'<path d="M50 486h12l-6 -11z" style="fill:var(--conc)"/>' + t(70, 486, 'golpe validado por acordada da Corte', size=10.5)
    o += line(50, 506, 560, 506, tone='muted', w=.8)
    o += t(50, 528, 'Venezuela', size=10.5, caps=True, weight=700)
    o += t(50, 544, 'regras de recrutamento descumpridas; nomeações em regimes de exceção.', size=10.5)
    o += t(50, 559, 'Quase metade dos ministros veio da magistratura, e isso não bastou.', size=10.5, fill='var(--ink-2)')
    return o


def cooptacao():
    cx, cy, r = 300, 250, 120
    o = t(50, 52, 'Chile e Colômbia · recrutamento endógeno', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    o += f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:none;stroke:var(--dif);stroke-width:2.4"/>'
    for ang, (a, b) in ((-90, ('cúpula judicial', '')), (30, ('seleciona', 'novos juízes')), (150, ('promove', 'na carreira'))):
        import math
        x, y = cx + r * math.cos(math.radians(ang)), cy + r * math.sin(math.radians(ang))
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" style="fill:var(--dif);stroke:var(--dif)"/>'
        dx = 0 if ang == -90 else (18 if ang == 30 else -18)
        anc = 'middle' if ang == -90 else ('start' if ang == 30 else 'end')
        dy = -18 if ang == -90 else 4
        o += t(x + dx, y + dy, a, size=11, weight=700, anchor=anc, caps=True, fill='var(--dif)')
        if b:
            o += t(x + dx, y + dy + 14, b, size=10.5, anchor=anc)
    for ang in (-30, 90, 210):
        import math
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        tx, ty = -math.sin(a), math.cos(a)
        o += f'<path d="M{x - tx * 2 - ty * 6:.1f} {y - ty * 2 + tx * 6:.1f}L{x + tx * 9:.1f} {y + ty * 9:.1f}L{x - tx * 2 + ty * 6:.1f} {y - ty * 2 - tx * 6:.1f}z" style="fill:var(--dif)"/>'
    o += t(cx, cy - 6, 'a própria hierarquia', size=10.5, anchor='middle') + t(cx, cy + 9, 'escolhe e promove', size=10.5, anchor='middle')
    o += f'<path d="M86 250H166" style="stroke:var(--conc);stroke-width:2;stroke-dasharray:5 4"/><path d="M160 242l12 16M172 242l-12 16" style="stroke:var(--conc);stroke-width:2.4"/>'
    o += t(86, 236, 'política', size=10.5, caps=True, weight=700, fill='var(--conc)')
    o += t(50, 430, 'Ganho', size=10.5, caps=True, weight=700, fill='var(--dif)') + t(130, 430, 'os Judiciários mais independentes da América do Sul', size=10.5)
    o += t(50, 452, 'Preço', size=10.5, caps=True, weight=700, fill='var(--conc)') + t(130, 452, 'uma elite judicial autocentrada, alheia ao país', size=10.5)
    o += t(50, 474, 'Colômbia', size=10.5, caps=True, weight=700, fill='var(--ink-2)') + t(130, 474, 'a violência política tornou o Judiciário mais ativo', size=10.5)
    return o


def brasil():
    tl = Timeline('a02-br', 50, 560, 330, 1985, 2025, step=1000)
    o = t(50, 52, 'Brasil · nomeação política, corte forte', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    tl.event(1988, 140, 'CF 1988', tone='ink', mark='dot')
    tl.span(150, 1990, 2025, '1 · demandas coletivas por direitos da CF', tone='dif', open_end=True)
    tl.span(186, 1990, 2025, '2 · árbitro entre Legislativo e Executivo', tone='mix', open_end=True)
    tl.span(222, 2010, 2025, '3 · ativismo punitivo', tone='conc', open_end=True)
    o += tl.svg()
    o += t(50, 400, 'O que separa o Brasil da Argentina, para os autores:', size=10.5, fill='var(--ink-2)')
    o += t(50, 418, 'estabilidade institucional e elites preocupadas com legitimação jurídica.', size=10.5, weight=700)
    o += t(50, 446, 'Protagonismo não é sinônimo de proteção de direitos.', size=10.5, fill='var(--conc)', weight=700)
    for yr, lab in ((1988, '1988'), (1995, 'anos 1990'), (2015, 'mais recente')):
        o += line(tl.x(yr), 330, tl.x(yr), 336, w=1) + t(tl.x(yr), 350, lab, size=10, anchor='middle', fill='var(--muted)')
    return o


def panels():
    bodies = [tese(), argentina(), cooptacao(), brasil()]
    return [svg('0 0 600 600', b, cls='panel fig on' if k == 0 else 'panel fig', ident=IDS[k], label=LABELS[k]) for k, b in enumerate(bodies)]
