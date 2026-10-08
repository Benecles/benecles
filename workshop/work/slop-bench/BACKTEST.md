# SLOP-3 backtest (CEO, 06/10)

**Question:** does each `slop_lint` rule fire clearly more on model prose than on human Portuguese legal doctrine?
**Corpora:** human = 368 documents of ~2,500 words from 12 doctrinal sources (Mendes, Sarlet, Tavares, José Afonso, Dimoulis, Barroso, Bonavides, Gilmar, Lenza, Engelmann & Bandeira, the ADPF 347 and transitional-justice articles; statutes, decisions, slides and the AI-built dossier excluded), split tune/holdout by source. Model = 170 live lesson pages (Codex/Claude, already linted: enforced rules read near zero there by selection) plus 18 **raw, unedited Haiku drafts** (`raw-haiku/`) to judge enforced rules fairly. Codex CLI could not generate (model unsupported on the ChatGPT account), so Codex-specific raw output is still missing.
**Method:** per-rule rate per 1,000 words and document prevalence (`backtest.py`); limits chosen as the smallest value with ≤10% of human documents alarming (`calibrate.py`); candidates from SlopDetector and tropes.fyi admitted only if they survive the same test (`candidates.py`, `eval_candidates.py`); alarm rates after tuning (`alarm_rates.py`).

## What changed
- **New house-tic rule `negated-inference`** ("não basta / substitui / resolve / autoriza / prova / transforma…"): pages 2.43/1k vs human 0.14/1k (~18×), on 92% of pages vs 25% of human docs. The single strongest discriminator found.
- **Limits set from data:** negative-parallelism HARD → RATE 2.0/1k; colon-reveal 2.5 → 5.6; triad-density 4 → 12.3; denial-restatement 0 → 1.6; stance-adverb 0 → 1.2.
- **Retired (measured backwards, off by default in `RETIRED`):** fragment-run, load-bearing-adverb.
- **Bands:** every finding now carries `band`: `tell` (evidence of model habit) or `style` (house rule human jurists also break: formulaic-metatext, ritual-conclusion, denial-restatement, stance-adverb, backstage, reader-address).
- **Ported and kept (SlopDetector + tropes.fyi):** tool-artifact, placeholder, chat-scaffolding, ai-self-reference, ritual-conclusion (style), challenges-future, evaluative-tail, count-announce, analogy-coach, where-it-lives, invented-label, stakes-inflation; RATE `ai-vocab-pt` (5.2/1k = human p90; raw drafts 7.5/1k vs human 2.2/1k).
- **Rejected after testing:** copula-avoidance ("configura-se como": human 15% of docs vs pages 0.6%), familiarity-appeal ("como se sabe": human 12%), self-repeat (only 1.8×; PDF headings inflate the human count) — left to the critic.
- **Tests:** adversarial false-positive set of legitimate legal sentences; a holdout test that fails if any tell rule alarms on >12% of held-out human doctrine (skips where the corpus is absent).
- **Side finding for Codex:** "slides" appears 24× on Controle lesson pages (backstage leak; the `backstage` rule flags 7.6% of pages).

## Alarm rates after tuning (share of documents)
```
docs: human 368, pages 170, raw 18
rule                      human%  pages%   raw%
puffery                     3.0     0.0    0.0
significance-gerund         0.8     0.0    0.0
formulaic-metatext         16.0     0.0    5.6  <- false alarms
vague-attribution           1.6     0.0    0.0
reader-address              0.8     0.0    0.0
AI-calque                   1.9     0.6    5.6
backstage                   0.8     7.6    0.0
teaser-hook                 0.0     0.0    0.0
self-labeling               0.3     0.0    0.0
hedge-stack                 0.5     0.0    0.0
false-concession            0.0     0.0    0.0
staged-objection            0.8     0.0    0.0
reader-steer-question       0.0     0.0    0.0
circular-because            0.0     0.0    0.0
tool-artifact               0.0     0.0    0.0
placeholder                 0.3     0.0    0.0
chat-scaffolding            0.0     0.0    0.0
ai-self-reference           0.0     0.0    0.0
ritual-conclusion           7.3     0.6    5.6
challenges-future           0.5     3.5    0.0
evaluative-tail             0.3     0.0    0.0
count-announce              0.0     2.4    0.0
analogy-coach               0.0     0.0    0.0
where-it-lives              0.0     0.0    0.0
invented-label              2.4     4.7    0.0
stakes-inflation            1.9     2.4   11.1
rhetorical-triad            1.6     0.0    0.0
negative-parallelism        7.3    42.4    0.0
negated-inference           6.5    77.6    5.6
colon-reveal                9.5    61.2   16.7
denial-restatement          4.6     2.9   22.2
rather-than                 0.0     1.2    0.0
triad-density               9.2    30.0   16.7
stance-adverb               5.2     1.8   11.1
negation-chain              0.0     0.0    0.0
same-opener-run             0.3     7.6    0.0
semicolon-correction        0.0     0.0    0.0
colon-appositive            0.0     0.0    0.0
nominalisation-pileup       0.0     0.0    0.0
stacked-questions           2.7    25.9    0.0
transition-opener           0.0     0.0    0.0
uniform-paragraphs          0.0    64.7   11.1
ai-vocab-pt                 0.5     0.0   22.2
paren-scarcity              0.0     0.0    0.0
```

## Luna (our writer) raw drafts, 06/10
15 unedited `gpt-6-luna` drafts (`raw-luna/`, same 18-topic prompt set; 3 timed out on Codex workspace routing). Share of drafts alarming, vs human doctrine:
- **triad-density 60.0%** (12.38/1k vs human 7.59), **colon-reveal 40.0%** (4.64/1k vs 3.05), **negated-inference 26.7%** (1.55/1k vs 0.06, ~25×), evaluative-tail 6.7%, uniform-paragraphs 6.7%, rather-than 6.7%.
- Luna produces **none** of the generic AI vocabulary or formulaic metatext Haiku does (ai-vocab-pt 0 vs Haiku 21%): model-specific profiling matters; English-style word lists would miss our writer.
- Conclusion: the three rules to watch hardest on Codex/Luna output are triads, colon reveals and negated inference. The site-wide follow-up pass should target exactly these.
