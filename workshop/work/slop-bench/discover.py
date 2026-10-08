#!/usr/bin/env python3
"""Model-specific overuse discovery (Antislop / slop-lint idea, CEO 06/10): words and bigrams our model texts use
far more than human Portuguese doctrine. Output feeds candidate vocabulary rules; each still needs a reason to ship."""
import collections, math, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import backtest as B
STOP = set('a o as os de da do das dos e em no na nos nas um uma uns umas que se por para com como ao aos à às ou mais não é foi ser são pelo pela pelos pelas sua seu suas seus isso este esta esse essa entre também já há quando sobre até mas lhe sem'.split())
def toks(t): return [w for w in re.findall(r'[a-záéíóúâêôãõçà]+', t.lower())]
def counts(docs):
    u = collections.Counter(); b = collections.Counter(); n = 0
    for _, t in docs:
        w = toks(t); n += len(w); u.update(x for x in w if x not in STOP and len(x) > 3)
        b.update(f'{x} {y}' for x, y in zip(w, w[1:]) if not (x in STOP and y in STOP))
    return u, b, n
def top(m, h, mn, hn, k=30, minc=6):
    out = []
    for w, c in m.items():
        if c < minc: continue
        r = (c / mn) / ((h[w] + 0.5) / hn)
        out.append((round(r, 1), c, h[w], w))
    return sorted(out, reverse=True)[:k]
if __name__ == '__main__':
    hu, hb, hn = counts(B.human_docs('tune') + B.human_docs('holdout'))
    for label, docs, minc in (('LIVE PAGES (Codex/Claude, cleaned)', B.model_docs('tune') + B.model_docs('holdout'), 25), ('RAW HAIKU (unedited)', B.raw_docs(), 4)):
        mu, mb, mn = counts(docs)
        print(f'\n== {label}: {mn} tokens vs human {hn}')
        print('words  :', ', '.join(f'{w} ×{r} ({c}/{h})' for r, c, h, w in top(mu, hu, mn, hn, 30, minc)))
        print('bigrams:', ', '.join(f'{w} ×{r} ({c}/{h})' for r, c, h, w in top(mb, hb, mn, hn, 30, minc)))
