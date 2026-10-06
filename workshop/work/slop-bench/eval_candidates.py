#!/usr/bin/env python3
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(__file__)); import backtest as B; from candidates import C
from difflib import SequenceMatcher
def self_repeat(t):
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) >= 10]
    sets = [set(re.findall(r'\w+', s.lower())) for s in sents]; n = 0
    for i in range(len(sets)):
        for j in range(max(0, i - 40), i):
            inter = len(sets[i] & sets[j]); uni = len(sets[i] | sets[j])
            if uni and inter / uni >= 0.7: n += 1; break
    return n
def stats(docs):
    rate = collections.Counter(); prev = collections.Counter(); w = 0
    for _, t in docs:
        w += len(t.split())
        for k, p in C.items():
            n = len(re.findall(p, t, re.I if k not in ('count-announce',) else 0)); rate[k] += n; prev[k] += n > 0
        n = self_repeat(t); rate['self-repeat'] += n; prev['self-repeat'] += n > 0
    return {k: (rate[k] * 1000 / w, prev[k] / len(docs)) for k in list(C) + ['self-repeat']}
H = stats(B.human_docs('tune') + B.human_docs('holdout')); P = stats(B.model_docs('tune') + B.model_docs('holdout')); R = stats(B.raw_docs())
print(f'{"candidate":20} {"hum/1k":>7} {"hum%":>6} {"pag/1k":>7} {"pag%":>6} {"raw/1k":>7} {"raw%":>6}')
for k in H:
    print(f'{k:20} {H[k][0]:7.3f} {H[k][1]*100:6.1f} {P[k][0]:7.3f} {P[k][1]*100:6.1f} {R[k][0]:7.3f} {R[k][1]*100:6.1f}')
