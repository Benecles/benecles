"""Direito Constitucional I Aula 04 · one cumulative field, three steps."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Field, Timeline, line, statute, svg, t

IDS = ['p-gen0', 'p-gen1', 'p-gen2']
LABELS = ['Modelo norte-americano', 'Modelos austríaco e italiano', 'Brasil: modelo misto']


def historical_strip():
    """Real-proportion chronology, with only the dates supplied by the lesson."""
    tl = Timeline('dci-a04-origens', 82, 518, 100, 1610, 1803, step=1000)
    tl.event(1610, 55, '1610', tone='conc', sub='Bonham · Coke', anchor='start')
    tl.event(1688, 45, 'supremacia do Parlamento', tone='muted', sub='1688', anchor='middle')
    tl.event(1776, 65, 'Carta própria', tone='dif', sub='1776', anchor='end')
    tl.event(1803, 45, '1803', tone='ink', sub='Marbury', anchor='end', mark='dot')
    return tl.svg()


def model_field(k):
    """The shared axes stay still; each step adds real model locations."""
    f = Field(f'dci-a04-modelos-{k}', x0=88, x1=512, y0=165, y1=438)
    f.region(165, 301.5, 'dif', .15)  # abstract, upper half
    f.region(301.5, 438, 'conc', .15)  # concrete/incidental, lower half
    f.axes(
        [(88, ('DIFUSO', 'todos os juízes')),
         (512, ('CONCENTRADO', 'um só órgão'))],
        [(165, ('ABSTRATO', 'em tese')),
         (438, ('CONCRETO', ''))],
        xtitle='Quem controla', ytitle='Como')
    # The cross makes four places legible even after every word is removed.
    f.o.append(line(300, 165, 300, 438, tone='muted', w=1))
    f.o.append(line(88, 301.5, 512, 301.5, tone='muted', w=1))

    if k == 0:
        f.point(190, 365, 'EUA', active=True, tone='conc', dx=13, dy=-4)
    elif k == 1:
        f.point(190, 365, 'EUA', tone='muted', dx=13, dy=-4)
        f.point(415, 220, 'ÁUSTRIA', active=True, tone='conc', dx=-12, dy=-14,
                anchor='end', sub='Kelsen')
        f.point(415, 365, 'ITÁLIA', active=True, tone='dif', dx=-12, dy=20,
                anchor='end', sub='incidental')
    else:
        # Earlier locations remain; the two Brazilian forms arrive in the same field.
        f.point(190, 365, 'EUA', tone='muted', dx=13, dy=-4)
        f.point(415, 220, 'ÁUSTRIA', tone='muted', dx=-12, dy=-14,
                anchor='end', sub='Kelsen')
        f.point(415, 365, 'ITÁLIA', tone='muted', dx=-12, dy=20,
                anchor='end', sub='incidental')
        f.o.append(line(225, 390, 445, 245, tone='mix', w=2.2))
        f.point(225, 390, 'RE', active=True, tone='conc', dx=-12, dy=23,
                anchor='end')
        f.point(445, 245, 'EC 16/1965', active=True, tone='dif', dx=12, dy=-14,
                anchor='start', sub='Depois de 1988')

    o = f.svg()
    o += historical_strip()
    if k == 1:
        o += t(300, 128, 'ÁUSTRIA · DÉCADA DE 1920', size=10.5,
               anchor='middle', caps=True, weight=700, fill='var(--ink-2)')
    if k == 2:
        # The actual constitutional clause is the instrument connecting the concrete RE
        # position to the Senate's power to extend effects beyond the parties.
        o += line(225, 399, 225, 497, tone='conc', w=1.5, dash='3 3')
        article, _ = statute(
            52, 512, 496, 'Constituição Federal · art. 52, X',
            [('suspender a execução,', True),
             (' no todo ou em parte, de lei declarada inconstitucional por decisão definitiva do Supremo Tribunal Federal;', False)],
            source='Senado Federal', tone='conc')
        o += article
    return o


def panel(k):
    return svg('32 0 536 612', model_field(k),
               cls='panel fig on' if k == 0 else 'panel fig',
               ident=IDS[k], label=LABELS[k])


def panels():
    return [panel(k) for k in range(3)]
