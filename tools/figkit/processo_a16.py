"""Aula 16: chronology and bounded reading of the Moodle decision extract."""
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


def excerpt_panel():
    """Two exact passages, separated by an omission, on one visibly cut document.

    Source: aula-16/30-supporting-003-moodle-model-julgamento-sinceridade-
    moodle-model-julgamento-sinceridade.txt. This is a reading aid, not a facsimile.
    Claim: the excerpt poses a proof question and separately states the result.
    """
    # The torn edges bound the selected text; they do not represent the case file.
    o = '<path d="M38 32l22 -7 22 7 22 -7 22 7 22 -7H790l22 7 22 -7 22 7 22 -7 22 7V345l-22 7 -22 -7 -22 7 -22 -7 -22 7H148l-22 -7 -22 7 -22 -7 -22 7 -22 -7Z" style="fill:var(--paper);stroke:var(--ink-2);stroke-width:1.3"/>'
    o += t(76, 66, 'TRECHOS DA DECISÃO', size=11, weight=700, fill='var(--ink-2)')
    o += t(76, 107, 'PERGUNTA SOBRE A PROVA', size=12, weight=700, fill='var(--conc)')
    o += line(58, 119, 58, 192, tone='conc', w=3)
    o += '<path d="M75 150H456M75 192H671" style="fill:none;stroke:var(--conc);stroke-width:2;opacity:.45"/>'
    o += t(76, 144, 'Mas, onde está a prova?', size=23, italic=True)
    o += t(76, 186, 'Ou onde isso foi alegado na inicial?', size=23, italic=True)
    o += t(470, 219, '[…]', size=16, anchor='middle', fill='var(--ink-2)', ls='0')
    o += t(76, 263, 'RESULTADO', size=12, weight=700, fill='var(--dif)')
    o += line(58, 276, 58, 310, tone='dif', w=3)
    o += '<path d="M75 310H736" style="fill:none;stroke:var(--dif);stroke-width:2;opacity:.45"/>'
    o += t(76, 302, 'Reconheço a decadência e extingo a ação.', size=23, italic=True)
    o += t(470, 381, 'EXCERTOS · PASSAGENS INTERMEDIÁRIAS OMITIDAS', size=10.5,
           anchor='middle', fill='var(--ink-2)', weight=600)
    return svg('20 8 900 390', o, cls='fig', ident='pci-a16-excerpt',
               label='Dois trechos da decisão: a pergunta sobre a prova das tentativas amigáveis e o resultado que reconhece a decadência e extingue a ação; as bordas e a elipse delimitam a seleção')


if __name__ == '__main__':
    print(panel())
