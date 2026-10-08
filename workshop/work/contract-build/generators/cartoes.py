import re, json, html as H
OUT = "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/teoria-geral-dos-contratos/"
cards = []
for n in range(1, 18):
    s = open(OUT + 'aula-%02d.html' % n).read()
    title = re.search(r'<title>(.*?) · Teoria', s).group(1)
    q = s[s.rindex('<div class="quiz">'):]
    q = q[:q.index('</div>')]
    for sm, ans in re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', q, re.S):
        cards.append({'a': '%02d' % n, 't': H.unescape(re.sub('<[^>]+>', '', title)), 'q': sm.strip(), 'r': ans.strip()})
print(len(cards), 'cards')
assert len(cards) > 60

p1 = open(OUT + 'revisao-p1.html').read()
head = p1[:p1.index('<style>')]
head = head.replace('<title>Revisão para a P1 · Teoria Geral dos Contratos</title>', '<title>Cartões de estudo · Teoria Geral dos Contratos</title>')
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Todas as perguntas das aulas de Teoria Geral dos Contratos em cartões: responda, confira e revise as que errou.">', head)

style = '''<style>
.deck-wrap{max-width:820px;margin:0 auto;padding:0 clamp(16px,4vw,48px) 40px}
.deck-tools{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:8px 0 18px}
.deck-tools button,.deck-tools select{min-height:38px;padding:6px 12px;border:1px solid var(--ink);background:var(--paper);color:var(--ink);font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;cursor:pointer}
.deck-tools button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.deck-tools select{flex:1 1 180px;min-width:0;max-width:100%}
.deck-tools .count{margin-left:auto;font:11px var(--mono);letter-spacing:.08em;color:var(--muted);text-transform:uppercase}
.card-box{position:relative;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);min-height:320px;display:flex;flex-direction:column}
.card-box .meta{display:flex;justify-content:space-between;gap:10px;padding:10px 16px;border-bottom:1px solid var(--ink);font:10px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.card-box .meta a{color:inherit}
.card-box .q{padding:22px 22px 10px;font:650 clamp(19px,2.4vw,24px)/1.3 var(--sans);letter-spacing:-.01em}
.card-box .r{margin:0 22px 18px;padding:14px 16px;border-left:3px solid var(--dif);background:var(--paper-2);font-size:17px;line-height:1.55;animation:fadein .35s ease both}
.card-box .r[hidden]{display:none}
.card-box .acts{margin-top:auto;display:flex;gap:10px;flex-wrap:wrap;padding:14px 16px;border-top:1px solid var(--ink)}
.card-box .acts button{flex:1 1 140px;min-height:46px;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:600 15px var(--sans);cursor:pointer}
.card-box .acts button:hover,.card-box .acts button:focus-visible{background:var(--paper-2)}
.card-box .acts .ok{border-color:var(--dif);color:var(--dif)}
.card-box .acts .no{border-color:var(--conc);color:var(--conc)}
.card-box .acts button[hidden]{display:none}
.deck-bar{height:4px;background:var(--grid);margin:0 0 16px}
.deck-bar i{display:block;height:100%;background:var(--conc);width:0;transition:width .3s}
.deck-done{padding:28px 22px;font-size:18px}
.deck-done b{font-family:var(--sans)}
.kbd{font:10px var(--mono);letter-spacing:.06em;color:var(--muted);margin-top:12px}
@keyframes fadein{from{opacity:0}}
</style>
</head>
'''
data = json.dumps(cards, ensure_ascii=False)
body = f'''<body>
<nav class="topbar"><a href="index.html">← Teoria Geral dos Contratos</a><span>Cartões</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero">
  <div class="kicker label"><span>Modo prova</span><span>{len(cards)} perguntas das aulas</span><span>Teoria Geral dos Contratos</span></div>
  <h1><span class="split">Cartões</span><span class="split">de estudo</span></h1>
  <p class="deck">Leia a pergunta, responda de cabeça, abra a resposta e marque se acertou. O intervalo cresce quando você acerta e recomeça quando erra.</p>
</header>
<div class="deck-wrap">
  <div class="deck-tools">
    <div role="group" aria-label="Filtrar por prova"><button type="button" data-f="all" aria-pressed="true">Todas</button> <button type="button" data-f="p1" aria-pressed="false">P1</button> <button type="button" data-f="p2" aria-pressed="false">P2</button></div>
    <select id="aula" aria-label="Filtrar por aula"><option value="">Todas as aulas</option></select>
    <button type="button" id="shuffle">Embaralhar</button>
    <button type="button" id="reset">Zerar progresso</button>
    <span class="count" id="count"></span>
  </div>
  <div class="deck-bar" aria-hidden="true"><i id="bar"></i></div>
  <div class="card-box" id="card" aria-live="polite">
    <div class="meta"><span id="where"></span><span id="pos"></span></div>
    <div class="q" id="q"></div>
    <div class="r" id="r" hidden></div>
    <div class="acts">
      <button type="button" id="show">Mostrar resposta</button>
      <button type="button" class="no" id="no" hidden>Errei · rever depois</button>
      <button type="button" class="ok" id="ok" hidden>Acertei</button>
    </div>
  </div>
  <p class="kbd">Atalhos: espaço mostra a resposta · 1 errei · 2 acertei</p>
</div>
<footer class="endnav"><a href="index.html"><span>Curso</span>Voltar ao índice</a><a href="artigos.html"><span>Consulta</span>Artigos do curso</a></footer>
<script>
(function(){{
  var ALL={data};
  var KEY='ordenacoes-contratos-cartoes-v1',DAY=86400000,INTERVALS=[0,DAY,3*DAY,7*DAY,16*DAY];
  var f='all',aula='',queue=[],done=0,right=0,cur=null,state={{}};
  var $=function(id){{return document.getElementById(id)}};
  function hash(t){{var h=2166136261;for(var i=0;i<t.length;i++){{h^=t.charCodeAt(i);h=Math.imul(h,16777619)}}return ('00000000'+(h>>>0).toString(16)).slice(-8)}}
  ALL.forEach(function(c){{c.id=hash(c.q)}});
  try{{var raw=localStorage.getItem(KEY),p=raw&&JSON.parse(raw);if(p&&typeof p==='object'&&!Array.isArray(p))state=p}}catch(e){{}}
  function save(){{try{{localStorage.setItem(KEY,JSON.stringify(state))}}catch(e){{}}}}
  var sel=$('aula'),seen={{}};ALL.forEach(function(c){{if(!seen[c.a]){{seen[c.a]=1;var o=document.createElement('option');o.value=c.a;o.textContent='Aula '+c.a+' · '+c.t;sel.appendChild(o)}}}});
  function shuffle(a){{for(var i=a.length-1;i>0;i--){{var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}}return a}}
  function pool(){{return ALL.filter(function(c){{var n=+c.a;return (f==='all'||(f==='p1'?n<=8:n>=9))&&(!aula||c.a===aula)}})}}
  function tally(){{var now=Date.now(),d=0,n=0;pool().forEach(function(c){{var s=state[c.id];if(!s)n++;else if(!(+s.due>now))d++}});$('count').textContent=d+' para revisar hoje · '+n+' novas'}}
  function build(){{
    var now=Date.now(),due=[],fresh=[],later=[];
    pool().forEach(function(c){{var s=state[c.id];if(!s)fresh.push(c);else if(!(+s.due>now))due.push(c);else later.push(c)}});
    queue=due.length||fresh.length?shuffle(due).concat(shuffle(fresh)):shuffle(later);
    done=0;right=0;tally();next();
  }}
  function next(){{
    var total=done+queue.length;
    $('bar').style.width=(total?Math.round(100*done/total):0)+'%';
    if(!queue.length){{
      $('where').textContent='Fim da pilha';$('pos').textContent='';
      $('q').innerHTML='<div class="deck-done"><b>Pilha concluída.</b> Você acertou '+right+' de primeira. Os cartões voltam quando vencer o intervalo de cada um.</div>';
      $('r').hidden=true;$('show').hidden=true;$('ok').hidden=true;$('no').hidden=true;return;
    }}
    cur=queue[0];
    $('where').innerHTML='<a href="aula-'+cur.a+'.html">Aula '+cur.a+'</a> · '+cur.t;
    $('pos').textContent=(done+1)+' / '+total;
    $('q').innerHTML=cur.q;$('r').innerHTML=cur.r;$('r').hidden=true;
    $('show').hidden=false;$('ok').hidden=true;$('no').hidden=true;
  }}
  function show(){{if(!cur||!$('r').hidden)return;$('r').hidden=false;$('show').hidden=true;$('ok').hidden=false;$('no').hidden=false;$('ok').focus()}}
  function mark(ok){{
    if(!cur||$('r').hidden)return;queue.shift();
    var old=state[cur.id],box=old?Math.max(1,Math.min(5,parseInt(old.box,10)||1)):1;
    if(ok){{box=Math.min(5,box+1);done++;right++}}else{{box=1;queue.push(cur)}}
    state[cur.id]={{box:box,due:Date.now()+INTERVALS[box-1]}};save();tally();next();
  }}
  $('show').onclick=show;$('ok').onclick=function(){{mark(true)}};$('no').onclick=function(){{mark(false)}};
  $('shuffle').onclick=build;sel.onchange=function(){{aula=sel.value;build()}};
  $('reset').onclick=function(){{if(!window.confirm('Zerar o progresso dos cartões?'))return;state={{}};try{{localStorage.removeItem(KEY)}}catch(e){{}}build()}};
  document.querySelectorAll('.deck-tools [data-f]').forEach(function(b){{b.onclick=function(){{f=b.getAttribute('data-f');document.querySelectorAll('.deck-tools [data-f]').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});build()}}}});
  document.addEventListener('keydown',function(e){{
    if(e.target.tagName==='SELECT'||e.target.tagName==='BUTTON'||e.metaKey||e.ctrlKey)return;
    if(e.key===' '&&$('r').hidden&&cur&&queue.length){{e.preventDefault();show()}}
    else if(e.key==='1')mark(false);else if(e.key==='2')mark(true);
  }});
  build();
}})();
</script>
</body>
</html>
'''
open(OUT + 'cartoes.html', 'w').write(head + style + body)
print('ok')
