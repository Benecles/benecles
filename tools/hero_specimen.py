"""Hero specimen: the Aula 01 (Controle) opening in switchable compositions, for the chairman to compare.

Run: python3 tools/hero_specimen.py  ->  specimen/hero.html
The hero markup is copied from the live page; only the composition CSS differs per variant.
"""
import os, re

ROOT = os.path.join(os.path.dirname(__file__), '..')
PAGE = os.path.join(ROOT, 'courses', 'controle-de-constitucionalidade', 'aula-01.html')

VARIANTS = [
    ('atual', 'Atual', 'Título grande na frente; o desenho vem depois do texto.'),
    ('desenho', 'Desenho à frente', 'Título menor; o desenho logo abaixo dele, no meio da tela; o texto de apoio depois.'),
    ('cartaz', 'Cartaz', 'Tudo centrado: título, desenho largo e o texto de apoio como legenda.'),
]

CSS = """
body{margin:0}
.switch{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:10px 16px;background:var(--paper);border-bottom:1.5px solid var(--ink);font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
.switch button{font:inherit;letter-spacing:inherit;text-transform:inherit;color:var(--ink);background:none;border:1px solid var(--rule);padding:6px 10px;cursor:pointer}
.switch button[aria-pressed=true]{border-color:var(--ink);background:var(--ink);color:var(--paper)}
.switch .why{flex-basis:100%;text-transform:none;letter-spacing:0;font:14px/1.4 var(--serif, Georgia, serif);color:var(--ink-2)}
.fold{max-width:1180px;margin:0 auto;border-top:1px dashed var(--conc);font:10px var(--mono);color:var(--conc);text-align:right;padding:2px 48px;letter-spacing:.08em;text-transform:uppercase}

/* Desenho à frente: the drawing is the centre of the first screen; the title sits above it, smaller */
body[data-v=desenho] header.hero{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:40px;align-items:end}
body[data-v=desenho] .hero .kicker{grid-column:1/-1;grid-row:1}
body[data-v=desenho] .hero h1{grid-column:1/-1;grid-row:2;font-size:clamp(40px,4.6vw,66px);max-width:none;margin:22px 0 0}
body[data-v=desenho] .hero-fork{grid-column:1/-1;grid-row:3;margin:30px 0 26px}
body[data-v=desenho] .hero .deck{grid-column:1;grid-row:4;font-size:clamp(18px,1.7vw,21px);max-width:52ch}
body[data-v=desenho] .titleblock{grid-column:2;grid-row:4;margin-top:0}

/* Cartaz: centred poster; the deck reads as the drawing's caption */
body[data-v=cartaz] header.hero{display:flex;flex-direction:column;align-items:center;text-align:center}
body[data-v=cartaz] .hero .kicker{justify-content:center;align-self:stretch}
body[data-v=cartaz] .hero h1{order:1;font-size:clamp(42px,5.6vw,80px);max-width:16ch;margin:24px 0 0}
body[data-v=cartaz] .hero-fork{order:2;margin:34px 0 22px}
body[data-v=cartaz] .hero .deck{order:3;font-size:clamp(18px,1.7vw,21px);max-width:56ch}
body[data-v=cartaz] .titleblock{order:4;margin-top:28px}
"""


def main():
    h = open(PAGE, encoding='utf-8').read()
    hero = re.search(r'<header class="hero">.*?</header>', h, re.S).group(0)
    css = re.search(r'href="(assets/controle\.css[^"]*)"', h).group(1)
    buttons = ''.join(f'<button type="button" data-v="{k}" data-why="{w}">{n}</button>' for k, n, w in VARIANTS)
    page = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Abertura de aula · amostras</title>
<link rel="stylesheet" href="../courses/controle-de-constitucionalidade/{css}">
<style>{CSS}</style></head><body data-v="atual">
<div class="switch" role="group" aria-label="Composição da abertura"><span>Abertura · Controle, Aula 01</span>{buttons}<span class="why"></span></div>
{hero}
<div class="fold">dobra de uma tela de 900 px</div>
<script>
const b=document.body, why=document.querySelector('.why'), btns=[...document.querySelectorAll('.switch button')];
function set(v){{b.dataset.v=v;btns.forEach(x=>x.setAttribute('aria-pressed',x.dataset.v===v));why.textContent=btns.find(x=>x.dataset.v===v).dataset.why;
  try{{localStorage.setItem('hero-v',v)}}catch(e){{}}
  const f=document.querySelector('.fold'), top=900-document.querySelector('.switch').offsetHeight; f.style.position='absolute';f.style.left=0;f.style.right=0;f.style.top=(document.querySelector('.switch').offsetHeight+top)+'px';
  document.querySelectorAll('.hero-fork .draw,.hero-fork .pop,.hero-fork .late').forEach(e=>{{e.style.animation='none';e.offsetWidth;e.style.animation=''}});}}
btns.forEach(x=>x.onclick=()=>set(x.dataset.v));
let v='atual';try{{v=localStorage.getItem('hero-v')||v}}catch(e){{}}set(btns.some(x=>x.dataset.v===v)?v:'atual');
</script></body></html>'''
    out = os.path.join(ROOT, 'specimen', 'hero.html')
    open(out, 'w', encoding='utf-8').write(page)
    print(out)


if __name__ == '__main__':
    main()
