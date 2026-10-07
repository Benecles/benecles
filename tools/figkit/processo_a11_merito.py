"""Aula 11-mérito: statutory convergence and the still-open cognitive phase.

All legal labels follow the captured CPC arts. 203 §§1–2 and 356 caput,
I–II and §§1–5 in the Aula 11-mérito compendium. The lengths are schematic;
they assert no quantity, duration, or order beyond the statutory relations.
"""

from figkit import line, svg, t


def _arrow(x, y, tone='ink'):
    """Open continuation, using the kit's line grammar."""
    return (line(x - 11, y - 7, x, y, tone=tone, w=2)
            + line(x - 11, y + 7, x, y, tone=tone, w=2))


def grounds_panel():
    """Art. 356 I–II converge on the caput's bounded object."""
    o = ''
    o += t(42, 48, 'ART. 356  /  DUAS CONDIÇÕES, UM RECORTE', size=14, weight=700)
    o += line(42, 64, 1038, 64, w=1.25)

    # The two alternative grounds are exactly the caput's incisos I–II.
    o += t(42, 111, 'I', size=16, fill='var(--conc)', weight=700)
    o += t(78, 111, 'INCONTROVERSO', size=13, weight=700)
    o += line(42, 130, 460, 130, tone='conc', w=3)
    o += t(42, 224, 'II', size=16, fill='var(--conc)', weight=700)
    o += t(78, 224, 'CONDIÇÕES DE IMEDIATO JULGAMENTO', size=13, weight=700)
    o += t(78, 244, 'nos termos do art. 355', size=11, fill='var(--ink-2)')
    o += line(42, 262, 460, 262, tone='conc', w=3)

    # Either ground reaches the same bounded decision; this is a path, not rows of text.
    o += line(460, 130, 570, 196, tone='conc', w=2.2)
    o += line(460, 262, 570, 196, tone='conc', w=2.2)
    o += line(570, 179, 570, 213, tone='dif', w=4)
    o += line(570, 196, 1008, 196, tone='dif', w=3)
    o += t(613, 177, 'DECISÃO PARCIAL DO MÉRITO', size=14, fill='var(--dif)', weight=700)
    o += t(1008, 225, 'ART. 356, CAPUT', size=10.5, anchor='end', fill='var(--ink-2)', weight=600)

    # The caput can cover whole requests or a portion. Other merits remain outside it.
    o += t(42, 319, 'UM OU MAIS PEDIDOS, OU PARCELA DELES', size=12, weight=700)
    o += line(42, 343, 1008, 343, tone='muted', w=1.3)
    o += line(42, 343, 570, 343, tone='dif', w=5)
    o += line(570, 330, 570, 357, tone='dif', w=2.4)
    o += line(570, 343, 1008, 343, tone='muted', w=2, dash='8 6')
    o += _arrow(1008, 343, tone='muted')
    o += t(42, 377, 'OBJETO DECIDIDO', size=11.5, fill='var(--dif)', weight=700)
    o += t(1008, 377, 'MÉRITO FORA DO OBJETO', size=11.5, anchor='end', fill='var(--ink-2)', weight=700)
    o += t(1008, 396, 'PERMANECE PENDENTE', size=11, anchor='end', fill='var(--ink-2)')
    return svg('24 25 1032 390', o, cls='fig', ident='pci-a11m-grounds',
               label='Artigo 356: o fundamento incontroverso e as condições de imediato julgamento convergem numa decisão parcial do mérito sobre objeto delimitado; o mérito fora dele permanece pendente')


def phase_panel():
    """An art. 356 merits chapter ends while the art. 203 cognitive phase continues."""
    o = ''
    o += t(42, 48, 'ARTS. 203 + 356  /  DUAS EXTENSÕES AO MESMO TEMPO', size=14, weight=700)
    o += line(42, 64, 1038, 64, w=1.25)

    # Art. 203 §1: sentence requires the end of the cognitive phase.
    o += t(42, 105, 'CRITÉRIO DA SENTENÇA · ART. 203, § 1º', size=11, fill='var(--ink-2)', weight=700)
    o += t(42, 125, 'fim da fase cognitiva', size=13, weight=600)
    o += line(42, 154, 1008, 154, tone='ink', w=2)
    o += _arrow(1008, 154)
    o += t(1008, 136, 'FASE COGNITIVA AINDA EM CURSO', size=11, anchor='end', fill='var(--ink-2)', weight=700)

    # At the same position in the proceeding, one object has been resolved.
    o += t(42, 226, 'PEDIDO OU PARCELA DECIDIDA', size=11.5, fill='var(--dif)', weight=700)
    o += line(42, 249, 570, 249, tone='dif', w=5)
    o += line(570, 231, 570, 267, tone='dif', w=3)
    o += t(601, 246, 'MÉRITO RESOLVIDO', size=13, fill='var(--dif)', weight=700)
    o += t(601, 267, 'decisão interlocutória · art. 203, § 2º', size=11, fill='var(--ink-2)')

    # The remaining object stays on an open course, so the phase cannot be over.
    o += t(42, 340, 'MÉRITO FORA DA DECISÃO', size=11.5, fill='var(--conc)', weight=700)
    o += line(42, 362, 1008, 362, tone='conc', w=3)
    o += _arrow(1008, 362, tone='conc')
    o += t(1008, 339, 'CONTINUA', size=11.5, anchor='end', fill='var(--conc)', weight=700)
    return svg('24 25 1032 362', o, cls='fig', ident='pci-a11m-phase',
               label='Artigos 203 e 356: uma parcela do mérito foi resolvida por decisão interlocutória enquanto o mérito restante e a fase cognitiva continuam')


def panels():
    return grounds_panel(), phase_panel()


def specimen_entry():
    a, b = panels()
    return ('<section class="ref" id="specimen-pci-a11m"><header><span class="g">'
            'Percursos · fundamento e fase</span><span class="v">verbo · delimitar</span></header>\n'
            '<h2>Processo · Aula 11-mérito · art. 356</h2>'
            '<p>Os dois fundamentos chegam à decisão sobre um objeto delimitado; '
            'a parcela decidida termina enquanto o restante mantém a fase cognitiva em curso.</p>'
            '<p class="r">novos componentes · pci-a11m-grounds / pci-a11m-phase</p>'
            f'<div class="wide"><div class="s">{a}</div><div class="s" '
            f'style="margin-top:18px">{b}</div></div></section>')


if __name__ == '__main__':
    print('\n'.join(panels()))
