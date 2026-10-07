"""Aula 14 score: the statutory sequence in CPC arts. 369–371."""
from figkit import t, line, svg


def panel():
    # Four measured statutory operations share two staves; alignment is the comparison.
    x0, x1 = 205, 1050
    xs = [x0 + i * (x1 - x0) / 4 for i in range(5)]
    o = ''
    # Staff rules and measure bars are the score's information-bearing geometry.
    for y, tone in [(252, 'conc'), (423, 'dif')]:
        o += line(x0, y, x1, y, tone='ink', w=2.2)
        for x in xs:
            o += line(x, y - 18, x, y + 18, tone=tone, w=1.5)
    for i, x in enumerate(xs):
        o += line(x, 210, x, 465, tone='muted', w=1, dash='2 5')
    # Ordered measure heads: article and operative statutory term.
    heads = [('369', 'meios legítimos'), ('370', 'pedido / ofício'),
             ('370', 'necessidade / recusa'), ('371', 'avaliação / razões')]
    for i, (art, lab) in enumerate(heads):
        cx = (xs[i] + xs[i+1]) / 2
        o += t(cx, 190, 'ART. ' + art, size=13, fill='var(--ink)', anchor='middle', weight=700)
        o += t(cx, 211, lab.upper(), size=11, fill='var(--ink-2)', anchor='middle', weight=600)
    o += t(35, 258, 'DEMONSTRATIVO', size=12, fill='var(--conc)', weight=700)
    o += t(35, 429, 'ARGUMENTATIVO', size=12, fill='var(--dif)', weight=700)
    o += t(35, 447, '/ PERSUASIVO', size=11, fill='var(--dif)', weight=600)
    upper = ['qual afirmação', 'o que informa', 'qual lacuna', 'qual conclusão']
    lower = ['quem participa', 'quem provoca', 'qual razão', 'quais razões']
    for i, x in enumerate(xs[:-1]):
        cx = (x + xs[i+1]) / 2
        # Paired note-heads, joined by one continuous staff: two lenses, one law.
        o += f'<circle cx="{cx:g}" cy="252" r="8" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/>'
        o += f'<circle cx="{cx:g}" cy="423" r="8" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:2"/>'
        o += t(cx, 294, upper[i], size=12, fill='var(--ink)', anchor='middle', weight=600, ls='.01em')
        o += t(cx, 315, 'sustentada?', size=12, fill='var(--ink-2)', anchor='middle', weight=500, ls='.01em')
        o += t(cx, 465, lower[i], size=12, fill='var(--ink)', anchor='middle', weight=600, ls='.01em')
        o += t(cx, 486, 'no processo?', size=12, fill='var(--ink-2)', anchor='middle', weight=500, ls='.01em')
    # Four beats survive removal of every label: order and vertical pairing remain visible.
    o += line(x0, 535, x1, 535, tone='ink', w=1.4)
    for i, x in enumerate(xs):
        o += f'<circle cx="{x:g}" cy="535" r="4" style="fill:var(--ink)"/>'
    o += t(x0, 565, 'MEIOS', size=11, fill='var(--ink-2)', weight=600)
    o += t(xs[1], 565, 'INICIATIVA', size=11, fill='var(--ink-2)', anchor='middle', weight=600)
    o += t(xs[2], 565, 'NECESSIDADE', size=11, fill='var(--conc)', anchor='middle', weight=700)
    o += t(xs[3], 565, 'AVALIAÇÃO', size=11, fill='var(--ink-2)', anchor='middle', weight=600)
    o += t(x1, 565, 'DECISÃO', size=11, fill='var(--ink-2)', anchor='end', weight=600)
    return svg('20 165 1045 415', o, cls='fig', ident='pci-a14-score',
               label='Partitura dos arts. 369 a 371: duas pautas mostram perguntas demonstrativas e argumentativas sobre os mesmos marcos legais')


if __name__ == '__main__':
    print(panel())
