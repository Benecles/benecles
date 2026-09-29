"""Teoria Geral dos Contratos course front: the course as the life of one contract (document-life genre).
Two parties are two lines. Before the signature they are separate (tratativas, proposta, aceitação) inside a dashed
band, because the contract does not exist yet; at the conclusion they bind; during execution they run together
(interpretação, revisão); at the cessão one line leaves and another enters; at the extinção the sheet tears and the
lines part. Principles are the roof over the whole life; classification is the stamp applied at conclusion.
Rewrites the front in the standard order: compact hero, the drawing, the exam card, the lesson grid.
Idempotent: the drawing lives between LIFE markers."""
import re, shutil, os

D = '/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/teoria-geral-dos-contratos/'
BK = '/private/tmp/claude-501/-Users-benecles/39f44e58-623c-4f38-b242-4c7babf2add5/scratchpad/contratos-index.pre-life.html'
if not os.path.exists(BK): shutil.copy(D + 'index.html', BK)

P2 = {'09', '10', '11', '12', '13', '14', '15', '16', '17'}
def tab(n, t, x, y, w, h=34):
    bar = f'<rect x="{x}" y="{y}" width="4" height="{h}" style="fill:var(--dif)"/>' if n in P2 else ''
    return (f'<a href="aula-{n}.html"><rect x="{x}" y="{y}" width="{w}" height="{h}" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>{bar}'
            f'<text x="{x + 11}" y="{y + h // 2 + 5}"><tspan class="n">{n}</tspan><tspan class="u" dx="7">{t}</tspan></text></a>')

W, H = 1100, 580
BT, BB = 250, 330                                  # the contract band
SIG, TEAR = 470, 1000
o = [f'<svg class="life" viewBox="0 0 {W} {H}" role="img" aria-label="Planta do curso: a vida de um contrato, das tratativas à extinção, com as aulas no momento que governam">']
o.append('<defs><marker id="la" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" style="fill:var(--ink)"/></marker></defs>')
o.append(f'<text x="30" y="30" class="hdr">A VIDA DE UM CONTRATO</text><text x="{W - 30}" y="30" text-anchor="end" class="ex">antes da assinatura: P1 · depois dela: P2 (27/11)</text>')

# roof: concept and principles hold over the whole life
o.append('<rect x="30" y="52" width="1040" height="56" style="fill:var(--paper-2);stroke:var(--ink);stroke-width:1.5"/>')
o.append('<text x="46" y="76" class="hdr">CONCEITO E PRINCÍPIOS</text><text x="46" y="95" class="ex" style="fill:var(--ink-2)">valem em toda a vida do contrato</text>')
o += [tab('01', 'Conceito', 330, 63, 150), tab('02', 'Liberdade, força, relatividade', 492, 63, 262), tab('03', 'Função social, boa-fé, equilíbrio', 766, 63, 290)]

# formation stations above the band
o.append('<text x="40" y="146" class="hdr" style="font-size:12px">FORMAÇÃO</text>')
o += [tab('04', 'Tratativas', 40, 156, 160), tab('05', 'Proposta e aceitação', 216, 156, 200), tab('06', 'Incidentes da formação', 432, 156, 210)]
for x0, xb in ((120, 120), (316, 316), (537, SIG)):
    o.append(f'<path d="M{x0} 190V{BT - 2}" style="stroke:var(--ink-2);stroke-width:1;fill:none"/>' if x0 == xb else
             f'<path d="M{x0} 190V214H{xb}V{BT - 2}" style="stroke:var(--ink-2);stroke-width:1;fill:none"/>')

# the band: dashed before it exists, solid after, torn at the end
o.append(f'<rect x="30" y="{BT}" width="{SIG - 30}" height="{BB - BT}" style="fill:var(--paper-2);stroke:var(--ink-2);stroke-width:1.2;stroke-dasharray:6 4"/>')
zig = ''.join(f'L{TEAR + (7 if k % 2 else -3)} {BT + k * 8}' for k in range(1, (BB - BT) // 8)) + f'L{TEAR} {BB}'
o.append(f'<path d="M{SIG} {BT}H{TEAR}{zig}H{SIG}Z" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.5"/>')
o.append(f'<text x="44" y="{BT + 16}" class="ex" style="fill:var(--ink-2)">A e B negociam; ainda não há contrato</text><text x="{SIG + 14}" y="{BT + 16}" class="ex" style="fill:var(--ink-2)">A e B estão vinculados</text>')

# the parties
A0, B0, A1, B1 = BT + 34, BT + 62, BT + 44, BT + 54
o.append(f'<text x="36" y="{A0 - 5}" class="pt">A</text><text x="36" y="{B0 + 14}" class="pt">B</text>')
o.append(f'<path d="M50 {A0}H{SIG - 40}C{SIG - 20} {A0} {SIG - 16} {A1} {SIG} {A1}H{TEAR - 12}C{TEAR + 4} {A1} {TEAR + 10} {BT + 18} {TEAR + 40} {BT + 18}" class="party"/>')
o.append(f'<path d="M50 {B0}H{SIG - 40}C{SIG - 20} {B0} {SIG - 16} {B1} {SIG} {B1}H835C850 {B1} 852 {BB + 24} 870 {BB + 30}" class="party"/>')
o.append(f'<path d="M820 {BB + 30}C842 {BB + 24} 846 {B1} 862 {B1}H{TEAR - 12}C{TEAR + 4} {B1} {TEAR + 10} {BB - 8} {TEAR + 40} {BB - 8}" class="party c"/>')
o.append(f'<text x="812" y="{BB + 44}" class="pt" style="fill:var(--dif)">C</text><text x="840" y="{BT - 10}" text-anchor="middle" class="ex" style="fill:var(--dif)">cessão: B sai, C entra ↓</text>')
o.append(f'<text x="80" y="{(A0 + B0) // 2 + 4}" class="ex" style="fill:var(--ink-2)">tratativas</text>')
o.append(f'<path d="M250 {A0 + 3}V{B0 - 4}" style="stroke:var(--ink);stroke-width:1.2;fill:none" marker-end="url(#la)"/><text x="256" y="{(A0 + B0) // 2 + 4}" class="ex">proposta</text>')
o.append(f'<path d="M380 {B0 - 3}V{A0 + 4}" style="stroke:var(--ink);stroke-width:1.2;fill:none" marker-end="url(#la)"/><text x="386" y="{(A0 + B0) // 2 + 4}" class="ex">aceitação</text>')

# the signature
o.append(f'<path d="M{SIG} {BT - 16}V{BB + 10}" style="stroke:var(--conc);stroke-width:2;fill:none"/>')
o.append(f'<path d="M{SIG - 34} {BT - 6}c7-15 13 9 19-3s9-12 14 1 7 7 13-5 6-4 12 2" style="stroke:var(--conc);stroke-width:1.6;fill:none"/>')
o.append(f'<text x="{SIG}" y="{BB + 26}" text-anchor="middle" class="ex" style="fill:var(--conc)">assinam: o contrato nasce</text>')
o.append(f'<text x="{TEAR + 44}" y="{BB + 26}" text-anchor="end" class="ex" style="fill:var(--conc)">extinção: o vínculo acaba</text>')

# classification: the stamp applied at conclusion
o.append('<rect x="40" y="392" width="330" height="96" style="fill:none;stroke:var(--ink);stroke-width:1.2"/><rect x="45" y="397" width="320" height="86" style="fill:none;stroke:var(--ink);stroke-width:.8;stroke-dasharray:3 3"/>')
o.append('<text x="58" y="418" class="hdr" style="font-size:12px">CLASSIFICAÇÃO</text><text x="186" y="418" class="ex" style="fill:var(--ink-2)">que tipo de contrato?</text>')
o += [tab('07', 'Classificação I', 58, 432, 145), tab('08', 'Classificação II', 212, 432, 145)]
o.append(f'<path d="M370 440H{SIG - 16}V{BB + 34}" style="stroke:var(--ink-2);stroke-width:1;stroke-dasharray:2 4;fill:none"/>')

# life after conclusion: stations below the band
ST = [(500, 'INTERPRETAÇÃO', 590, [('09', 'Sentido do acordo'), ('10', 'Regras especiais')]),
      (640, 'REVISÃO', 720, [('11', 'Na origem'), ('12', 'Na execução'), ('13', 'Base do negócio')]),
      (790, 'CESSÃO', 845, [('14', 'Quem entra')]),
      (930, 'EXTINÇÃO', 1000, [('15', 'Cumprimento'), ('16', 'Por vontade'), ('17', 'Inadimplemento')])]
for x, name, xb, tabs in ST:
    w = 135 if name != 'CESSÃO' else 125
    o.append(f'<text x="{x}" y="390" class="hdr" style="font-size:12px">{name}</text>')
    if name != 'CESSÃO':
        o.append(f'<path d="M{xb} {BB + 2}V376" style="stroke:var(--ink-2);stroke-width:1;stroke-dasharray:2 3;fill:none"/>')
    for k, (n, t) in enumerate(tabs):
        o.append(tab(n, t, x, 400 + k * 42, w))
# revisão "na origem" reaches back to the conclusion

o.append(f'<text x="30" y="{H - 14}" class="ex" style="fill:var(--muted)">linhas: as partes · tracejado: antes de o contrato existir · <tspan style="fill:var(--dif)">▌</tspan> matéria da P2 (27/11)</text></svg>')
svg = ''.join(o)

CSS = ('<style>.life{width:100%;height:auto;display:block;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major)}'
       '.life-scroll{overflow-x:auto}.life-scroll .life{min-width:880px}.life text{font-family:var(--mono);font-size:11px;fill:var(--ink)}'
       '.life .hdr{font:600 13px var(--mono);letter-spacing:.1em}.life .ex{fill:var(--conc)}.life .u{font:500 11.5px var(--sans)}.life .n{fill:var(--conc);font-weight:500}'
       '.life .pt{font:600 12px var(--mono)}.life .party{fill:none;stroke:var(--ink);stroke-width:2.2}.life .party.c{stroke:var(--dif)}'
       '.life a rect{transition:fill .15s}.life a:hover rect:first-child,.life a:focus-visible rect:first-child{fill:var(--conc-wash)}'
       'header.hero.front h1{font-size:clamp(40px,6.2vw,84px)!important;margin:18px 0 12px!important;max-width:none}header.hero.front .deck{max-width:62ch}'
       '.front-row{max-width:1180px;margin:28px auto 0;padding:0 clamp(16px,4vw,48px)}.front-row .exam-card{max-width:520px}</style>')

s = open(D + 'index.html').read()
if '<!-- LIFE:START -->' not in s:
    # standard order: compact hero (no exam card inside), the drawing, then the exam card row
    card = re.search(r'<aside class="exam-card".*?</aside>\s*(<script>.*?</script>\s*<script>.*?</script>)', s, re.S)
    card_html = card.group(0)
    s = s.replace(card_html, '')
    s = s.replace('<header class="hero">', '<header class="hero front">', 1)
    s = re.sub(r'<div class="course-intro">\s*<div>\s*(<p class="deck">.*?</p>)\s*</div>\s*</div>', r'\1', s, count=1, flags=re.S)
    sec = re.search(r'<section class="map-section" id="planta".*?</section>', s, re.S).group(0)
    new = ('<!-- LIFE:START --><!-- LIFE:END -->'
           f'\n<section class="front-row" aria-label="Próxima prova">{card_html}</section>')
    s = s.replace(sec, new)
block = (f'<!-- LIFE:START -->{CSS}<section class="map-section" id="planta" aria-label="Planta do curso: a vida de um contrato">'
         f'<div class="life-scroll" tabindex="0" role="region" aria-label="Planta do curso; deslize para o lado no celular">{svg}</div></section><!-- LIFE:END -->')
a, b = s.index('<!-- LIFE:START -->'), s.index('<!-- LIFE:END -->') + len('<!-- LIFE:END -->')
s = s[:a] + block + s[b:]
open(D + 'index.html', 'w').write(s)
print('contratos front written', len(s))
