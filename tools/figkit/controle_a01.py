"""Controle Aula 01 (A Constituição como régua): hero + Figs. 1–3, drawn with the figure kit."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Ruler, svg, t, WARN

REUNIAO = dict(stops=['livre', ('pacífica,', 'sem armas'), ('aviso', 'prévio'), 'autorização', 'proibição'],
               title='Quanto a lei pode exigir de uma reunião?', source='CF · art. 5º, XVI', limit=2)
LEI_A = (('Lei A', 'exige aviso 48 h antes'), 2)
LEI_B = (('Lei B', 'exige autorização do prefeito'), 3)


def hero():
    r = Ruler('h01', 40, 44, 1000, **REUNIAO)
    o = f'<defs>{r.defs()}</defs>' + r.body()
    o += r.strip(164, LEI_A[1], LEI_A[0], d=.4)
    o += r.strip(224, LEI_B[1], LEI_B[0], d=.9)
    o += r.limit_mark(250, 'limite', 'independe de autorização', d=1.3)
    return svg('0 0 1080 258', o, cls='hero-fork figkit')


def fig1():
    r = Ruler('f101', 40, 120, 520, **REUNIAO)
    o = f'<defs>{r.defs()}</defs>'
    o += t(40, 100, 'Parâmetro · a norma que mede', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    o += r.body()
    o += t(40, 318, 'Objeto · o ato medido', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    o += r.strip(372, LEI_A[1], LEI_A[0], note='cabe na régua', d=.2)
    o += r.limit_mark(400, 'limite', 'independe de autorização')
    return svg('0 0 600 600', o, cls='panel fig on', ident='p-piramide', label='A relação vertical')


def fig2():
    r = Ruler('f201', 40, 120, 520, **REUNIAO)
    o = f'<defs>{r.defs()}</defs>' + r.body()
    o += r.strip(310, LEI_A[1], LEI_A[0], note='compatível · válida', d=.2)
    o += r.strip(410, LEI_B[1], LEI_B[0], note='incompatível · vício', d=.6)
    o += r.limit_mark(450, 'limite', 'independe de autorização', d=1)
    return svg('0 0 600 600', o, cls='panel fig', ident='p-contraste', label='Conformidade ou incompatibilidade')


def fig3():
    stops = ['ninguém', ('devedor de', 'alimentos'), ('depositário', 'infiel'), ('qualquer', 'devedor')]
    lei = (('CC, art. 652', 'prende o depositário'), 2)
    cf = Ruler('f301', 30, 70, 540, stops, title='Quem pode ser preso por dívida?', source='CF · art. 5º, LXVII', limit=2)
    pacto = Ruler('f302', 30, 330, 540, stops, title='Quem pode ser preso por dívida?', source='Pacto de San José · 7.7', limit=1)
    o = f'<defs>{cf.defs()}{pacto.defs()}</defs>'
    o += t(30, 52, 'Constitucionalidade', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    o += cf.body() + cf.strip(214, lei[1], lei[0], note='cabe na Constituição', d=.2)
    o += t(30, 312, 'Convencionalidade · tratado supralegal', size=10.5, caps=True, weight=700, fill='var(--ink-2)')
    o += pacto.body() + pacto.strip(474, lei[1], lei[0], note='não cabe no tratado', d=.6)
    o += pacto.limit_mark(500, 'limite', 'só alimentos', d=1)
    return svg('0 0 600 600', o, cls='panel fig', ident='p-parametro', label='Qual é o parâmetro?')


if __name__ == '__main__':
    root = os.path.join(os.path.dirname(__file__), '..', '..')
    page = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kit de figuras · amostra</title>
<link rel="stylesheet" href="../courses/controle-de-constitucionalidade/assets/controle.css">
<style>body{{max-width:1180px;margin:0 auto;padding:24px 16px}} .s{{border:1.5px solid var(--ink);background:var(--paper);margin:18px 0;padding:8px}}
.row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:18px}} .s svg{{display:block;width:100%;height:auto;opacity:1!important;visibility:visible!important;position:static!important}}
.cap{{font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);margin:4px 2px}}</style></head><body>
<div class="cap">Abertura · Aula 01</div><div class="s">{hero()}</div>
<div class="row"><div><div class="cap">Fig. 1 · A relação vertical</div><div class="s">{fig1()}</div></div>
<div><div class="cap">Fig. 2 · Conformidade ou incompatibilidade</div><div class="s">{fig2()}</div></div>
<div><div class="cap">Fig. 3 · Qual é o parâmetro?</div><div class="s">{fig3()}</div></div></div></body></html>'''
    out = os.path.join(root, 'specimen', 'figkit-controle-a01.html')
    open(out, 'w').write(page)
    print(out); print('\n'.join(WARN) or 'no text warnings')
