"""Metodologia figures (Claude, 29/09). Aula 01: the glossed page, the literal object of medieval legal study."""
import kit
from kit import T
from figs import FIGS, S, src

def _lines(x0, x1, y0, n, gap, style, jag=True):
    o = ''
    for i in range(n):
        x_end = x1 - (18 if jag and i % 3 == 2 else 0)
        o += f'<path d="M{x0} {y0 + i * gap}H{x_end}" style="{style}"/>'
    return o

INK = 'fill:none;stroke:var(--ink);stroke-width:2.2;stroke-linecap:round'
GLOSS = 'fill:none;stroke:var(--conc);stroke-width:1.1;stroke-linecap:round'
FAINT = 'fill:none;stroke:var(--ink-2);stroke-width:1.6;stroke-linecap:round;opacity:.45'

def _page(k):
    """k = 0 text alone, 1 glossed, 2 commentary beside the page."""
    o = T(30, 38, 'COMO SE ESTUDAVA O DIREITO EM BOLONHA', 't-small', style='letter-spacing:.1em')
    if k < 2:
        px, pw, py, ph = 150, 300, 70, 450
        o += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>'
        o += _lines(215, 385, 150, 14, 20, INK)                               # the Roman text, central column
        o += T(300, 128, 'DIGESTO', 't-small', anchor='middle', style='letter-spacing:.14em;fill:var(--ink-2)')
        if k == 0:
            o += f'<path d="M455 250H500" style="fill:none;stroke:var(--ink-2);stroke-width:1"/>'
            o += T(506, 246, 'o texto', 't-small') + T(506, 262, 'de autoridade', 't-small')
            o += T(300, 560, 'Irnério ensina o direito justinianeu em Bolonha (séc. XII).', 't-small', anchor='middle', style='font-size:12.5px')
        else:
            o += _lines(222, 370, 160, 13, 20, GLOSS, jag=False)             # interlinear glosses
            for gx in (162, 400):                                            # marginal glosses, both margins
                o += _lines(gx, gx + 38, 96, 20, 20, GLOSS, jag=False)
            o += f'<path d="M438 176H500" style="fill:none;stroke:var(--conc);stroke-width:1"/>'
            o += T(506, 172, 'glosa', 't-small tc-conc') + T(506, 188, 'marginal', 't-small tc-conc')
            o += f'<path d="M300 170L262 58" style="fill:none;stroke:var(--conc);stroke-width:1"/>'
            o += T(150, 54, 'glosa entre as linhas', 't-small tc-conc')
            o += T(300, 560, 'Acúrsio reúne as glosas na Magna Glosa (c. 1230–1240).', 't-small', anchor='middle', style='font-size:12.5px')
    else:
        o += f'<rect x="36" y="110" width="200" height="300" style="fill:var(--paper-2);stroke:var(--ink-2);stroke-width:1.2"/>'
        o += _lines(78, 194, 160, 10, 20, FAINT) + T(136, 140, 'DIGESTO E GLOSA', 't-small', anchor='middle', style='letter-spacing:.1em;fill:var(--ink-2)')
        o += f'<rect x="276" y="80" width="290" height="420" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>'
        o += T(421, 110, 'COMENTÁRIO', 't-small', anchor='middle', style='letter-spacing:.14em;fill:var(--dif)')
        rows = [('o texto romano', 'a regra geral do direito comum'), ('o estatuto da cidade', 'onde incide, e o que exclui'),
                ('letra × espírito', 'documento também por procurador'), ('a solução', 'que preserva a coerência do todo')]
        for i, (h, sub) in enumerate(rows):
            y = 142 + i * 88
            o += f'<path d="M296 {y}V{y + 58}" style="fill:none;stroke:var(--dif);stroke-width:3"/>'
            o += T(310, y + 20, h, 't-mid', style='font-size:17px') + T(310, y + 44, sub, 't-small', style='font-size:12px;fill:var(--ink-2)')
        o += f'<path d="M236 260C256 260 256 186 290 186" style="fill:none;stroke:var(--dif);stroke-width:1.4;stroke-dasharray:4 4"/>'
        o += T(300, 560, 'Cino de Pistóia, Bártolo e Baldo (a partir do fim do séc. XIII).', 't-small', anchor='middle', style='font-size:12.5px')
    return o

def fig_mj01():
    ref = 'draft lesson-01 "O que separa o glosador do comentador?"'
    return kit.scrolly('Do texto à glosa, da glosa ao comentário', [
        ('p-mj0', _page(0), 'O texto'), ('p-mj1', _page(1), 'A glosa'), ('p-mj2', _page(2), 'O comentário')], [
        S('p-mj0', 'O ponto de partida', 'O texto de autoridade',
          '<p>Na primeira metade do século XII, Irnério começa a ensinar o direito justinianeu em Bolonha. A escola parte da autoridade do <strong>Corpus Iuris</strong>: o texto romano não se troca, se esclarece.</p>' + src(ref), 'dif'),
        S('p-mj1', 'Glosadores', 'Esclarecer palavra por palavra',
          '<p>A <strong>glosa</strong> explica brevemente uma palavra ou passagem obscura, anotada <strong>entre as linhas</strong> ou <strong>à margem</strong>. O trabalho fica preso ao texto e às suas relações com outros trechos. Acúrsio reúne boa parte dessa produção na Magna Glosa, por volta de 1230–1240.</p>' + src(ref), 'conc'),
        S('p-mj2', 'Comentadores', 'Resolver o caso com o texto e o estatuto',
          '<p>Os <strong>comentadores</strong>, de Cino de Pistóia a Bártolo e Baldo, trabalham com materiais mais amplos e com finalidade prática: perguntam onde o estatuto local incide, como se relaciona à regra geral e que solução preserva a coerência do conjunto. Podem contrapor a letra ao espírito: se a regra menciona a apresentação de documento, Bártolo a admite também por procurador.</p>' + src(ref), 'dif'),
    ])

FIGS[('metodologia', 'aula-01.html')] = {3: fig_mj01}
