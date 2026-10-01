"""Metodologia Jurídica · Aula 04 · III Concílio de Lima: provisão paroquial."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from figkit import Document, svg


LINES = [
    ('title', 'Síntese da aula', 'title'),
    ('party', ('Fonte', 'III Concílio de Lima'), 'source'),
    ('clause', ('Atendimento', 'Paróquias indígenas com atendimento suficiente.'), 'attendance'),
    ('clause', ('Prover pároco', 'Povoado com trezentos indígenas (ou mesmo duzentos).'), 'threshold'),
    ('clause', ('Se não atingido',
               'O prelado reuniria comunidades onde pudessem ser governadas com comodidade.'), 'grouping'),
    ('clause', ('Efeito', 'Organização territorial e distribuição de ministros.'), 'effect'),
]


def panel():
    x, y, w = 70, 34, 460
    d = Document('met-a04-s4', x, y, w, LINES, lead=19, indent=148)
    inner = d.paper()
    inner += d.highlight(['threshold'], 'dif')
    inner += d.highlight(['grouping'], 'conc')
    inner += ''.join(d.parts)
    view = f'{x - 16} {y - 16} {w + 32} {d.h + 32}'
    out = svg(view, inner, cls='fig', ident='met-a04-s4',
              label='Síntese da aula sobre a provisão paroquial no III Concílio de Lima.')
    # This was a standalone responsive SVG, not a fixed scrolly panel.
    return out.replace(f'viewBox="{view}"',
                       f'viewBox="{view}" style="display:block;width:100%;height:auto"')
