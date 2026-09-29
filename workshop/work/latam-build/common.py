"""Shared setup for the Direito Latino-americano (DIR03057) course pages.
Writes into the study-lab publish checkout: courses/direito-latino-americano/."""
import sys
sys.path.insert(0, '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/contract-build/generators')
import kit
from kit import *

kit.OUT = '/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/direito-latino-americano/'
kit.COURSE = 'Direito Latino-americano'
kit.VER = '20260927h'

EXTRA_CSS = ('.longform{max-width:1180px;margin:28px auto 12px;padding:0 clamp(16px,4vw,48px)}'
             '.longform>div{max-width:66ch}'
             '.longform p{font-size:19px;line-height:1.62;margin:0 0 1.05em}'
             '.longform h3{font:750 22px/1.2 var(--sans);margin:1.6em 0 .5em}'
             '.lex{margin:6px 0 22px;padding:2px 0 2px 16px;border-left:3px solid var(--dif);font-size:17px;line-height:1.55;color:var(--ink-2)}'
             '.lex b{font:600 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--dif);display:block;margin-bottom:2px}'
             '.lex.conc{border-left-color:var(--conc)}.lex.conc b{color:var(--conc)}'
             '.eixo{margin:26px 0 8px;padding:14px 18px;border:1.5px solid var(--ink);background:var(--paper);box-shadow:4px 4px 0 var(--grid-major);font:600 19px/1.4 var(--sans)}'
             '.eixo b{display:block;font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--conc);margin-bottom:6px}'
             '@media (max-width:560px){.longform p{font-size:18px}.eixo{font-size:17px}}')

def longform(*paras):
    return '<div class="longform"><div>' + ''.join(paras) + '</div></div>\n'

def lex(label, text, tone=''):
    return f'<p class="lex {tone}"><b>{label}</b>{text}</p>'

def eixo(text, label='Eixo de discussão da aula'):
    return f'<p class="eixo"><b>{label}</b>{text}</p>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)

KICK = ['Direito Latino-americano', 'DIR03057', 'UFRGS · 2026/2']

def lesson(n, fname, title, desc, h1a, h1b, deck, hero, tb, body, prev, nxt, date, **kw):
    page(fname, n, title, desc, KICK, h1a, h1b, deck, hero, tb, body, prev, nxt,
         extra_css=EXTRA_CSS, toplabel=f'Aula {n} · {date}', **kw)

def bet(question, options, reveal, kicker='Antes de ler: como você decidiria?'):
    """options: list of (text, who) where who is '' or the court/judges that took that side; mark the
    winning side's who with a leading '*' (e.g. '*STF, 7 votos')."""
    btns = ''
    for i, (text, who) in enumerate(options):
        court = who.startswith('*')
        w = who.lstrip('*')
        btns += (f'<button type="button" data-opt="{i}"' + (' data-court' if court else '') + ' aria-pressed="false">'
                 + text + (f'<span class="who">{w}</span>' if w else '') + '</button>')
    return (f'<div class="bet"><div><span class="bet-k">{kicker}</span><p class="bet-q">{question}</p>'
            f'<div class="bet-opts">{btns}</div><div class="bet-reveal">{reveal}</div></div></div>\n')

# ---- depth additions (Codex/Luna drafts in work/depth/latam/aula-NN-add.md), merged as an "Aprofundamento" chapter
import os as _os, re as _re, html as _html
DEPTH = '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/depth/latam/'
def _inline(t):
    t = _html.escape(t, quote=False)
    t = _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = _re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', t)
    return t.replace('Near miss probatório', 'Armadilha de prova').replace('Near miss', 'Armadilha').replace('near miss', 'armadilha')
def deepen(n, skip=()):
    p = _os.path.join(DEPTH, f'aula-{n}-add.md')
    if not _os.path.exists(p): return ''
    secs, cur = [], None
    for line in open(p).read().split('\n'):
        if line.startswith('# '): continue
        if line.startswith('## '):
            cur = [line[3:].strip(), []]; secs.append(cur); continue
        if cur is not None: cur[1].append(line)
    out = []
    for title, lines in secs:
        if title.lower().startswith('integração editorial') or any(title.startswith(k) for k in skip): continue
        out.append(f'<h3>{_inline(title)}</h3>')
        para, items = [], []
        def flush():
            if para: out.append('<p>' + _inline(' '.join(para)) + '</p>'); para.clear()
            if items: out.append('<ul>' + ''.join(f'<li>{_inline(i)}</li>' for i in items) + '</ul>'); items.clear()
        for l in lines + ['']:
            s = l.strip()
            if not s: flush(); continue
            if s.startswith('### '): flush(); out.append(f'<h3>{_inline(s[4:])}</h3>'); continue
            if s.startswith('- '): 
                if para: flush()
                items.append(s[2:]); continue
            para.append(s)
    return longform(*out) if out else ''
def deep_chapter(n, num, skip=()):
    body = deepen(n, skip)
    if not body: return ''
    return chapter(num, f'c{int(num)}', 'Aprofundamento', 'Mais posições, casos e distinções para a atividade.', 'dif') + body
