"""Latam course index: head/CSS from the Contratos index (same components), body written here.
The semester plan is an atlas plate: countries tinted and clickable, case cities pinned with their lessons."""
import re, sys
sys.path.insert(0, '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/contract-build/generators')
import common, kit
from maps import latam_map, map_defs, xy

PUB = '/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/'
src = open(PUB + 'teoria-geral-dos-contratos/index.html').read()
head = src[:src.find('<body')]
head = re.sub(r'<title>.*?</title>', '<title>Direito Latino-americano · Ordenações</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Guia de estudo de Direito Latino-americano (DIR03057), UFRGS 2026/2: constitucionalismo, cortes, justiça de transição, soberania popular e litígio estrutural na América Latina.">', head)
head = re.sub(r'curso\.css\?v=[^"]*', f'curso.css?v={kit.VER}', head)
head = head.replace('</style>', '.atlas{display:grid;grid-template-columns:minmax(0,640px) minmax(0,1fr);gap:34px;align-items:start}'
                    '.atlas svg.fig{width:100%;height:auto;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major)}'
                    '.atlas a use{cursor:pointer}.atlas a:hover use,.atlas a:focus-visible use{fill:var(--conc-wash)!important;fill-opacity:.9}'
                    '.exam-card::before{content:"PRÓXIMA AVALIAÇÃO"!important}.hero.front{padding-bottom:6px}header.hero.front h1{font-size:clamp(40px,6.2vw,84px)!important;margin:18px 0 12px!important;max-width:none}.hero.front .deck{max-width:62ch}'
                    '.front-sheet{padding-top:18px!important}.atlas-side{display:grid;gap:22px;align-content:start}.atlas-side .exam-card{margin:0}'
                    '@media(max-width:860px){.atlas{grid-template-columns:1fr}}</style>', 1)

PINS = [('BRA', (-47.9, -15.8), 'Brasília', '03 · 07 · 09', 'aula-03.html', 'end', -14, -22),
        ('COL', (-74.07, 4.71), 'Bogotá', '04 · 07 · 08', 'aula-04.html', 'end', -44, 44),
        ('URY', (-56.2, -34.9), 'Montevidéu', '05', 'aula-05.html', 'start', 12, 6),
        ('BOL', (-65.26, -19.05), 'Sucre', '06', 'aula-06.html', 'end', -16, 2),
        ('CRI', (-84.08, 9.93), 'San José · Corte IDH', '03 · 05 · 06', 'aula-05.html', 'end', -24, -30)]
fills = {'BRA': 'conc', 'COL': 'dif', 'URY': 'mix', 'BOL': 'mix', 'CRI': 'dif'}
m = latam_map(fills, [], title='ONDE O CURSO ACONTECE', skip_seas=('OCEANO PACÍFICO',))
for iso, (lon, lat), city, aulas, href, anc, dx, dy in PINS:
    x, y = xy(lon, lat)
    lead = f'<path d="M{x} {y}L{x + dx + (4 if anc == "end" else -4)} {y + dy - 5}" style="fill:none;stroke:var(--ink-2);stroke-width:.8"/>' if abs(dy) > 20 else ''
    m += (f'<a href="{href}" aria-label="{city}: aulas {aulas}"><use href="#lm-{iso}" style="fill:transparent;stroke:none"/>'
          f'<circle cx="{x}" cy="{y}" r="4" style="fill:var(--ink)"/><circle cx="{x}" cy="{y}" r="7.5" style="fill:none;stroke:var(--ink);stroke-width:.9"/>{lead}'
          f'<text x="{x + dx}" y="{y + dy}" text-anchor="{anc}" style="font:600 12px var(--mono);fill:var(--ink)">{city}</text>'
          f'<text x="{x + dx}" y="{y + dy + 15}" text-anchor="{anc}" style="font:11px var(--mono);fill:var(--conc)">aulas {aulas}</text></a>')
m += (f'<g style="font:12px var(--mono);fill:var(--ink-2)"><text x="24" y="470">Brasil: anistia, ECI, saúde</text><text x="24" y="488">Colômbia: transição, ECI, T-025</text>'
      f'<text x="24" y="506">Uruguai, Bolívia: soberania</text><text x="24" y="524">San José: Corte IDH</text></g>')
atlas_svg = map_defs() + f'<svg class="fig" viewBox="0 0 600 600" role="img" aria-label="Mapa do curso: países e cortes estudados">{m}</svg>'

UNITS = [
    ('17/08', 'Constitucionalismo e cortes', 'Haiti, Cádiz e os três projetos fundacionais; o estudo de Engelmann e Bandeira e o mapa das cortes constitucionais.', [('aula-01.html', 'Aula 01 · Constitucionalismo'), ('aula-02.html', 'Aula 02 · Cortes')]),
    ('24/08', 'Justiça de transição', 'ADPF 153 e Gomes Lund; a Corte Constitucional colombiana e o processo de paz.', [('aula-03.html', 'Aula 03 · ADPF 153'), ('aula-04.html', 'Aula 04 · Colômbia')]),
    ('31/08', 'Soberania popular e direitos', 'Gelman contra a Lei de Caducidade; a reeleição boliviana e a OC-28.', [('aula-05.html', 'Aula 05 · Gelman'), ('aula-06.html', 'Aula 06 · Bolívia e OC-28')]),
    ('14/09', 'Estado de coisas inconstitucional', 'T-153 e as prisões colombianas; a ADPF 347 no STF.', [('aula-07.html', 'Aula 07 · ECI')]),
    ('21/09', 'Litígio estrutural', 'T-025, deslocamento forçado e os autos de acompanhamento.', [('aula-08.html', 'Aula 08 · T-025')]),
    ('28/09', 'Saúde e diálogo institucional', 'STA 175, Temas 500, 6 e 1234 e as Súmulas Vinculantes 60 e 61.', [('aula-09.html', 'Aula 09 · Saúde')]),
]
EXTRA_UNITS = ('<article class="lesson-group"><h3><span>Atividade · 05/10</span>Revisão para a atividade</h3><p>Oito eixos, três quadros comparativos e dez problemas mistos resolvidos.</p><div class="lesson-links"><a class="review-link" href="revisao-atividade.html">Abrir revisão →</a></div></article>'
               '<article class="lesson-group"><h3><span>Modo prova</span>Cartões de estudo</h3><p>As perguntas das aulas em cartões com revisão espaçada: os que você acerta voltam mais tarde, os que erra voltam logo.</p><div class="lesson-links"><a href="cartoes.html">Abrir cartões →</a></div></article>')
units = ''.join(f'<article class="lesson-group"><h3><span>{d}</span>{t}</h3><p>{p}</p><div class="lesson-links">' + ''.join(f'<a href="{h}">{l}</a>' for h, l in links) + '</div></article>' for d, t, p, links in UNITS)

body = f'''<body>
<nav class="topbar" aria-label="Navegação principal"><a href="../../index.html">← Ordenações</a><span>DIR03057 · UFRGS · 2026/2</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero front">
  <div class="kicker label"><span>Guia de estudo · Direito Público</span><span>Profa. Roberta Baggio</span><span>9 aulas · atividade em 05/10</span></div>
  <h1><span class="split">Direito</span><span class="split">Latino-americano</span></h1>
  <p class="deck">Constituições, cortes e direitos humanos na América Latina. Cada país marcado tem ao menos uma aula: clique nele para abrir.</p>
</header>

<main>
<section class="map-section front-sheet" id="planta" aria-label="Mapa do curso">
  <div class="atlas">{atlas_svg}
    <div class="atlas-side">
      <aside class="exam-card" aria-labelledby="exam-title">
        <span class="exam-date">Atividade avaliativa · 05/10/2026</span>
        <h2 id="exam-title">Revisão para a atividade</h2>
        <p>Os oito eixos com respostas, três quadros comparativos e dez problemas mistos resolvidos.</p>
        <a href="revisao-atividade.html"><span>Abrir revisão</span><span aria-hidden="true">→</span></a>
        <a href="cartoes.html"><span>Cartões com revisão espaçada</span><span aria-hidden="true">→</span></a>
        <a class="resume" href="#" hidden><span>Continuar de onde parou</span><span aria-hidden="true">→</span></a>
      </aside>
      <ol class="pathway" aria-label="Aulas por data" style="grid-template-columns:1fr">
        {''.join(f'<li class="unit current"><h3>{d} · {t}</h3><div class="unit-links">' + ''.join(f'<a href="{h}">{l.split(" · ")[0]}</a>' for h, l in links) + '</div></li>' for d, t, p, links in UNITS)}
      </ol>
    </div>
  </div>
<script>(function(){{try{{if(localStorage.getItem('ordenacoes-no-resume'))return;var d=JSON.parse(localStorage.getItem('ordenacoes-dla-last')||'null');if(!d||!/^\\d\\d$/.test(d.n))return;var a=document.querySelector('.exam-card .resume');a.href='aula-'+d.n+'.html';a.firstChild.textContent='Continuar: Aula '+d.n+' · '+String(d.t).slice(0,48);a.hidden=false}}catch(e){{}}}})()</script>
</section>

'''
body += f'''<section class="lessons" id="aulas" aria-labelledby="lessons-title">
  <header class="section-head"><span class="label">02 / Caderno de estudo</span><h2 id="lessons-title">Aulas</h2><p>Na ordem do programa.</p></header>
  <div class="lesson-grid">{units}{EXTRA_UNITS}</div>
</section>
</main>
<p class="endnote">Direito Latino-americano (DIR03057) · UFRGS · 2026/2. Fronteiras nos mapas: atuais, para orientação.</p>
<script src="assets/curso.js?v={kit.VER}"></script>
</body>
</html>
'''
open(PUB + 'direito-latino-americano/index.html', 'w').write(head + body)
print('wrote index', len(head + body))

# the ⓘ sources button lives in the top bar; re-apply it after rewriting the front
import subprocess
subprocess.run(['python3', '/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/tools/fontes_info.py'], check=True)
