"""Aula 16 chronology: the three dates stated in the Moodle decision extract."""
from figkit import t, line, svg


def panel():
    # One baseline carries the reported sequence; spacing is ordinal, not elapsed time.
    xs = [135, 570, 1005]
    y = 112
    o = line(xs[0], y, xs[-1], y, tone='ink', w=2)
    labels = [
        ('NOV. 2012', 'compra do aparelho', 'mês indicado'),
        ('18 AGO. 2015', 'ajuizamento da ação', ''),
        ('15 JAN. 2016', 'decisão reconhece decadência', ''),
    ]
    for i, (x, (date, event, precision)) in enumerate(zip(xs, labels)):
        tone = 'conc' if i == 2 else 'ink'
        o += line(x, y - 22, x, y + 22, tone=tone, w=2.2)
        o += f'<circle cx="{x}" cy="{y}" r="5" style="fill:var(--paper);stroke:var(--{tone});stroke-width:2"/>'
        o += t(x, 70, date, size=13, fill=f'var(--{tone})', anchor='middle', weight=700)
        o += t(x, 150, event, size=11.5, fill='var(--ink)', anchor='middle', weight=600, ls='.01em')
        if precision:
            o += t(x, 170, precision, size=10.5, fill='var(--ink-2)', anchor='middle', weight=500, ls='.01em')
    return svg('25 35 1090 155', o, cls='fig', ident='pci-a16-timeline',
               label='Cronologia dos três momentos mencionados no excerto da decisão: compra em novembro de 2012, ajuizamento em 18 de agosto de 2015 e decisão em 15 de janeiro de 2016; o primeiro dado indica apenas o mês')


if __name__ == '__main__':
    print(panel())
