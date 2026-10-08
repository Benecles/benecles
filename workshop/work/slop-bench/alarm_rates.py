#!/usr/bin/env python3
"""Per-rule alarm rates: share of documents where a rule fires (HARD) or exceeds its limit (RATE).
False-alarm rate = on human doctrine; hit rate = on our pages (tune+holdout) and raw drafts. CEO 06/10."""
import os, sys, tempfile, collections
sys.path.insert(0, os.path.dirname(__file__)); import backtest as B; import slop_lint as L
def alarms(docs):
    c = collections.Counter()
    with tempfile.TemporaryDirectory() as d:
        for i, (_, t) in enumerate(docs):
            p = os.path.join(d, f'{i}.txt'); open(p, 'w').write(t)
            r = L.lint(p, None); fired = set()
            for f in r['findings']:
                if f.get('severity') == 'hard' or f.get('over_limit'): fired.add(f['rule'])
            c.update(fired)
    return {k: v / len(docs) for k, v in c.items()}, len(docs)
H, hn = alarms(B.human_docs('tune') + B.human_docs('holdout')); P, pn = alarms(B.model_docs('tune') + B.model_docs('holdout')); R, rn = alarms(B.raw_docs())
print(f'docs: human {hn}, pages {pn}, raw {rn}\n{"rule":24} {"human%":>7} {"pages%":>7} {"raw%":>6}')
for rule in list(L.HARD) + list(L.RATE):
    h, p, r = H.get(rule, 0), P.get(rule, 0), R.get(rule, 0)
    flag = '  <- false alarms' if h >= 0.10 else ''
    print(f'{rule:24} {h*100:6.1f} {p*100:7.1f} {r*100:6.1f}{flag}')
