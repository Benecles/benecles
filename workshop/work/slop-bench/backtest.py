#!/usr/bin/env python3
"""Backtest every slop_lint rule: human Portuguese legal doctrine vs our LLM-written lesson pages (CEO, 06/10).
A rule earns its place only if it fires clearly more on the model pages than on human doctrine (bheijden/slop method).
Split: TUNE (most sources/courses) vs HOLDOUT (sources and courses never used for tuning) so thresholds are checked out of sample.
usage: backtest.py [--write report]"""
import glob, os, re, sys, json, tempfile, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(WS, 'protocols', 'tools'))
import slop_lint
SITE = os.path.expanduser('~/Developer/ordenacoes-filipinas/courses')
CH = os.path.join(WS, 'work', 'pipeline', '*', 'chapters')
HUMAN = {'tune': ['mendes-branco-curso-2023', 'sarlet-marinoni-mitidiero-curso-2020', 'tavares-curso-2020', 'jose-afonso-curso-2016',
                  'dimoulis-lunardi-processo-constitucional', 'barroso-controle-2012', 'adpf347-eci-article'],
         'holdout': ['bonavides-curso-2011', 'gilmar-aspectos-juridicos-politicos', 'lenza-esquematizado-2022', 'engelmann-bandeira-2017', 'justica-transicao-brasil-colombia']}
MODEL = {'holdout': ['teoria-geral-dos-contratos', 'metodologia-juridica']}   # every other course tunes
CHUNK, CAP = 2500, 40
random.seed(7)

def human_docs(split):
    docs = []
    for src in HUMAN[split]:
        words = []
        for f in sorted(glob.glob(os.path.join(CH, src, '*.txt'))):
            t = open(f, errors='ignore').read()
            t = re.sub(r'^=====.*$', '', t, flags=re.M)
            words += t.split()
        chunks = [' '.join(words[i:i + CHUNK]) for i in range(0, len(words) - CHUNK // 2, CHUNK)]
        random.shuffle(chunks)
        docs += [(src, c) for c in chunks[:CAP]]
    return docs

def raw_docs():
    return [(os.path.basename(f), open(f).read()) for f in sorted(glob.glob(os.path.join(HERE, 'raw-haiku', 'g*.txt')))]

def model_docs(split):
    out = []
    for f in sorted(glob.glob(os.path.join(SITE, '*', '*.html'))):
        course = f.split('/')[-2]; name = os.path.basename(f)
        if name in ('index.html', 'cartoes.html') or not re.match(r'(aula|unidade|suplemento|revisao|parte)', name): continue
        if (course in MODEL['holdout']) != (split == 'holdout'): continue
        out.append((course, slop_lint.text_of(f)))
    return out

def run(docs):
    per = collections.defaultdict(lambda: [0, 0]); words = 0
    with tempfile.TemporaryDirectory() as d:
        for i, (_, text) in enumerate(docs):
            p = os.path.join(d, f'{i}.txt'); open(p, 'w').write(text)
            r = slop_lint.lint(p, None); words += r['words']
            c = collections.Counter(f['rule'] for f in r['findings'])
            for rule, n in c.items(): per[rule][0] += n; per[rule][1] += 1
    return per, words, len(docs)

def table(split):
    h, hw, hn = run(human_docs('tune' if split == 'raw' else split)); m, mw, mn = run(raw_docs() if split == 'raw' else model_docs(split))
    rows = []
    for rule in list(slop_lint.HARD) + list(slop_lint.RATE):
        hr = h[rule][0] * 1000 / max(hw, 1); mr = m[rule][0] * 1000 / max(mw, 1)
        hp = h[rule][1] / max(hn, 1); mp = m[rule][1] / max(mn, 1)
        ratio = (mr / hr) if hr else (float('inf') if mr else None)
        if mr == 0 and hr == 0: verdict = 'silent'
        elif hr >= mr: verdict = 'BACKWARDS'
        elif ratio is not None and ratio >= 2: verdict = 'keep'
        else: verdict = 'weak'
        rows.append((rule, round(hr, 3), round(mr, 3), None if ratio is None else (round(ratio, 2) if ratio != float('inf') else 'inf'), round(hp, 3), round(mp, 3), verdict))
    return rows, (hn, hw), (mn, mw)

if __name__ == '__main__':
    res = {}
    for split in ('tune', 'holdout', 'raw'):
        rows, hs, ms = table(split); res[split] = {'rows': rows, 'human': hs, 'model': ms}
        print(f'== {split}: human {hs[0]} docs/{hs[1]} words · model {ms[0]} pages/{ms[1]} words')
        print(f"{'rule':24} {'hum/1k':>7} {'mod/1k':>7} {'ratio':>6} {'hum%':>5} {'mod%':>5} verdict")
        for r in rows: print(f'{r[0]:24} {r[1]:7} {r[2]:7} {str(r[3]):>6} {r[4]:5} {r[5]:5} {r[6]}')
    json.dump(res, open(os.path.join(HERE, 'backtest.json'), 'w'), indent=1)
