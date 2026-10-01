"""Delito Unidade 04 · Fig. 1 (Dolo e culpa: representação e vontade), five steps, drawn with the Field."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Field, svg

X = [(270, ('não prevê', 'podia prever')), (400, ('prevê como', 'possível')), (520, ('prevê como', 'certo'))]
Y = [(140, ('quer', 'como fim')), (240, ('aceita', 'o resultado')), (340, ('confia que', 'não ocorre')), (430, ('nem chega', 'a prever'))]
STEPS = ['Dolo direto de primeiro grau', 'Dolo direto de segundo grau', 'Dolo eventual', 'Culpa consciente', 'Culpa inconsciente']


def panel(k):
    f = Field(f'u04-{k}')
    f.region(100, 290, 'conc', .35)
    f.region(290, 470, 'dif', .35)
    f.axes(X, Y, xtitle='Representação do resultado', ytitle='Atitude')
    f.border(290, 'dolo · art. 18, I', 'culpa · art. 18, II')
    f.bar(400, 520, 140, 'Dolo direto · 1º grau', active=k == 0, tone='conc', sub='o resultado é o fim')
    f.point(520, 240, '2º grau', active=k == 1, tone='conc', dx=8, dy=26, anchor='end', sub='efeito colateral certo')
    f.point(400, 240, 'Dolo eventual', active=k == 2, tone='conc', dx=-14, anchor='end', sub='aceita o possível')
    f.point(400, 340, 'Culpa consciente', active=k == 3, tone='dif', dx=-14, anchor='end', sub='confia que não ocorre')
    f.point(270, 430, 'Culpa inconsciente', active=k == 4, tone='dif', dx=14, sub='podia prever, não previu')
    if k in (2, 3):  # the frontier the lesson's Caso 4 sits on
        f.range(400, 252, 328, 'caso 4 · trânsito', 'a prova decide o lado')
    cls = 'panel fig on' if k == 0 else 'panel fig'
    return svg('0 0 600 600', f.svg(), cls=cls, ident=f'u04-sp-{k}', label=STEPS[k])


def panels():
    return [panel(k) for k in range(5)]
