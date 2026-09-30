"""Build study-card decks for the three 2026/2 new courses.

Usage: python3 cartoes.py [output-root]
The default output is this checkout's staging tree. The script never writes to
the publish checkout; pass a different staging root explicitly when needed.
"""
from __future__ import annotations

import argparse
import glob
import html
import importlib.util
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
BUILD = os.path.join(HERE, "build.py")
SPECS = os.path.join(HERE, "specs")
EXTRAS = os.path.join(WORK, "cartoes-2026-09-29", "extras")
DEFAULT_OUT = os.path.join(WORK, "staging", "courses")
COURSE_KEYS = {
    "processo-civil": "cufrgs-processo-civil-cartoes-v1",
    "constitucional": "cufrgs-constitucional-cartoes-v1",
    "metodologia": "cufrgs-metodologia-cartoes-v1",
}
COURSE_TITLES = {
    "processo-civil": "Processo Civil I-a",
    "constitucional": "Direito Constitucional I",
    "metodologia": "Metodologia Jurídica",
}


def manifest():
    spec = importlib.util.spec_from_file_location("newcourses_build", BUILD)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.COURSES


def safe_json(value):
    # Keep JSON data inert inside a script element as well as valid Unicode JS.
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            .replace("<", "\\u003c").replace(">", "\\u003e")
            .replace("&", "\\u0026").replace("\u2028", "\\u2028")
            .replace("\u2029", "\\u2029"))


def load_cards(cname, course):
    specs = os.path.join(SPECS, cname)
    lessons = {}
    cards = []
    for key, *_ in course["lessons"]:
        with open(os.path.join(specs, key + ".json"), encoding="utf-8") as f:
            lesson = json.load(f)
        lessons[key] = lesson
        page = lesson["pages"][0]
        for question, answer in lesson.get("quiz", []):
            cards.append({"a": key, "t": page["title"], "q": question, "r": answer,
                          "href": page["file"]})

    for path in sorted(glob.glob(os.path.join(EXTRAS, cname + "-*.json"))):
        with open(path, encoding="utf-8") as f:
            shard = json.load(f)
        if not isinstance(shard, list):
            raise ValueError(f"Expected a JSON array in {path}")
        for item in shard:
            key = str(item["key"])
            if key not in lessons:
                raise ValueError(f"Extra references unknown lesson {cname}/{key}: {path}")
            page = lessons[key]["pages"][0]
            cards.append({"a": key, "t": page["title"], "q": item["q"], "r": item["r"],
                          "href": page["file"]})
    return cards


def render(cname, slug, cards, storage_key):
    title = COURSE_TITLES[cname]
    data = safe_json(cards)
    escaped_title = html.escape(title)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<script>(function(){{var k='cufrgs-theme',r=document.documentElement;try{{if(localStorage.getItem(k)==='dark')r.dataset.theme='dark'}}catch(e){{}}document.addEventListener('DOMContentLoaded',function(){{var b=document.querySelector('.theme-toggle');if(!b)return;function sync(){{b.setAttribute('aria-pressed',r.dataset.theme==='dark')}}sync();b.addEventListener('click',function(){{var d=r.dataset.theme!=='dark';if(d)r.dataset.theme='dark';else delete r.dataset.theme;try{{localStorage.setItem(k,d?'dark':'light')}}catch(e){{}}sync()}})}})}})()</script>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cartões · {escaped_title}</title>
<meta name="description" content="Cartões de estudo de {escaped_title}, com repetição espaçada.">
<link rel="stylesheet" href="assets/curso.css">
<style>
.deck-wrap{{max-width:820px;margin:0 auto;padding:0 clamp(16px,4vw,48px) 40px}}
.deck-tools{{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:8px 0 18px}}
.deck-tools button,.deck-tools select{{min-height:38px;padding:6px 12px;border:1px solid var(--ink);background:var(--paper);color:var(--ink);font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;cursor:pointer}}
.deck-tools button[aria-pressed="true"]{{background:var(--ink);color:var(--paper)}}
.deck-tools select{{flex:1 1 180px;min-width:0;max-width:100%}}
.deck-tools .count{{flex:1 0 100%;font:11px var(--mono);letter-spacing:.08em;color:var(--muted);text-transform:uppercase}}
.card-box{{border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);min-height:320px;display:flex;flex-direction:column}}
.card-box .meta{{display:flex;justify-content:space-between;gap:10px;padding:10px 16px;border-bottom:1px solid var(--ink);font:10px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}}
.card-box .meta a{{color:inherit}}.card-box .q{{padding:22px 22px 10px;font:650 clamp(19px,2.4vw,24px)/1.3 var(--sans)}}
.card-box .r{{margin:0 22px 18px;padding:14px 16px;border-left:3px solid var(--dif);background:var(--paper-2);font-size:17px;line-height:1.55}}
.card-box .r[hidden],.card-box .acts button[hidden]{{display:none}}
.card-box .acts{{margin-top:auto;display:flex;gap:10px;flex-wrap:wrap;padding:14px 16px;border-top:1px solid var(--ink)}}
.card-box .acts button{{flex:1 1 140px;min-height:46px;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:600 15px var(--sans);cursor:pointer}}
.card-box .acts .ok{{border-color:var(--dif);color:var(--dif)}}.card-box .acts .no{{border-color:var(--conc);color:var(--conc)}}
.deck-bar{{height:4px;background:var(--grid);margin:0 0 16px}}.deck-bar i{{display:block;height:100%;background:var(--conc);width:0;transition:width .3s}}
.deck-done{{padding:28px 22px;font-size:18px}}.kbd{{font:10px var(--mono);letter-spacing:.06em;color:var(--muted);margin-top:12px}}
@media(max-width:560px){{.deck-tools{{gap:8px}}.card-box{{min-height:300px}}.card-box .q{{padding:20px 18px 10px}}.card-box .r{{margin:0 18px 16px}}}}
</style></head>
<body>
<nav class="topbar"><a href="index.html">← {escaped_title}</a><span>Cartões</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero"><div class="kicker label"><span>Modo prova</span><span>{len(cards)} perguntas das aulas</span><span>{escaped_title}</span></div><h1><span class="split">Cartões</span><span class="split">de estudo</span></h1><p class="deck">Leia a pergunta, responda de cabeça, abra a resposta e marque se acertou. O intervalo cresce quando você acerta e recomeça quando erra.</p></header>
<div class="deck-wrap"><div class="deck-tools"><select id="aula" aria-label="Filtrar por aula"><option value="">Todas as aulas</option></select><button type="button" id="shuffle">Embaralhar</button><button type="button" id="reset">Zerar progresso</button><span class="count" id="count" aria-live="polite"></span></div>
<div class="deck-bar" aria-hidden="true"><i id="bar"></i></div><div class="card-box" aria-live="polite"><div class="meta"><span id="where"></span><span id="pos"></span></div><div class="q" id="q"></div><div class="r" id="r" hidden></div><div class="acts"><button type="button" id="show">Mostrar resposta</button><button type="button" class="no" id="no" hidden>Errei · rever depois</button><button type="button" class="ok" id="ok" hidden>Acertei</button></div></div>
<p class="kbd">Atalhos: espaço mostra a resposta · 1 errei · 2 acertei</p></div>
<nav class="endnav" aria-label="Navegação do curso"><a href="index.html"><span>Curso</span>Voltar ao índice</a><a href="{html.escape(cards[0]['href'] if cards else 'index.html')}" style="text-align:right"><span>Primeira aula</span>Começar o curso</a></nav>
<script>
(function(){{'use strict';var ALL={data},KEY={safe_json(storage_key)},DAY=86400000,INTERVALS=[0,DAY,3*DAY,7*DAY,16*DAY],aula='',queue=[],done=0,right=0,cur=null,state={{}};
var $=function(id){{return document.getElementById(id)}};
function hash(s){{var h=2166136261;for(var i=0;i<s.length;i++){{h^=s.charCodeAt(i);h=Math.imul(h,16777619)}}return('00000000'+(h>>>0).toString(16)).slice(-8)}}
ALL.forEach(function(c){{c.id=hash(c.a+'|'+c.q)}});
try{{var saved=JSON.parse(localStorage.getItem(KEY)||'null');if(saved&&typeof saved==='object'&&!Array.isArray(saved))state=saved}}catch(e){{}}
var sel=$('aula'),seen={{}};ALL.forEach(function(c){{if(!seen[c.a]){{seen[c.a]=true;var o=document.createElement('option');o.value=c.a;o.textContent='Aula '+c.a+' · '+c.t;sel.appendChild(o)}}}});
function shuffle(a){{for(var i=a.length-1;i>0;i--){{var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}}return a}}
function pool(){{return ALL.filter(function(c){{return !aula||c.a===aula}})}}
function save(){{try{{localStorage.setItem(KEY,JSON.stringify(state))}}catch(e){{}}}}
function tally(){{var now=Date.now(),due=0,fresh=0;pool().forEach(function(c){{var s=state[c.id];if(!s)fresh++;else if(!Number.isFinite(+s.due)||+s.due<=now)due++}});$('count').textContent=due+' para revisar hoje · '+fresh+' novas'}}
function build(){{var now=Date.now(),due=[],fresh=[],later=[];pool().forEach(function(c){{var s=state[c.id];if(!s)fresh.push(c);else if(!Number.isFinite(+s.due)||+s.due<=now)due.push(c);else later.push(c)}});queue=due.length||fresh.length?shuffle(due).concat(shuffle(fresh)):shuffle(later);done=0;right=0;tally();next()}}
function next(){{var total=done+queue.length;$('bar').style.width=(total?Math.round(100*done/total):0)+'%';if(!queue.length){{$('where').textContent='Fim da pilha';$('pos').textContent='';$('q').textContent='Pilha concluída. Você acertou '+right+' de primeira. Os cartões voltam quando vencer o intervalo de cada um.';$('r').hidden=true;$('show').hidden=$('ok').hidden=$('no').hidden=true;return}}cur=queue[0];var link=document.createElement('a');link.href=cur.href;link.textContent='Aula '+cur.a;$('where').replaceChildren(link,document.createTextNode(' · '+cur.t));$('pos').textContent=(done+1)+' / '+total;$('q').textContent=cur.q;$('r').textContent=cur.r;$('r').hidden=true;$('show').hidden=false;$('ok').hidden=$('no').hidden=true}}
function show(){{if(!cur||!$('r').hidden)return;$('r').hidden=false;$('show').hidden=true;$('ok').hidden=$('no').hidden=false;$('ok').focus()}}
function mark(ok){{if(!cur||$('r').hidden)return;queue.shift();var old=state[cur.id],box=old?Math.max(1,Math.min(5,parseInt(old.box,10)||1)):1;if(ok){{box=Math.min(5,box+1);done++;right++}}else{{box=1;queue.push(cur)}}state[cur.id]={{box:box,due:Date.now()+INTERVALS[box-1]}};save();tally();next()}}
$('show').onclick=show;$('ok').onclick=function(){{mark(true)}};$('no').onclick=function(){{mark(false)}};$('shuffle').onclick=build;sel.onchange=function(){{aula=sel.value;build()}};$('reset').onclick=function(){{if(!window.confirm('Zerar o progresso dos cartões?'))return;state={{}};try{{localStorage.removeItem(KEY)}}catch(e){{}}build()}};
document.addEventListener('keydown',function(e){{if(e.target.tagName==='SELECT'||e.target.tagName==='BUTTON'||e.metaKey||e.ctrlKey)return;if(e.key===' '&&$('r').hidden&&cur){{e.preventDefault();show()}}else if(e.key==='1')mark(false);else if(e.key==='2')mark(true)}});build()}})();
</script></body></html>'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_root", nargs="?", default=DEFAULT_OUT,
                        help="staging courses root (defaults to this checkout's work/staging/courses)")
    args = parser.parse_args()
    courses = manifest()
    for cname, key in COURSE_KEYS.items():
        course = courses[cname]
        cards = load_cards(cname, course)
        target = os.path.join(os.path.abspath(args.output_root), course["slug"], "cartoes.html")
        course_dir = os.path.dirname(target)
        asset_dir = os.path.join(course_dir, "assets")
        os.makedirs(asset_dir, exist_ok=True)
        css_src = os.path.join(args.output_root, "direito-latino-americano", "assets", "curso.css")
        if not os.path.isfile(css_src):
            raise FileNotFoundError(f"Staging house stylesheet not found: {css_src}")
        shutil.copyfile(css_src, os.path.join(asset_dir, "curso.css"))
        with open(target, "w", encoding="utf-8") as f:
            f.write(render(cname, course["slug"], cards, key))
        print(f"{cname}: {len(cards)} cards -> {target}")


if __name__ == "__main__":
    main()
