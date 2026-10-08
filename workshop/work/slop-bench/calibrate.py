#!/usr/bin/env python3
"""Pick each RATE rule's limit from data: the smallest per-1000 limit at which <=10% of human doctrine documents
would alarm; report the share of our pages still caught. CEO 06/10."""
import os, sys, re, tempfile
sys.path.insert(0, os.path.dirname(__file__)); import backtest as B; import slop_lint as L
def per_doc(docs):
    out = []
    with tempfile.TemporaryDirectory() as d:
        for i, (_, t) in enumerate(docs):
            p = os.path.join(d, f'{i}.txt'); open(p, 'w').write(t); r = L.lint(p, None)
            out.append({k: v['per_1000'] for k, v in r['density'].items()})
    return out
H = per_doc(B.human_docs('tune') + B.human_docs('holdout')); P = per_doc(B.model_docs('tune') + B.model_docs('holdout'))
print(f'{"rule":22} {"now":>5} {"p90 human":>9} {"pick":>5} {"human%":>6} {"pages%":>6}')
for rule, (_, limit, _) in L.RATE.items():
    if rule in ('paren-scarcity', 'uniform-paragraphs'): continue
    hv = sorted(d.get(rule, 0) for d in H); p90 = hv[int(0.9 * len(hv))]
    pick = max(limit, round(p90 + 0.05, 2))
    h = sum(d.get(rule, 0) > pick for d in H) / len(H); pg = sum(d.get(rule, 0) > pick for d in P) / len(P)
    print(f'{rule:22} {limit:5} {p90:9} {pick:5} {h*100:6.1f} {pg*100:6.1f}')
