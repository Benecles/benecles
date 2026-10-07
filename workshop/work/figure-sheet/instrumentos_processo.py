#!/usr/bin/env python3
"""Reference instruments for Processo (CEO specimen, 07/10): generated, so every date and position is exact.
Writes specimen/instrumentos.html in the site repo given as argv[1]."""
import sys, pathlib, datetime as dt
SITE = pathlib.Path(sys.argv[1]).expanduser()
head = (SITE / 'specimen/casa.html').read_text().split('<style>')[0]
head = head.replace('A casa, junta · espécime', 'Instrumentos de processo · espécime')

# ---------- 1. calendar ----------
D = dt.date
hol = {D(2015,4,3): 'Sexta-feira Santa', D(2015,4,21): 'Tiradentes', D(2015,5,1): 'Dia do Trabalho'}
disp, pub = D(2015,4,1), D(2015,4,2)
count, d, n = {}, pub, 0
while n < 15:
    d += dt.timedelta(1)
    if d.weekday() < 5 and d not in hol: n += 1; count[d] = n
end = d
start = D(2015,3,30)
X0, Y0, CW, CH = 40, 92, 132, 84
s = [f'<svg viewBox="0 0 1080 610" role="img" aria-label="Calendário de abril de 2015 com a contagem de 15 dias úteis, de 6 a 27 de abril">']
s.append('<style>.c-n{font:500 15px var(--mono);fill:var(--ink)}.c-dim{fill:var(--muted)}.c-k{font:500 11px var(--mono);letter-spacing:.08em;fill:var(--ink-2)}.c-t{font:500 13px var(--mono);fill:var(--dif)}.c-l{font:italic 400 15px var(--serif);fill:var(--ink)}</style>')
s.append('<defs><pattern id="ip-hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" style="stroke:var(--conc);stroke-width:2;opacity:.45"/></pattern></defs>')
s.append(f'<text x="{X0}" y="34" class="c-k">Abril de 2015 · prazo de 15 dias (CPC, art. 1.003, § 5º), só em dias úteis (art. 219)</text>')
for i, w in enumerate(['seg','ter','qua','qui','sex','sáb','dom']):
    s.append(f'<text x="{X0+i*CW+10}" y="{Y0-14}" class="c-k">{w}</text>')
for k in range(35):
    day = start + dt.timedelta(k); r, c = divmod(k, 7)
    x, y = X0 + c*CW, Y0 + r*CH
    other = day.month != 4
    wk = day.weekday() >= 5
    fill = 'var(--paper-2)' if (wk or other) else 'var(--paper)'
    s.append(f'<rect x="{x}" y="{y}" width="{CW-6}" height="{CH-6}" style="fill:{fill};stroke:var(--grid-major);stroke-width:1"/>')
    if day in hol: s.append(f'<rect x="{x}" y="{y}" width="{CW-6}" height="{CH-6}" style="fill:url(#ip-hatch)"/>')
    cls = 'c-n c-dim' if (other or wk) else 'c-n'
    s.append(f'<text x="{x+10}" y="{y+22}" class="{cls}">{day.day:02d}</text>')
    if day in hol:
        w = hol[day].split(' ', 1) if len(hol[day]) > 13 else [hol[day]]
        for j, part in enumerate(w): s.append(f'<text x="{x+10}" y="{y+CH-16-(len(w)-1-j)*14}" class="c-k" style="fill:var(--conc)">{part}</text>')
    if day in count:
        last = day == end
        col = 'var(--conc)' if last else 'var(--dif)'
        s.append(f'<circle cx="{x+CW-30}" cy="{y+CH/2-3}" r="17" style="fill:{"var(--conc)" if last else "none"};stroke:{col};stroke-width:2"/>')
        s.append(f'<text x="{x+CW-30}" y="{y+CH/2+2}" text-anchor="middle" class="c-t" style="fill:{"var(--paper)" if last else col}">{count[day]}</text>')
    if day == disp: s.append(f'<text x="{x+10}" y="{y+CH-16}" class="c-k">disponibilizada</text>')
    if day == pub: s.append(f'<text x="{x+10}" y="{y+CH-16}" class="c-k">publicada</text>')
# legend rail under the grid
ly = Y0 + 5*CH + 22
s.append(f'<line x1="{X0}" y1="{ly}" x2="{X0+7*CW-6}" y2="{ly}" style="stroke:var(--ink);stroke-width:1.5"/>')
steps = [('01/04', 'o DJE disponibiliza'), ('02/04', 'publicada (art. 224, § 2º)'), ('06/04', 'começa a contar (§ 3º)'), ('27/04', 'último dia')]
for i, (a, b) in enumerate(steps):
    x = X0 + i*(7*CW-6)/4
    col = 'var(--conc)' if i == 3 else 'var(--ink)'
    s.append(f'<circle cx="{x+6}" cy="{ly}" r="5" style="fill:{col}"/>')
    s.append(f'<text x="{x}" y="{ly+26}" class="c-n" style="fill:{col}">{a}</text><text x="{x}" y="{ly+46}" class="c-l">{b}</text>')
s.append('</svg>')
cal = '\n'.join(s)

# ---------- 2. seating chart ----------
t = ['<svg viewBox="0 0 1080 600" role="img" aria-label="Quadro do litisconsórcio: necessário ou facultativo, simples ou unitário, com o caso Valter e o restaurante na casa simples e facultativo">']
t.append('<style>.q-k{font:500 11px var(--mono);letter-spacing:.08em;fill:var(--ink-2)}.q-h{font:750 22px var(--sans);fill:var(--ink)}.q-q{font:italic 400 16px var(--serif);fill:var(--ink-2)}.q-c{font:500 14px var(--mono);fill:var(--ink)}.q-s{font:400 15px var(--serif);fill:var(--ink)}</style>')
GX, GY, GW, GH = 230, 110, 400, 210
t.append(f'<text x="{GX}" y="40" class="q-k">art. 116 · o juiz terá de decidir o mérito de modo uniforme para todos?</text>')
t.append(f'<text x="{GX+GW/2}" y="80" text-anchor="middle" class="q-h">simples</text><text x="{GX+GW*1.5}" y="80" text-anchor="middle" class="q-h">unitário</text>')
t.append(f'<text x="{GX+GW/2}" y="98" text-anchor="middle" class="q-q">não: cada um pode ter sua sorte</text><text x="{GX+GW*1.5}" y="98" text-anchor="middle" class="q-q">sim: uma decisão para todos</text>')
t.append(f'<text transform="translate(36 {GY+GH}) rotate(-90)" text-anchor="middle" class="q-k">art. 114 · a sentença depende da citação de todos?</text>')
t.append(f'<text x="{GX-18}" y="{GY+GH/2}" text-anchor="end" class="q-h">facultativo</text><text x="{GX-18}" y="{GY+GH/2+20}" text-anchor="end" class="q-q">não: reunir é escolha</text>')
t.append(f'<text x="{GX-18}" y="{GY+GH*1.5}" text-anchor="end" class="q-h">necessário</text><text x="{GX-18}" y="{GY+GH*1.5+20}" text-anchor="end" class="q-q">sim: falta alguém, falha</text>')
for r in range(2):
    for c in range(2):
        t.append(f'<rect x="{GX+c*GW}" y="{GY+r*GH}" width="{GW-8}" height="{GH-8}" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>')
# the exam case, seated
cx, cy = GX + 26, GY + 30
t.append(f'<text x="{cx}" y="{cy}" class="q-k" style="fill:var(--dif)">2015/1 · questão 3 · polo passivo</text>')
for i, nm in enumerate(['VALTER', 'OS GALOS PRIMOS LTDA.']):
    t.append(f'<rect x="{cx}" y="{cy+16+i*44}" width="{220 if i else 120}" height="32" style="fill:none;stroke:var(--dif);stroke-width:2"/><text x="{cx+12}" y="{cy+37+i*44}" class="q-c" style="fill:var(--dif)">{nm}</text>')
t.append(f'<text x="{cx}" y="{cy+128}" class="q-s">chef e restaurante podem ter sortes diferentes,</text><text x="{cx}" y="{cy+148}" class="q-s">e Gustavo podia ter processado só um deles</text>')
# the trap: alternative c seats the hypothetical active pole in unitário
ax, ay = GX + GW + 26, GY + 30
t.append(f'<text x="{ax}" y="{ay}" class="q-k" style="fill:var(--conc)">a alternativa c sentou aqui · erro</text>')
for i, nm in enumerate(['GUSTAVO', 'MAIQUE']):
    t.append(f'<rect x="{ax}" y="{ay+16+i*44}" width="130" height="32" style="fill:none;stroke:var(--conc);stroke-width:2;stroke-dasharray:6 5"/><text x="{ax+12}" y="{ay+37+i*44}" class="q-c" style="fill:var(--conc)">{nm}</text>')
t.append(f'<path d="M{ax-8} {ay+48} C {ax-120} {ay+20}, {cx+250} {ay+60}, {cx+232} {ay+60}" style="fill:none;stroke:var(--conc);stroke-width:1.5;stroke-dasharray:4 4"/>')
t.append(f'<text x="{ax}" y="{ay+128}" class="q-s">cada cliente sofreu o seu dano moral:</text><text x="{ax}" y="{ay+148}" class="q-s">juntos no polo ativo, o litisconsórcio seria simples</text>')
t.append(f'<text x="{GX}" y="{GY+2*GH+30}" class="q-k">duas perguntas independentes: necessário não implica unitário (2015/1, questão 8, alternativa d)</text>')
t.append('</svg>')
seat = '\n'.join(t)

css = '''<style>
.ip-col{width:min(1083px,calc(100vw - 96px));margin:26px auto 0}
.ip-col p{font-size:19px;line-height:1.62;margin:0 0 1em}
.ip-fig{width:min(1083px,calc(100vw - 96px));margin:30px auto;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);padding:18px 18px 12px}
.ip-fig svg{display:block;width:100%;height:auto}
.ip-fig figcaption{margin-top:10px;font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.ip-why{width:min(1083px,calc(100vw - 96px));margin:0 auto 46px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.ip-why div{border-top:3px solid var(--ink);padding-top:8px;font:400 16px/1.45 var(--serif)}
.ip-why b{display:block;font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2);margin-bottom:4px}
@media(max-width:1099px) and (orientation:portrait){.ip-col,.ip-fig,.ip-why{width:calc(100vw - 32px)}}
</style>'''
body = f'''</head>
<body class="casa">
<nav class="topbar"><a href="../index.html">← Ordenações</a><span>Espécime · instrumentos de processo</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero"><div class="kicker label"><span>Espécime</span><span>Processo Civil</span><span>07/10</span></div>
<h1><span class="split">Instrumentos,</span><span class="split">não caixas</span></h1></header>
<div class="ip-col"><p>Processo parece texto puro, mas cada instituto vive num objeto: o calendário em que o prazo corre, o polo em que as partes sentam, os autos em que o ato fica. A figura desenha o objeto com os fatos de uma prova real; a regra entra como a pergunta que o objeto responde.</p></div>
<figure class="ip-fig">{cal}<figcaption>Fig. A · O prazo contado no calendário de verdade: a decisão do caso da prova 2015/1, disponibilizada no DJE em 01/04/2015</figcaption></figure>
<div class="ip-why"><div><b>O objeto</b>Um mês real, com os feriados que o leitor esqueceria (Sexta-feira Santa, Tiradentes). Os fins de semana ficam apagados sozinhos.</div><div><b>A regra</b>Três artigos viram três marcos na régua: disponibilizada, publicada, começa. Nenhum precisa ser repetido no texto.</div><div><b>O que o leitor faz</b>Conta junto, aponta o dia 27 e sabe por que não é o dia 23. Troque a data de disponibilização e o exercício está pronto.</div></div>
<figure class="ip-fig">{seat}<figcaption>Fig. B · O quadro do litisconsórcio: duas perguntas, quatro lugares, as partes da prova sentadas onde a resposta conferida as põe</figcaption></figure>
<div class="ip-why"><div><b>O objeto</b>Um mapa de assentos. Os eixos são as perguntas literais dos arts. 114 e 116, não rótulos.</div><div><b>A regra</b>As duas perguntas são independentes: o quadro mostra isso sem dizer, porque as quatro casas existem.</div><div><b>O que o leitor faz</b>Senta as partes de cada caso. A armadilha da prova (a alternativa c) aparece tracejada em laranja, sentada no lugar errado.</div></div>
<div class="ip-col"><p class="label" style="font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)">Para quem desenha · F-026, F-031: apague todo o texto; se sobrar um mês, um polo, uma pilha de folhas, é instrumento. Se sobrar uma grade vazia, é tabela.</p></div>
</body></html>'''
(SITE / 'specimen/instrumentos.html').write_text(head + css + body)
print('ok, end of count:', end)
