#!/usr/bin/env python3
"""Controle house-style roll-out helper (site repo root).
  controle_casa.py list  NN      plain <strong> in running text, with context (decide each by reading)
  controle_casa.py apply NN      head links + .law/.julgado -> .fonte + unwrap bold inside the new blocks
  controle_casa.py unwrap NN 'phrase' ...   unwrap <strong> whose text starts with each phrase ('*' = all left)
Text is moved, never edited. .julgado boxes are summaries, not quotes: they become .fonte.resumo with
<div class="corpo">, never <blockquote> (a blockquote would put our words in the court's mouth)."""
import re, sys, pathlib

def page(nn): return pathlib.Path(f'courses/controle-de-constitucionalidade/aula-{int(nn):02d}.html')

def masked(s):
    """Positions of <strong> that marks_lint would flag (same container mask)."""
    t = re.sub(r'(?is)<(script|style|svg|head)\b.*?</\1>', lambda m: '#' * len(m.group(0)), s)
    for o, c in ((r'<header\b', r'</header>'), (r'<p class="deck"', r'</p>'), (r'<p class="eixo"', r'</p>'), (r'<div class="bet"', r'</div></div>'),
                 (r'<aside class="fonte', r'</aside>'), (r'<div class="titleblock', r'</div></div>'), (r'<table\b', r'</table>'), (r'<summary\b', r'</summary>'), (r'<nav\b', r'</nav>')):
        t = re.sub(r'(?is)' + o + r'.*?' + c, lambda m: '#' * len(m.group(0)), t)
    return [m for m in re.finditer(r'(?is)<strong>(?!\s*\w+(?: \w+){0,2}\.\s*</)(.*?)</strong>', t)]

def plain(x): return re.sub(r'<[^>]+>', '', x)

def lst(nn):
    s = page(nn).read_text()
    for i, m in enumerate(masked(s)):
        a = s.rfind('<p', 0, m.start()); b = s.find('</p>', m.end())
        ctx = plain(s[max(a, m.start() - 220):m.start()]) + '[[' + plain(m.group(1)) + ']]' + plain(s[m.end():min(b, m.end() + 120)])
        print(f'{i:3d} L{s.count(chr(10), 0, m.start()) + 1}: {" ".join(ctx.split())}\n')

def fonte_law(m):
    cite, body = m.group(1).strip(), m.group(2).strip()
    src, _, loc = cite.partition(', ')
    body = re.sub(r'</?strong>', '', body)
    h = f'<span>{src}</span>' + (f'<span class="loc">{loc}</span>' if loc else '')
    return f'<aside class="fonte dec" aria-label="Fonte: {cite}"><header>{h}</header><blockquote><p>{body}</p></blockquote></aside>'

def fonte_julgado(m):
    kind = 'lim' if 'conc' in (m.group(1) or '') else 'dec'
    a, b, corpo = m.group(2), m.group(3), m.group(4).strip()
    corpo = re.sub(r'</?strong>', '', corpo)
    return (f'<aside class="fonte {kind} resumo" aria-label="Resumo: {a}"><header><span>{a}</span><span class="loc">{b}</span></header>'
            f'<div class="corpo">{corpo}</div></aside>')

def apply(nn):
    p = page(nn); s = p.read_text()
    if 'casa.css' not in s:
        s = s.replace('<link rel="stylesheet" href="assets/controle.css', '<link rel="stylesheet" href="../../assets/casa.css"><link rel="stylesheet" href="assets/controle.css', 1)
        assert 'casa.css' in s, 'controle.css anchor not found'
    if 'casa.js' not in s:
        s = re.sub(r'(<script[^>]*highlight-panel\.js[^>]*></script>)', r'\1\n<script src="../../assets/casa.js" defer></script>', s, 1)
        if 'casa.js' not in s: s = s.replace('</body>', '<script src="../../assets/casa.js" defer></script>\n</body>', 1)
    s, nl = re.subn(r'(?s)<blockquote class="law"><cite>(.*?)</cite>(.*?)</blockquote>', fonte_law, s)
    s, nj = re.subn(r'(?s)<div class="julgado( [a-z]+)?">\s*<header><span>(.*?)</span><span>(.*?)</span></header>\s*<div class="corpo">(.*?)</div>\s*</div>', fonte_julgado, s)
    s = re.sub(r'(?s)<div class="julgados">\s*((?:<aside class="fonte[^"]*resumo.*?</aside>\s*)+)</div>', lambda m: m.group(1).strip(), s)
    p.write_text(s); print(f'aula-{int(nn):02d}: law {nl}, julgado {nj}, left: law {s.count("class=\"law")}, julgado {s.count("class=\"julgado")}')

def unwrap(nn, phrases):
    p = page(nn); s = p.read_text(); n = 0
    for m in reversed(masked(s)):
        txt = plain(m.group(1)).strip()
        if '*' in phrases or any(txt.startswith(ph) for ph in phrases):
            s = s[:m.start()] + m.group(1) + s[m.end():]; n += 1
    p.write_text(s); print('unwrapped', n, '· left', len(masked(s)))

if __name__ == '__main__':
    cmd, nn = sys.argv[1], sys.argv[2]
    {'list': lambda: lst(nn), 'apply': lambda: apply(nn), 'unwrap': lambda: unwrap(nn, sys.argv[3:])}[cmd]()
