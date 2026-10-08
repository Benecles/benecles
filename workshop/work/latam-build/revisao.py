"""Revisão para a atividade de 05/10. Content: Codex/Luna draft work/latam-prep/drafts/revisao-atividade.md.
Eixos become recall cards (quiz component); comparisons become wide tables; mixed problems take the exam-paper
form: the facts are printed, the worked answer is folded."""
import re
from common import *
from common import _inline

SRC = '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/latam-prep/drafts/revisao-atividade.md'
md = open(SRC).read()

def split(text, level):
    """[(title, body)] for headings of exactly `level` #s."""
    parts = re.split(rf'^{"#" * level} (.+)$', text, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts), 2)]

def paras(body):
    return [p.strip().replace('\n', ' ') for p in re.split(r'\n\s*\n', body) if p.strip() and not p.strip().startswith('|')]

def mdtable(body):
    rows = [r.strip() for r in body.split('\n') if r.strip().startswith('|')]
    cells = [[c.strip() for c in r.strip('|').split('|')] for r in rows if not re.match(r'^\|[\s\-|:]+\|$', r)]
    head, rest = cells[0], cells[1:]
    return table([_inline(h) for h in head], [[_inline(c) for c in r] for r in rest])

top = dict(split(md, 2))
eixos = split(top['Oito eixos, oito respostas'], 3)
comps = split(top['Três comparações'], 3)
probs = split(top['Problemas mistos'], 3)

EXTRA = ('.prob{max-width:1180px;margin:0 auto 22px;padding:0 clamp(16px,4vw,48px)}'
         '.prob>div{max-width:72ch;border:1.5px solid var(--ink);background:var(--paper);box-shadow:5px 5px 0 var(--grid-major);padding:18px 22px}'
         '.prob h3{font:700 20px/1.25 var(--sans);margin:4px 0 10px}.prob .n{font:600 11px var(--mono);letter-spacing:.1em;color:var(--conc)}'
         '.prob p{font-size:18px;line-height:1.6;margin:0 0 .8em}.prob details{border-top:1.5px dashed var(--ink);margin-top:12px;padding-top:10px}'
         '.prob summary{cursor:pointer;font:600 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dif)}'
         '.prob details[open] summary{margin-bottom:10px}')

# hero: the six class dates, like an exam paper's syllabus strip
DATES = [(120, '17/08', 'Aulas 01–02', 'constituições e cortes'), (280, '24/08', 'Aulas 03–04', 'justiça de transição'),
         (440, '31/08', 'Aulas 05–06', 'soberania popular'), (600, '14/09', 'Aula 07', 'estado de coisas'),
         (760, '21/09', 'Aula 08', 'litígio estrutural'), (920, '28/09', 'Aula 09', 'saúde e diálogo')]
hero = '<path class="draw" d="M60 70H1020" style="fill:none;stroke:var(--ink);stroke-width:3"/>'
for i, (x, d, a, t) in enumerate(DATES):
    hero += (f'<g class="pop" style="--d:{.2 + i * .15:.2f}s;font:12px var(--mono);letter-spacing:1px">'
             f'<circle cx="{x}" cy="70" r="7" style="fill:var(--conc)"/>'
             f'<text x="{x}" y="46" text-anchor="middle" style="fill:var(--conc)">{d}</text>'
             f'<text x="{x}" y="100" text-anchor="middle" style="fill:var(--ink)">{a}</text>'
             f'<text x="{x}" y="118" text-anchor="middle" style="fill:var(--ink-2);font-size:11px">{t}</text></g>')
hero += '<text x="1020" y="160" text-anchor="end" style="font:600 13px var(--mono);letter-spacing:.12em;fill:var(--dif)">ATIVIDADE · 05/10</text>'

b = ''
b += chapter('01', 'c1', 'Oito eixos, oito respostas', 'Cada aula tinha uma pergunta de discussão. Tente responder de cabeça antes de abrir.', 'dif')
b += quiz([(_inline(re.sub(r'^\d+\.\s*', '', t)), ' '.join(_inline(p) for p in paras(body))) for t, body in eixos])
b += chapter('02', 'c2', 'Três comparações', 'Os casos lado a lado, pelas perguntas que a atividade costuma cruzar.')
for t, body in comps:
    b += longform(f'<h3>{_inline(t)}</h3>')
    b += wide(mdtable(body))
b += chapter('03', 'c3', 'Problemas mistos', 'Fatos novos que exigem juntar duas ou mais aulas. Escreva sua resposta, depois compare com a resolução.', 'dif')
for i, (t, body) in enumerate(probs):
    ps = paras(body)
    facts = [p for p in ps if not p.startswith('**Resposta')]
    ans = [p for p in ps if p.startswith('**Resposta')]
    title = re.sub(r'^\d+\.\s*', '', t)
    ans_html = ''.join('<p>' + _inline(re.sub(r'^\*\*Resposta trabalhada\.\*\*\s*', '', p)) + '</p>' for p in ans)
    b += (f'<div class="prob"><div><span class="n">PROBLEMA {i + 1:02d}</span><h3>{_inline(title)}</h3>'
          + ''.join('<p>' + _inline(p) + '</p>' for p in facts)
          + f'<details><summary>Resolução</summary>{ans_html}</details></div></div>\n')

kit.FIGN[0] = 0
page('revisao-atividade.html', 'R', 'Revisão para a atividade',
     'Revisão para a atividade avaliativa de 05/10 de Direito Latino-americano: os oito eixos de discussão com respostas, três quadros comparativos e dez problemas mistos resolvidos.',
     KICK, 'Revisão para', 'a atividade',
     'Seis aulas, oito perguntas, dez problemas. Responda primeiro, <strong class="dif">abra depois</strong>: o que você não souber dizer sem olhar é o que falta estudar.',
     hero, [('Atividade', '05/10'), ('Aulas', '01 a 09'), ('Eixos', '8'), ('Problemas', '10')], b,
     ('aula-09.html', '← Aula 09', 'Saúde e diálogo institucional'), ('cartoes.html', 'Cartões →', 'Revisão espaçada'),
     extra_css=EXTRA + EXTRA_CSS, toplabel='Revisão · 05/10')
