"""Controle Aula 27 · Plenário virtual as a procedural clock (replaces ctl-a27-s11)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Clock, svg, t

DAYS = [('sex', 'D1', True), ('sáb', '', False), ('dom', '', False), ('seg', 'D2', True),
        ('ter', 'D3', True), ('qua', 'D4', True), ('qui', 'D5', True), ('sex', 'D6', True)]


def panel():
    c = Clock('a27', 132, 570, 40, DAYS, pre=(88, '−48 h'))
    c.header(560)
    o = t(42, 112, 'pedido de', size=10, fill='var(--conc)') + t(42, 125, 'sustentação', size=10, fill='var(--conc)') + t(42, 138, 'oral ou de', size=10, fill='var(--conc)') + t(42, 151, 'destaque', size=10, fill='var(--conc)') + t(42, 164, 'pela parte', size=10, fill='var(--conc)')
    # 1 · sem incidente: 11 votos entram na janela
    c.lane(140, 'Sem incidente', 'janela de 6 dias úteis')
    c.votes(140, [0, 0, 3, 3, 4, 4, 5, 6, 6, 7, 7])
    c.event(140, 7, 'resultado', anchor='end')
    # 2 · vista
    c.lane(250, 'Pedido de vista', 'devolução em 90 dias corridos →')
    c.votes(250, [0, 0, 3, 4])
    c.event(250, 5, 'vista', 'suspende, não fecha a votação', tone='mix', anchor='end')
    c.run(250, 5, 570, '')
    # 3 · destaque
    c.lane(370, 'Destaque de ministro', 'a janela segue aberta: ainda entram votos')
    c.votes(370, [0, 0, 3])
    c.votes(370, [5, 6, 7], tone='muted')
    c.event(370, 4, 'destaque', 'reinicia no presencial', tone='conc', anchor='end')
    # 4 · silêncio
    c.lane(480, 'Ministro que não vota')
    c.votes(480, [0, 0, 3, 3, 4, 5, 6, 6, 7, 7], hollow=[7])
    o2 = t(570, 506, 'silêncio não é adesão ao relator', size=10.5, anchor='end', weight=700, fill='var(--conc)')
    return svg('0 0 600 600', c.svg() + o + o2, cls='panel fig on', ident='p-a27-relogio', label='Plenário virtual: a janela e seus incidentes')
