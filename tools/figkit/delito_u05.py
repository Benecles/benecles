"""Delito Unidade 05 · Fig. 1 (Da representação à consequência), 3 steps, drawn as a decision path."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Path, svg, t, line

STEPS = ['Localize o erro', 'Essencial ou acidental?', 'Inevitável ou evitável?']


def panel(k):
    p = Path(f'u05-{k}')
    p.question(96, ['O que o agente', 'representou mal?'], 'a proibição', 'Erro de proibição',
               ['o fato era conhecido;', 'outra análise · art. 21'], tone='mix', go='um elemento do tipo',
               active=k == 0, next_y=256)
    p.question(256, ['O dado é principal', 'no tipo?'], 'não', 'Erro acidental',
               ['objeto, pessoa, execução,', 'curso causal: o dolo segue'], tone='dif', go='sim · essencial',
               active=k == 1, next_y=416)
    p.question(416, ['Era evitável?'], 'inevitável', 'Exclui dolo e culpa',
               ['faltava previsibilidade'], tone='dif', go='evitável', active=k == 2, next_y=None)
    o = p.svg()
    a = k == 2
    o += line(232, 425, 232, 512, w=2.2 if a else 1.4) + line(232, 512, 322, 512, tone='conc' if a else 'muted', w=2 if a else 1.2)
    o += t(218, 452, 'evitável', size=10.5, anchor='end', weight=700 if a else 500, fill='var(--ink)' if a else 'var(--ink-2)')
    c, h = p.card(330, 488, 240, 'Exclui o dolo · art. 20', ['culpa só se a lei prevê', 'a forma culposa'], 'conc', a)
    o += c
    if a:  # the lesson's own case runs the whole path
        o += f'<rect x="18" y="470" width="200" height="104" style="fill:var(--paper);stroke:var(--mix);stroke-width:1.4;stroke-dasharray:4 3"/>'
        for i, (s, b) in enumerate([('caso · o casaco', True), ('A leva um casaco que', False), ('pensa ser seu: erra sobre', False),
                                    ('"coisa alheia" (essencial).', False), ('Furto não tem forma', False), ('culposa: fato atípico.', True)]):
            o += t(30, 488 + 15 * i, s, size=10.5 if not b else 10.5, weight=700 if b else 500, caps=(i == 0), fill='var(--mix)' if b else 'var(--ink)')
    return svg('0 0 600 600', o, cls='panel fig on' if k == 0 else 'panel fig', ident=f'u05-sp-{k}', label=STEPS[k])


def panels():
    return [panel(k) for k in range(3)]
