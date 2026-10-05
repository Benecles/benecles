"""Delito Unidade 01 · seção 3.1: one fact sheet, two normative overlays."""
import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from figkit import Document, line, svg, t

# Claim: the same baby-care fact can take two normative routes and reach two provisional judgments.
FACT = [
    ('title', 'FICHA · O MESMO FATO', 'head'),
    ('party', ('FATO', 'A pessoa abriu a porta e deixou o bebê sozinho por horas.'), 'fact'),
    ('clause', ('FALTAM', 'capacidade concreta de agir · resultado demonstrado'), 'pending'),
]


def panel():
    d = Document('u01-s7', 18, 18, 444, FACT, lead=22, indent=82)
    paper_bottom = d.y + d.h
    split_y = paper_bottom + 34
    norm_y = split_y + 40
    judgment_y = norm_y + 78
    end_y = judgment_y + 84

    # One shared record branches into two readings. The solid and dashed tracks
    # remain visible when the text is removed, so the fork is carried by the drawing.
    o = d.paper() + d.highlight(['pending'], 'mix') + ''.join(d.parts)
    o += line(240, paper_bottom, 240, split_y, w=1.8)
    o += line(28, split_y, 452, split_y, w=1.8)
    o += line(28, split_y, 28, end_y, w=2.2)
    o += line(452, split_y, 452, end_y, tone='muted', w=2.2, dash='5 4')

    # Norm overlays, named by their legal function; no guessed article for the second route.
    o += t(46, norm_y, 'ART. 13, § 2º', size=12, weight=700)
    o += t(46, norm_y + 17, 'dever de garante', size=10.5, fill='var(--ink-2)')
    o += t(434, norm_y, 'TIPO OMISSIVO PRÓPRIO', size=10.8, anchor='end', weight=700)
    o += t(434, norm_y + 17, 'sem dever de garante', size=10.5, anchor='end', fill='var(--ink-2)')
    o += line(46, norm_y + 28, 220, norm_y + 28, tone='ink', w=1.2)
    o += line(260, norm_y + 28, 434, norm_y + 28, tone='muted', w=1.2, dash='5 4')

    # Each overlay ends in its own provisional judgment.
    o += t(46, judgment_y, 'JUÍZO', size=10, weight=700, fill='var(--ink-2)')
    o += t(46, judgment_y + 22, 'resultado pode ser', size=11.5)
    o += t(46, judgment_y + 39, 'imputado: possível', size=11.5)
    o += t(46, judgment_y + 56, 'omissão imprópria', size=11.5, weight=700)
    o += t(434, judgment_y, 'JUÍZO', size=10, anchor='end', weight=700, fill='var(--ink-2)')
    o += t(434, judgment_y + 22, 'resultado não se', size=11.5, anchor='end')
    o += t(434, judgment_y + 39, 'transfere por essa via', size=11.5, anchor='end')
    o += t(434, judgment_y + 56, 'pergunta: omissão', size=10.4, anchor='end', weight=700)
    o += t(434, judgment_y + 73, 'própria', size=10.4, anchor='end', weight=700)

    return svg(f'0 0 480 {end_y + 18}', o, cls='fig', ident='tdl-u01-s7',
               label='Um mesmo fato recebe dois recortes normativos e gera juízos provisórios distintos')


def panels():
    return [panel()]
