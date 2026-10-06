#!/usr/bin/env python3
"""CASA-1: build specimen/casa.html in the site repo from live Latam A05 + the Latam register.
Usage: python3 build_casa.py [SITE_DIR]   (default ~/Developer/ordenacoes-filipinas)
Prose is A05 chapter 2 verbatim; the only edits are span wrappers (marks) and the block swap
.lex -> .fonte. Nothing is rewritten."""
import re, sys, pathlib

SITE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '~/Developer/ordenacoes-filipinas').expanduser()
a05 = (SITE / 'courses/direito-latino-americano/aula-05.html').read_text()
idx = (SITE / 'courses/direito-latino-americano/index.html').read_text()

def cut(s, start, end):
    i = s.index(start); j = s.index(end, i); return s[i:j + len(end)]

fork = cut(a05, '<svg class="hero-fork"', '</svg>')
bet = cut(a05, '<div class="bet">', '</div></div>') + '</div>'   # outer wrapper close
bet = a05[a05.index('<div class="bet">'):]
bet = bet[:bet.index('<section class="chapter"')]
reg = cut(idx, '<section class="front-lessons register"', '</section>')
reg = re.sub(r'(<li class="reg-unit">.*?</li>)', lambda m: m.group(1), reg, flags=re.S)
units = re.findall(r'<li class="reg-unit">.*?</ol></li>', reg, flags=re.S)
reg = '<section class="register casa-reg"><ol class="reg">' + units[0] + units[1] + '</ol></section>'

quiz = cut(a05, '<div class="quiz">', '</details></div>')
# keep the first two questions only
qs = re.findall(r'<details>.*?</details>', quiz, flags=re.S)
quiz = '<div class="quiz">' + ''.join(qs[:2]) + '</div>'

def art(t): return f'<span class="art">{t}</span>'

PROSE_1 = (
 'A Corte reafirmou a linha que vinha desde <em>Barrios Altos vs. Peru</em> (2001): são inadmissíveis anistias, prescrições e excludentes de responsabilidade que impeçam a investigação e a punição de graves violações, como tortura, execuções e desaparecimentos forçados (§ 225). '
 f'Essas leis violam os {art("arts. 1.1 e 2")} da Convenção, porque impedem que as vítimas sejam ouvidas por um juiz ({art("art. 8.1")}) e recebam proteção judicial ({art("art. 25")}), e por isso “<span class="held">carecem de efeitos jurídicos</span>” (§ 226).'
)
PROSE_2 = (
 'Dois passos da sentença vão além dessa linha. O primeiro está no § 229: a incompatibilidade não se restringe às '
 '<span class="term" tabindex="0" data-def="Anistia editada pelo regime em favor de si próprio.">autoanistias</span>. '
 'O que importa não é o processo de adoção nem a autoridade que editou a lei, mas a sua '
 '<span class="term" tabindex="0" data-def="O propósito da lei; aqui, deixar impunes graves violações."><em>ratio legis</em></span>, isto é, deixar impunes graves violações. '
 '<span class="held">A incompatibilidade é material, não formal.</span>'
)
SRC_238 = '''<aside class="fonte dec" aria-label="Fonte: Corte IDH, Gelman vs. Uruguai, § 238">
<header><span>Corte IDH · Gelman vs. Uruguai (2011)</span><span class="loc">§ 238</span></header>
<blockquote lang="es"><p>El hecho de que la Ley de Caducidad haya sido aprobada en un régimen democrático y aún ratificada o respaldada por la ciudadanía en dos ocasiones no le concede, <span class="key">automáticamente ni por sí sola, legitimidad ante el Derecho Internacional</span>.</p></blockquote>
<p class="tr" hidden><b>Tradução nossa</b>O fato de a Lei de Caducidade ter sido aprovada num regime democrático e ainda ratificada ou respaldada pela cidadania em duas ocasiões não lhe concede, automaticamente nem por si só, legitimidade perante o Direito Internacional.</p>
<footer><button type="button" data-tr aria-expanded="false">ver tradução</button></footer>
</aside>'''
PROSE_3 = (
 'O segundo passo responde exatamente ao que distinguia o caso uruguaio: a lei não era uma autoanistia de ditadura, e o povo a confirmou duas vezes. '
 f'Para a Corte, o referendo de 1989 ({art("art. 79")} da Constituição uruguaia) e o plebiscito de 2009 ({art("art. 331")}) são atos atribuíveis ao Estado e, portanto, também geram responsabilidade internacional (§ 238). E no § 239 formula o princípio:'
)
SRC_239 = '''<aside class="fonte dec" aria-label="Fonte: Corte IDH, Gelman vs. Uruguai, § 239">
<header><span>Corte IDH · Gelman vs. Uruguai (2011)</span><span class="loc">§ 239</span></header>
<blockquote lang="es"><p>La sola existencia de un régimen democrático no garantiza, per se, el permanente respeto del Derecho Internacional [...]. La legitimación democrática de determinados hechos o actos en una sociedad está limitada por las normas y obligaciones internacionales de protección de los derechos humanos [...], <span class="key">la protección de los derechos humanos constituye un límite infranqueable a la regla de mayorías</span>, es decir, a la esfera de lo “susceptible de ser decidido” por parte de las mayorías.</p></blockquote>
<p class="tr" hidden><b>Tradução nossa</b>A mera existência de um regime democrático não garante, por si só, o respeito permanente ao Direito Internacional [...]. A legitimação democrática de determinados fatos ou atos numa sociedade está limitada pelas normas e obrigações internacionais de proteção dos direitos humanos [...], a proteção dos direitos humanos constitui um limite intransponível à regra das maiorias, isto é, à esfera do “suscetível de ser decidido” pelas maiorias.</p>
<footer><button type="button" data-tr aria-expanded="false">ver tradução</button></footer>
</aside>'''
PROSE_4 = (
 'O caso tinha uma particularidade que a Corte registrou sem se deixar desviar por ela. Desde 23 de junho de 2005, o Executivo uruguaio entendia que o caso Gelman estava fora do alcance da Lei de Caducidade, e a investigação havia sido reaberta. Mesmo assim, o principal obstáculo às investigações tinha sido a vigência e a aplicação da própria lei (§ 241). Por isso a condenação não se limita ao caso: o Uruguai descumpriu o dever de adequar seu direito interno à Convenção ('
 f'{art("art. 2º")}), pela interpretação e aplicação que deu à Lei de Caducidade em graves violações.'
)
PROSE_5 = (
 'Nos pontos resolutivos, todos votados por unanimidade, a Corte declarou o Uruguai responsável pelo desaparecimento forçado de María Claudia, pela supressão e substituição da identidade de Macarena, tratada como forma de desaparecimento forçado, e pela falta de investigação. Mandou conduzir a investigação, determinar responsabilidades e aplicar as sanções cabíveis (ponto 9), continuar a busca por María Claudia (ponto 10) e garantir que a Lei de Caducidade, por carecer de efeitos, não volte a obstruir a investigação deste e de outros casos de graves violações (ponto 11).'
)
H3 = 'O voto de Vio Grossi: por que o eleitorado responde pelo Estado'
PROSE_6 = (
 'Ninguém divergiu, mas o juiz Eduardo Vio Grossi juntou um voto concorrente que explica o passo mais ousado da sentença: imputar ao Estado o resultado de uma votação popular. Pelas regras de responsabilidade internacional codificadas pela '
 '<span class="org">Comissão de Direito Internacional da ONU</span>, é ato do Estado o comportamento de qualquer de seus órgãos, exerça ele funções legislativas, executivas, judiciais ou “de outra índole”. Quando o eleitorado aprova ou ratifica uma lei, exerce função legislativa, ou ao menos uma função de outra índole, a da democracia direta. '
 '<span class="mark">Logo, a cidadania inteira pode violar uma norma internacional e comprometer a responsabilidade do Estado.</span> A qualificação de um ato como ilícito pelo direito internacional não depende do que diz o direito interno.'
)
PROSE_7 = (
 'Vio Grossi apoia a frase do § 239 na Carta Democrática Interamericana: ela faz do respeito aos direitos humanos elemento essencial da democracia (art. 3º) e, no art. 8º, garante a quem se considere violado o acesso ao sistema interamericano de petições, e não aos órgãos políticos da OEA. O mesmo voto traz uma advertência que reaparecerá em Montevidéu: a jurisprudência da Corte é fonte auxiliar do direito internacional. Ela interpreta o tratado, o costume ou o princípio vigente para o Estado; '
 '<span class="limit">não cria direito novo</span>.'
)
SRC_AUTO = '''<aside class="fonte lim" aria-label="Fonte: Corte Constitucional da Colômbia, Auto 008/2009">
<header><span>Corte Constitucional · Auto 008/2009</span><span class="loc">ordinal primeiro</span></header>
<blockquote lang="es"><p>Constatar que persiste el estado de cosas inconstitucional, a pesar de los avances logrados. [...] <span class="key">La carga de demostrar que las condiciones que dieron lugar a la declaratoria del estado de cosas inconstitucional han sido superadas, recae sobre el gobierno nacional.</span></p></blockquote>
<footer></footer>
</aside>'''
SRC_LEI = '''<aside class="fonte dec" aria-label="Fonte: Lei 6.683/1979">
<header><span>Lei 6.683/1979</span><span class="loc">art. 1º, § 1º</span></header>
<blockquote><p>Consideram-se conexos, para efeito deste artigo, os crimes de qualquer natureza relacionados com crimes políticos ou praticados por motivação política.</p></blockquote>
</aside>'''

KEY = [
 ('<span class="held">decidiu</span>', 'o que a corte ou a lei decidiu: a regra operativa', 'azul · no máximo uma por parágrafo'),
 ('<span class="limit">não fez</span>', 'o limite, a armadilha, o que a decisão não faz', 'laranja · no máximo uma por parágrafo'),
 ('<span class="mark">a frase para guardar</span>', 'a única frase do capítulo que vale decorar', 'marca-texto · uma por capítulo'),
 ('<span class="term" tabindex="0" data-def="Passe o ponteiro ou use Tab: a definição aparece aqui.">termo técnico</span>', 'define o termo ali mesmo', 'pontilhado · passe o ponteiro'),
 (art('art. 23 CADH'), 'artigo que o leitor pode querer abrir', 'mono em caixa fina'),
 ('<span class="org">Corte Constitucional</span>', 'órgão, na primeira menção', 'versalete'),
]
key_html = ''.join(f'<li><span class="k-sample">{s}</span><span class="k-does">{d}</span><span class="k-rule">{r}</span></li>' for s, d, r in KEY)

html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script>(function(){{var k='ordenacoes-theme',r=document.documentElement;try{{if(localStorage.getItem(k)==='dark')r.dataset.theme='dark'}}catch(e){{}}document.addEventListener('DOMContentLoaded',function(){{var b=document.querySelector('.theme-toggle');if(!b)return;function sync(){{b.setAttribute('aria-pressed',r.dataset.theme==='dark')}}sync();b.addEventListener('click',function(){{if(r.dataset.theme==='dark')delete r.dataset.theme;else r.dataset.theme='dark';try{{localStorage.setItem(k,r.dataset.theme==='dark'?'dark':'light')}}catch(e){{}}sync()}})}})}})();</script>
<title>A casa, junta · espécime · Ordenações Filipinas</title>
<link rel="stylesheet" href="../courses/direito-latino-americano/assets/curso.css">
<link rel="stylesheet" href="../assets/front.css">
<link rel="stylesheet" href="../assets/casa.css">
<style>
.casa-col{{width:min(1083px,calc(100vw - 96px));margin:26px auto 0}}
@media(max-width:1099px){{.casa-col{{width:calc(100vw - 32px)}}}}
.casa-col p{{font-size:19px;line-height:1.62;margin:0 0 1.05em;max-width:none}}
.casa-col h3{{font:750 22px/1.2 var(--sans);margin:1.6em 0 .5em}}
.casa-ch{{width:min(1083px,calc(100vw - 96px));max-width:none;margin:0 auto;padding:56px 0 0}}
.dial{{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 94%,transparent);border-bottom:1.5px solid var(--ink)}}
.dial>div{{width:min(1083px,calc(100vw - 96px));margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px;padding:10px 0;font:500 11px var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}}
.dial button{{font:inherit;letter-spacing:inherit;text-transform:inherit;padding:6px 12px;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);cursor:pointer}}
.dial button[aria-pressed="true"]{{background:var(--ink);color:var(--paper)}}
.dial .dial-note{{margin-left:auto;color:var(--muted)}}
.legenda{{list-style:none;margin:34px auto 0;padding:0;width:min(1083px,calc(100vw - 96px));border-top:1.5px solid var(--ink)}}
.legenda li{{display:grid;grid-template-columns:minmax(170px,1.1fr) 2fr 1.4fr;gap:14px;align-items:baseline;padding:11px 0;border-bottom:1px solid var(--grid-major);font:400 16px/1.4 var(--serif)}}
.legenda .k-sample{{font-size:19px}}
.legenda .k-rule{{font:500 11px/1.4 var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}}
@media(max-width:760px){{.legenda li{{grid-template-columns:1fr}}}}
.annot{{width:min(1083px,calc(100vw - 96px));margin:38px auto 10px;padding-top:10px;border-top:1.5px dashed var(--ink-2);font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}}
.annot b{{color:var(--conc);font-weight:600}}
.casa-fig{{width:min(1083px,calc(100vw - 96px));margin:34px auto;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);padding:18px 18px 12px}}
.casa-fig svg{{display:block;width:100%;height:auto}}
.casa-fig figcaption{{margin-top:10px;font:500 11px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}}
.casa .bet,.casa .quiz,.casa-reg{{width:min(1083px,calc(100vw - 96px));margin-left:auto;margin-right:auto;padding-left:0;padding-right:0}}
.casa .bet>div{{max-width:none}}
.casa-reg{{max-width:none}}
@media(max-width:1099px){{.casa-fig,.annot,.legenda,.dial>div,.casa .bet,.casa .quiz,.casa-reg,.casa-ch{{width:calc(100vw - 32px)}}}}
</style>
</head>
<body class="casa" data-int="proposto">
<nav class="topbar"><a href="../index.html">← Ordenações</a><span>Espécime · estilo da casa</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero">
  <div class="kicker label"><span>Espécime</span><span>CASA-1</span><span>06/10</span></div>
  <h1><span class="split">A casa,</span><span class="split">junta</span></h1>
</header>
<div class="dial" role="group" aria-label="Intensidade das marcas"><div><span>Marcas no texto</span><button type="button" data-int="discreto" aria-pressed="false">Discreto</button><button type="button" data-int="proposto" aria-pressed="true">Proposto</button><button type="button" data-int="forte" aria-pressed="false">Forte</button><span class="dial-note">Aula 05 · Gelman, texto verbatim</span></div></div>
<ul class="legenda" aria-label="Chave das marcas">{key_html}</ul>
<section class="chapter casa-ch" aria-labelledby="c2"><span class="num" aria-hidden="true">02</span><h2 id="c2">O que a Corte Interamericana decidiu</h2><p class="lede">As anistias para graves violações não têm efeito jurídico, venham de onde vierem.</p></section>
<div class="casa-col">
<p>{PROSE_1}</p>
<p>{PROSE_2}</p>
{SRC_238}
<p>{PROSE_3}</p>
{SRC_239}
</div>
<figure class="casa-fig"><svg viewBox="0 0 1080 170" role="img" aria-label="Linha do tempo do caso Gelman">{fork[fork.index('>')+1:]}<figcaption>Fig. 1 · A lei, as duas consultas, a sentença</figcaption></figure>
<div class="casa-col">
<p>{PROSE_4}</p>
<p>{PROSE_5}</p>
<h3>{H3}</h3>
<p>{PROSE_6}</p>
<p>{PROSE_7}</p>
</div>
<div class="annot"><b>Variantes do bloco</b> · azul: texto operativo de decisão ou lei · laranja: o limite · tinta: livro ou doutrina</div>
<div class="casa-col">
{SRC_AUTO}
{SRC_LEI}
</div>
<div class="annot"><b>Aposta e teste</b> · a mesma ficha de papel dos blocos, sem barra</div>
{bet}
<div class="casa-col" style="margin-top:30px"></div>
{quiz}
<div class="annot"><b>Registro de aulas</b> · o instrumento de cada frente de curso</div>
{reg}
<div class="annot" style="margin-bottom:80px"><b>Recusado</b> · cor de partido nas comparações (colide com azul = decisão); notas laterais (a coluna de 1.083 px não deixa margem, e nota lateral é fonte falando fora do bloco)</div>
<script src="../courses/direito-latino-americano/assets/curso.js" defer></script>
<script>
document.querySelectorAll('.dial button').forEach(function(b){{b.addEventListener('click',function(){{document.body.dataset.int=b.dataset.int;document.querySelectorAll('.dial button').forEach(function(o){{o.setAttribute('aria-pressed',String(o===b))}})}})}});
document.querySelectorAll('.fonte [data-tr]').forEach(function(b){{b.addEventListener('click',function(){{var s=b.closest('.fonte'),t=s.querySelector('.tr'),show=t.hidden;t.hidden=!show;b.setAttribute('aria-expanded',String(show));b.textContent=show?'ocultar tradução':'ver tradução'}})}});
</script>
</body></html>
'''
(SITE / 'specimen/casa.html').write_text(html)
print('wrote', SITE / 'specimen/casa.html', len(html))
