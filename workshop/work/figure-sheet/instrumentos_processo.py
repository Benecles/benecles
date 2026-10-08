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

# ---------- 3. the autos, seen from the side ----------
# 2015/1, Avaliação 2 (24/06/2015), questões 1–4. Acts and dates from the enunciado; folha numbers illustrative.
import random, math
rng = random.Random(207)
# (title, meta lines, sheets, kind)  kind: act | key (blue, the question) | gap (orange, absent) | next (dashed, not yet)
acts = [
    ('petição inicial e documentos', ['Jesse Valadão · cobrança solidária de R$ 100.000,00'], 14, 'act'),
    ('ARs das cartas de citação', ['Dalvo Fritz e Serotonina da Silva, citados por carta'], 2, 'act'),
    ('termo da audiência preliminar', ['01/04/2015 · todas as partes presentes, sem acordo'], 2, 'act'),
    ('contestação de Dalvo Fritz', ['preliminares, mérito e reconvenção', 'na primeira semana do prazo'], 14, 'act'),
    ('petição complementar de Dalvo', ['13/04/2015 · impugna os fatos esquecidos', 'questão 1: ainda no prazo, integra a defesa'], 2, 'key'),
    ('defesa de Serotonina da Silva', ['nenhuma folha: revel (art. 344), sem advogado', 'a contestação de Dalvo a socorre (art. 345, I)'], 3, 'gap'),
    ('resposta à reconvenção e réplica', ['arts. 343, § 1º, 350 e 351 · ainda por vir'], 4, 'next'),
    ('decisão de saneamento', ['art. 357, III: distribui o ônus da prova (Fig. D)'], 2, 'next'),
]
P, SH = 11, 8                      # sheet pitch, sheet thickness
SX, SW = 262, 380                  # stack left edge (after the spine), width
BOT = 640                          # bottom of the stack (top of the capa)
u = ['<svg viewBox="0 0 1080 720" role="img" aria-label="Os autos vistos de lado: uma pilha de folhas numeradas em que cada ato do caso Jesse Valadão entra por cima, na ordem em que foi juntado">']
u.append('<style>.a-k{font:500 11px var(--mono);letter-spacing:.08em;fill:var(--ink-2)}.a-f{font:500 13px var(--mono);fill:var(--ink-2)}.a-h{font:650 17px var(--sans);fill:var(--ink)}.a-m{font:italic 400 15px var(--serif);fill:var(--ink-2)}.a-q{font:italic 400 17px var(--serif);fill:var(--ink)}</style>')
u.append('<text x="40" y="34" class="a-k">2015/1 · Avaliação 2 · Jesse Valadão × Dalvo Fritz e Serotonina da Silva</text>')
u.append('<text x="40" y="60" class="a-q">art. 207: “O escrivão ou o chefe de secretaria numerará e rubricará todas as folhas dos autos.”</text>')
# capa
u.append(f'<rect x="{SX-6}" y="{BOT}" width="{SW+14}" height="18" rx="2" style="fill:var(--paper-2);stroke:var(--ink);stroke-width:1.5"/>')
bands, y, fl = [], BOT, 2
for title, meta, n, kind in acts:
    top = y - n*P
    bands.append((title, meta, n, kind, top, y, fl))
    if kind == 'gap':
        u.append(f'<rect x="{SX}" y="{top+2}" width="{SW}" height="{n*P-4}" style="fill:url(#ip-hatch);stroke:var(--conc);stroke-width:1.5;stroke-dasharray:6 5"/>')
    else:
        for k in range(n):
            sy = y - (k+1)*P + (P-SH)
            dx = rng.uniform(-3, 3); dw = rng.uniform(-4, 2)
            if kind == 'next':
                st = 'fill:none;stroke:var(--muted);stroke-width:1;stroke-dasharray:4 4'
            else:
                first = k == 0
                st = f'fill:var(--paper);stroke:var(--ink);stroke-width:{1.6 if first else 1}'
            u.append(f'<rect x="{SX+dx:.1f}" y="{sy}" width="{SW+dw:.1f}" height="{SH}" style="{st}"/>')
        if kind != 'next':
            u.append(f'<text x="{SX-26}" y="{(top+y)/2+5}" text-anchor="end" class="a-f">{fl if n == 1 else f"{fl}–{fl+n-1}"}</text>')
            fl += n
    y = top
STOP = y
# spine: the binding cord through the left margin, only along the sheets that exist
spine_top = bands[4][4]
u.append(f'<line x1="{SX+14}" y1="{spine_top+4}" x2="{SX+14}" y2="{BOT+14}" style="stroke:var(--ink);stroke-width:1.5"/>')
for yy in range(int(spine_top)+16, BOT, 46):
    u.append(f'<line x1="{SX+8}" y1="{yy}" x2="{SX+20}" y2="{yy}" style="stroke:var(--ink);stroke-width:2.5"/>')
u.append(f'<text x="{SX-26}" y="{BOT+14}" text-anchor="end" class="a-f">1</text>')
u.append(f'<text x="{SX-26}" y="{BOT+36}" text-anchor="end" class="a-k">fls.</text>')
# growth rail at the far left
u.append(f'<line x1="70" y1="{BOT+10}" x2="70" y2="{STOP+6}" style="stroke:var(--ink);stroke-width:1.5"/><path d="M63 {STOP+18} L70 {STOP+4} L77 {STOP+18}" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>')
u.append(f'<text transform="translate(58 {(BOT+STOP)/2}) rotate(-90)" text-anchor="middle" class="a-k">cada ato juntado entra por cima</text>')
# tabs and labels: labels relaxed to keep 1 line gap, leaders out into the clear column
LX, LH, MH = 724, 20, 19
want = []
for b in bands:
    title, meta, n, kind, top, bot, _ = b
    h = LH + MH*len(meta)
    want.append([ (top+bot)/2 - h/2 + 14, h ])
# capa label too
want.append([BOT+9-6, LH]); bands.append(('capa · autuação', [], 0, 'capa', BOT, BOT+18, 1))
# relax upward from bottom: labels in order bottom→top must keep ys decreasing with gaps
order = list(range(len(want)))
order.sort(key=lambda i: -want[i][0])
prev = None
for i in order:
    if prev is not None:
        lim = want[prev][0] - 10 - want[i][1]
        if want[i][0] > lim: want[i][0] = lim
    prev = i
# if the topmost label went too high, push all down from the top
top_i = order[-1]
if want[top_i][0] < 96:
    shift = 96 - want[top_i][0]; prev = None
    for i in reversed(order):
        if prev is not None:
            lim = want[prev][0] + want[prev][1] + 10
            if want[i][0] < lim: want[i][0] = lim
        else: want[i][0] += shift
        prev = i
for b, (ly, h) in zip(bands, want):
    title, meta, n, kind, top, bot, _ = b
    col = {'key': 'var(--dif)', 'gap': 'var(--conc)', 'next': 'var(--muted)'}.get(kind, 'var(--ink)')
    my = (top+bot)/2
    if kind != 'capa':
        dash = ';stroke-dasharray:4 4' if kind == 'next' else ''
        u.append(f'<rect x="{SX+SW+4}" y="{top+3}" width="16" height="{bot-top-6}" style="fill:{"var(--dif)" if kind=="key" else "var(--paper)"};stroke:{col};stroke-width:1.5{dash}"/>')
        x0 = SX+SW+20
    else:
        x0 = SX+SW+10
    ty = ly + 2
    u.append(f'<path d="M{x0} {my} H{x0+22} L{LX-14} {ty-5} H{LX-6}" style="fill:none;stroke:{col};stroke-width:1.2"/>')
    hc = 'a-h' if kind != 'capa' else 'a-k'
    u.append(f'<text x="{LX}" y="{ty}" class="{hc}" style="fill:{col if kind in ("key","gap") else ("var(--muted)" if kind=="next" else "var(--ink)")}">{title}</text>')
    for j, m in enumerate(meta):
        u.append(f'<text x="{LX}" y="{ty+LH+j*MH}" class="a-m">{m}</text>')
u.append(f'<text x="40" y="{BOT+62}" class="a-k">números de folha ilustrativos: o enunciado não os dá · atos, datas e ordem: os do enunciado</text>')
u.append('</svg>')
autos = '\n'.join(u)

# ---------- 4. the burden of proof, on a balance ----------
# CPC art. 373 (capture 28/09: chapters/cpc-lei-13105-capture-2026-09-28/0373-art-0373.txt), words verbatim.
v = ['<svg viewBox="0 0 1080 770" role="img" aria-label="Balança do ônus da prova: o fato constitutivo no prato do autor, os fatos impeditivos, modificativos e extintivos no prato do réu; um peso passa de um prato ao outro pelo § 1º, e o fiel não pode entrar na faixa do § 2º">']
v.append('<style>.b-k{font:500 11px var(--mono);letter-spacing:.08em;fill:var(--ink-2)}.b-w{font:500 13px var(--mono);fill:var(--ink)}.b-h{font:750 22px var(--sans);fill:var(--ink)}.b-r{font:400 16px var(--serif);fill:var(--ink)}.b-q{font:italic 400 17px var(--serif);fill:var(--ink)}</style>')
PX, PY, HL, TH = 540, 310, 330, 7          # pivot, half-beam, tilt (deg) after § 1º
def beam_end(side, th):
    a = math.radians(th); return PX + side*HL*math.cos(a), PY + side*HL*math.sin(a)
v.append('<text x="40" y="34" class="b-k">art. 373 · se o fato ficar sem prova, quem perde?</text>')
# post and base
v.append(f'<line x1="{PX}" y1="{PY}" x2="{PX}" y2="682" style="stroke:var(--ink);stroke-width:5"/>')
v.append(f'<path d="M{PX-90} 700 L{PX-60} 678 H{PX+60} L{PX+90} 700 Z" style="fill:var(--paper-2);stroke:var(--ink);stroke-width:1.5"/>')
# gauge (o fiel): scale above the pivot, § 2º zones at the ends
R = 132
def pol(deg, r): a = math.radians(deg); return PX + r*math.sin(a), PY - r*math.cos(a)
LIM, MAXA = 16, 40
for sgn in (1, -1):
    a0, a1 = sgn*LIM, sgn*MAXA
    p0o, p1o, p1i, p0i = pol(a0, R+16), pol(a1, R+16), pol(a1, R-6), pol(a0, R-6)
    sw = 1 if sgn > 0 else 0
    v.append(f'<path d="M{p0o[0]:.1f} {p0o[1]:.1f} A{R+16} {R+16} 0 0 {sw} {p1o[0]:.1f} {p1o[1]:.1f} L{p1i[0]:.1f} {p1i[1]:.1f} A{R-6} {R-6} 0 0 {1-sw} {p0i[0]:.1f} {p0i[1]:.1f} Z" style="fill:url(#ip-hatch);stroke:var(--conc);stroke-width:1.5"/>')
    sp = pol(sgn*LIM, R+5)
    v.append(f'<circle cx="{sp[0]:.1f}" cy="{sp[1]:.1f}" r="4.5" style="fill:var(--conc)"/>')
pa, pb = pol(-MAXA, R), pol(MAXA, R)
v.append(f'<path d="M{pa[0]:.1f} {pa[1]:.1f} A{R} {R} 0 0 1 {pb[0]:.1f} {pb[1]:.1f}" style="fill:none;stroke:var(--ink);stroke-width:1.2"/>')
for d in range(-MAXA, MAXA+1, 2):
    q0, q1 = pol(d, R), pol(d, R+(12 if d % 10 == 0 else 6))
    v.append(f'<line x1="{q0[0]:.1f}" y1="{q0[1]:.1f}" x2="{q1[0]:.1f}" y2="{q1[1]:.1f}" style="stroke:var(--ink);stroke-width:1"/>')
# beams: dashed = caput (level), solid = after § 1º
l0, r0 = beam_end(-1, 0), beam_end(1, 0)
v.append(f'<line x1="{l0[0]}" y1="{l0[1]}" x2="{r0[0]}" y2="{r0[1]}" style="stroke:var(--muted);stroke-width:2;stroke-dasharray:7 6"/>')
L, Rr = beam_end(-1, TH), beam_end(1, TH)
v.append(f'<line x1="{L[0]:.1f}" y1="{L[1]:.1f}" x2="{Rr[0]:.1f}" y2="{Rr[1]:.1f}" style="stroke:var(--ink);stroke-width:7;stroke-linecap:round"/>')
nd = pol(TH, R-10)
v.append(f'<line x1="{PX}" y1="{PY}" x2="{nd[0]:.1f}" y2="{nd[1]:.1f}" style="stroke:var(--dif);stroke-width:3"/>')
v.append(f'<circle cx="{PX}" cy="{PY}" r="9" style="fill:var(--paper);stroke:var(--ink);stroke-width:2.5"/>')
def weight(cx, by, w, h, label, kind='ink'):
    st = {'ink': 'fill:var(--paper-2);stroke:var(--ink);stroke-width:1.6',
          'blue': 'fill:var(--dif);stroke:var(--dif);stroke-width:1.6',
          'ghost': 'fill:var(--paper);stroke:var(--dif);stroke-width:1.5;stroke-dasharray:5 4'}[kind]
    out = [f'<path d="M{cx-w/2} {by} L{cx-w/2+8} {by-h} H{cx+w/2-8} L{cx+w/2} {by} Z" style="{st}"/>',
           f'<path d="M{cx-9} {by-h} V{by-h-9} Q{cx} {by-h-17} {cx+9} {by-h-9} V{by-h}" style="fill:none;stroke:{"var(--ink)" if kind=="ink" else "var(--dif)"};stroke-width:2{";stroke-dasharray:3 3" if kind=="ghost" else ""}"/>']
    if label:
        out.append(f'<text x="{cx}" y="{by-h/2+5}" text-anchor="middle" class="b-w" style="fill:{"var(--paper)" if kind=="blue" else ("var(--dif)" if kind=="ghost" else "var(--ink)")}">{label}</text>')
    return out
def pan(ex, ey, w, drop):
    py = ey + drop
    out = [f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ex-w/2:.1f}" y2="{py:.1f}" style="stroke:var(--ink);stroke-width:1.2"/>',
           f'<line x1="{ex:.1f}" y1="{ey:.1f}" x2="{ex+w/2:.1f}" y2="{py:.1f}" style="stroke:var(--ink);stroke-width:1.2"/>',
           f'<path d="M{ex-w/2:.1f} {py:.1f} Q{ex:.1f} {py+40:.1f} {ex+w/2:.1f} {py:.1f} Z" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>',
           f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" style="fill:var(--ink)"/>']
    return out, py
DROP, PW = 170, 320
o, lpy = pan(L[0], L[1], PW, DROP); v += o
o, rpy = pan(Rr[0], Rr[1], PW, DROP); v += o
# autor's pan: the constitutive fact, and the empty place the moved weight left
v += weight(L[0]-36, lpy, 178, 56, 'fato constitutivo')
gx = L[0]+98
v += weight(gx, lpy, 72, 40, '', 'ghost')
# réu's pan: impeditivo, modificativo, extintivo, plus the moved weight on top
v += weight(Rr[0]-74, rpy, 132, 44, 'impeditivo')
v += weight(Rr[0]+70, rpy, 146, 44, 'modificativo')
v += weight(Rr[0]-66, rpy-44, 118, 40, 'extintivo')
mx = Rr[0]+60
v += weight(mx, rpy-44, 72, 40, '§ 1º', 'blue')
# the move: from the ghost over the gauge to the réu's pan
v.append(f'<path d="M{gx} {lpy-64} C {gx+30} 20, {mx-30} 20, {mx} {rpy-106}" style="fill:none;stroke:var(--dif);stroke-width:2;stroke-dasharray:7 5"/>')
v.append(f'<path d="M{mx-7} {rpy-120} L{mx} {rpy-104} L{mx+8} {rpy-119}" style="fill:none;stroke:var(--dif);stroke-width:2"/>')
v.append(f'<text x="{PX}" y="62" text-anchor="middle" class="b-k" style="fill:var(--dif)">§ 1º · por decisão fundamentada</text>')
v.append(f'<text x="{PX}" y="86" text-anchor="middle" class="b-q">“poderá o juiz atribuir o ônus da prova de modo diverso”</text>')
# § 2º, beside the right-hand zone
z = pol(MAXA, R+16)
v.append(f'<text x="{z[0]+14:.1f}" y="{z[1]+18:.1f}" class="b-k" style="fill:var(--conc)">§ 2º · batente</text>')
v.append(f'<text x="{z[0]+14:.1f}" y="{z[1]+40:.1f}" class="b-r">nunca “impossível ou</text>')
v.append(f'<text x="{z[0]+14:.1f}" y="{z[1]+60:.1f}" class="b-r">excessivamente difícil”</text>')
# party and caput, under each pan
for x, py, who, lines in ((L[0], lpy, 'autor', ['I · “ao autor, quanto ao fato', 'constitutivo de seu direito”']),
                          (Rr[0], rpy, 'réu', ['II · “ao réu, quanto à existência de fato', 'impeditivo, modificativo ou extintivo', 'do direito do autor”'])):
    v.append(f'<text x="{x-PW/2:.1f}" y="{py+60:.1f}" class="b-h">{who}</text>')
    for j, ln in enumerate(lines):
        v.append(f'<text x="{x-PW/2:.1f}" y="{py+86+j*21:.1f}" class="b-r">{ln}</text>')
v.append(f'<text x="{PX-110}" y="730" class="b-k">tracejado: a balança do caput · cheio: depois do § 1º</text>')
v.append('<text x="40" y="756" class="b-k" style="fill:var(--dif)">2015/1 · Avaliação 2 · questão 8, gabarito d: a decisão que inverte o ônus “não prescinde de fundamentação”</text>')
v.append('</svg>')
balanca = '\n'.join(v)

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
<figure class="ip-fig">{autos}<figcaption>Fig. C · Os autos vistos de lado: cada ato do caso Jesse Valadão entra por cima, na ordem em que foi juntado, e a defesa que não veio é um vão na pilha</figcaption></figure>
<div class="ip-why"><div><b>O objeto</b>A pilha de folhas, de lado, com a capa embaixo e a costura na margem. A espessura de cada peça mostra quanto ela pesa nos autos; a ordem é a do processo.</div><div><b>A regra</b>O art. 207 numera as folhas; o resto é consequência: o ato posterior fica sempre por cima. A revelia de Serotonina não é uma folha, é a falta dela.</div><div><b>O que o leitor faz</b>Procura cada ato pela aba, como no balcão do cartório. Vê que a folha de 13/04 caiu antes do fim do prazo (questão 1) e que as próximas folhas já têm lugar marcado.</div></div>
<figure class="ip-fig">{balanca}<figcaption>Fig. D · O ônus da prova numa balança: cada fato pesa no prato de quem perde se ele ficar sem prova; o juiz pode mover um peso, mas o fiel não entra na faixa do § 2º</figcaption></figure>
<div class="ip-why"><div><b>O objeto</b>Uma balança de pratos com o fiel e a escala. O tracejado é a distribuição legal; a viga cheia, a redistribuída.</div><div><b>A regra</b>Os dois incisos do caput viram dois pratos; o § 1º é o peso que muda de lado por decisão fundamentada; o § 2º é o batente na escala.</div><div><b>O que o leitor faz</b>Pergunta, para cada fato do caso, em que prato ele está e quem o pôs ali. A questão 8 da prova vira a seta azul: sem fundamentação, o peso não se move.</div></div>
<div class="ip-col"><p class="label" style="font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)">Para quem desenha · F-026, F-031: apague todo o texto; se sobrar um mês, um polo, uma pilha de folhas, é instrumento. Se sobrar uma grade vazia, é tabela.</p></div>
</body></html>'''
(SITE / 'specimen/instrumentos.html').write_text(head + css + body)
print('ok, end of count:', end)
