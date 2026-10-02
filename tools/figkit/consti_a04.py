"""Constitucional I Aula 04 · Fig. 1 (Modelos de defesa), 3 steps.

The historical layers compare the North American and Austrian models, then read the
Brazilian mixed system beside the statutory clause that assigns the Senate its role.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Strata, statute, svg, t


IDS = ['p-gen0', 'p-gen1', 'p-gen2']
LABELS = ['Modelo norte-americano', 'Modelo austríaco', 'Brasil']


USA = [
    ('Inglaterra · séc. XVII', 'Origem próxima: supremacia de uma lei sobre outra'),
    ('Bonham · 1610', 'Coke: common law controlaria atos do Parlamento; tese recusada'),
    ('Revolução · 1688', 'Depois dela, prevalece a supremacia do Parlamento'),
    ('Colônias · 1776', 'Cartas do Reino dão lugar a Carta ou Lei Fundamental própria'),
    ('EUA · 1803', 'Marbury v. Madison: controle judicial das leis do Congresso'),
    ('Quem controla', 'Todos os juízes · controle difuso'),
    ('Como', 'No processo, decide a questão concreta da controvérsia entre partes'),
]

AUSTRIA = [
    ('Europa · por volta de 1920', 'É quando se firmam os tribunais constitucionais'),
    ('Áustria · década de 1920', 'Modelo austríaco com influência de Kelsen'),
    ('Quem controla', 'Um só órgão · controle concentrado'),
    ('Órgão', 'Tribunal Constitucional, órgão técnico fora do Judiciário'),
    ('Como', 'Abstrato: independe de um caso concreto'),
    ('Objeto', 'A lei em tese'),
    ('Itália · contraste', 'Concentrado, mas incidental: a questão nasce no processo e sobe separada ao Tribunal'),
]

BRASIL = [
    ('Difuso-concreto', 'Continua entre todos os juízes e tribunais'),
    ('Recurso extraordinário', 'O STF também resolve a questão e o caso'),
    ('Efeito no caso', 'Inter partes; pode chegar a todos por resolução do Senado'),
    ('EC 16/1965', 'Controle abstrato, concentrado no STF'),
    ('Efeitos abstratos', 'Erga omnes e vinculante para Judiciário e Administração'),
    ('Depois de 1988', 'Acesso direto ampliado · pluralidade de ações'),
]


def layers(uid, rows, y=64, layer_h=64):
    s = Strata(uid, x=52, y=y, w=496, date_w=132, layer_h=layer_h, gap=2)
    for period, label in rows:
        s.layer(period, label, tone='muted')
    return s.svg()


def panel(k):
    if k == 0:
        o = t(52, 50, 'ORIGEM E TRAÇOS DO MODELO NORTE-AMERICANO', size=10.5,
              caps=True, weight=700, fill='var(--ink-2)')
        o += layers('dci-a04-us', USA)
    elif k == 1:
        o = t(52, 50, 'MODELO AUSTRÍACO · QUEM E COMO CONTROLA', size=10.5,
              caps=True, weight=700, fill='var(--ink-2)')
        o += layers('dci-a04-at', AUSTRIA)
    else:
        o = t(52, 50, 'BRASIL · O MODELO MISTO E O ART. 52, X', size=10.5,
              caps=True, weight=700, fill='var(--ink-2)')
        o += layers('dci-a04-br', BRASIL, y=64, layer_h=52)
        article, _ = statute(
            52, 414, 496, 'Constituição Federal · art. 52, X',
            [('suspender a execução,', True),
             (' no todo ou em parte, de lei declarada inconstitucional por decisão definitiva do Supremo Tribunal Federal;', False)],
            source='Senado Federal', tone='ink')
        o += article
    return svg('36 22 528 528', o, cls='panel fig on' if k == 0 else 'panel fig',
               ident=IDS[k], label=LABELS[k])


def panels():
    return [panel(k) for k in range(3)]
