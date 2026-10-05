# SLOP-2 local corpus discovery

## Scope and provenance

This is a descriptive comparison of the available Portuguese legal book extracts (reference-candidate set) and visible text from staged lesson HTML pages (target-corpus proxies). The staged pages have unknown writer labels and are **not confirmed model generations**. The extracts are not a matched human control set, and no causal or authorship inference is supported.

Fresh samples from 30 tasks/models were not supplied. The requested 200,000-token threshold is therefore **not met or validated**; counts below are word-token counts from these files and do not establish any token threshold.

## Measured corpus

- Reference candidates: 9 `.txt` extracts; 622 934 word tokens.
- Target proxies: 20 `aula-*.html` pages; 21 611 visible-text word tokens.
- Reference tokenization: Unicode letter/number words, case-folded; HTML visible text excludes script/style/template/noscript and `aria-hidden` content. Navigation and other reader-visible labels remain included.

## Construction queries

Rates are occurrences per 10,000 word tokens. Ratios compare target rate/reference rate; `∞` means no occurrence in the reference candidate set, not proof of target-specific style. Repeated phrase occurrences can overlap.

| Construction | Reference count | Target count | Ref / 10k | Target / 10k | Target ÷ ref |
|---|---:|---:|---:|---:|---:|
| `não apenas` | 118 | 2 | 1.89 | 0.93 | 0.49× |
| `não só` | 87 | 1 | 1.40 | 0.46 | 0.33× |
| `mais do que` | 42 | 0 | 0.67 | 0.00 | 0.00× |
| `não se trata de` | 22 | 0 | 0.35 | 0.00 | 0.00× |
| `nesse sentido` | 103 | 0 | 1.65 | 0.00 | 0.00× |
| `diante desse cenário` | 1 | 0 | 0.02 | 0.00 | 0.00× |
| `é importante destacar` | 2 | 0 | 0.03 | 0.00 | 0.00× |
| `vale destacar` | 4 | 0 | 0.06 | 0.00 | 0.00× |
| `em outras palavras` | 45 | 0 | 0.72 | 0.00 | 0.00× |
| `por outro lado` | 79 | 0 | 1.27 | 0.00 | 0.00× |
| `de um lado` | 19 | 1 | 0.31 | 0.46 | 1.52× |
| `de outro lado` | 10 | 0 | 0.16 | 0.00 | 0.00× |
| `em suma` | 22 | 0 | 0.35 | 0.00 | 0.00× |
| `portanto` | 375 | 4 | 6.02 | 1.85 | 0.31× |
| `assim` | 996 | 5 | 15.99 | 2.31 | 0.14× |
| `cabe observar` | 1 | 0 | 0.02 | 0.00 | 0.00× |
| `cumpre destacar` | 3 | 0 | 0.05 | 0.00 | 0.00× |
| `sob essa perspectiva` | 0 | 0 | 0.00 | 0.00 | — |

## Most overrepresented observed words

Top 30 words with at least 10 target occurrences and a nonzero reference rate, ranked by target/reference rate ratio.

| Word | Ref count | Target count | Ref / 10k | Target / 10k | Ratio |
|---|---:|---:|---:|---:|---:|
| `homologação` | 2 | 13 | 0.03 | 6.02 | 187.36× |
| `identifique` | 3 | 15 | 0.05 | 6.94 | 144.12× |
| `etapa` | 3 | 12 | 0.05 | 5.55 | 115.30× |
| `033` | 3 | 11 | 0.05 | 5.09 | 105.69× |
| `01` | 4 | 12 | 0.06 | 5.55 | 86.47× |
| `abolir` | 5 | 14 | 0.08 | 6.48 | 80.71× |
| `contrato` | 11 | 25 | 0.18 | 11.57 | 65.51× |
| `contratos` | 17 | 37 | 0.27 | 17.12 | 62.74× |
| `pec` | 12 | 26 | 0.19 | 12.03 | 62.45× |
| `preâmbulo` | 7 | 15 | 0.11 | 6.94 | 61.77× |
| `muda` | 6 | 12 | 0.10 | 5.55 | 57.65× |
| `08` | 6 | 12 | 0.10 | 5.55 | 57.65× |
| `schmitt` | 9 | 18 | 0.14 | 8.33 | 57.65× |
| `03` | 8 | 16 | 0.13 | 7.40 | 57.65× |
| `02` | 11 | 15 | 0.18 | 6.94 | 39.31× |
| `supralegal` | 12 | 16 | 0.19 | 7.40 | 38.43× |
| `rito` | 17 | 21 | 0.27 | 9.72 | 35.61× |
| `05` | 10 | 11 | 0.16 | 5.09 | 31.71× |
| `pergunta` | 27 | 27 | 0.43 | 12.49 | 28.82× |
| `cnj` | 19 | 19 | 0.31 | 8.79 | 28.82× |
| `06` | 10 | 10 | 0.16 | 4.63 | 28.82× |
| `programa` | 14 | 13 | 0.22 | 6.02 | 26.77× |
| `comparação` | 12 | 11 | 0.19 | 5.09 | 26.42× |
| `recepção` | 44 | 40 | 0.71 | 18.51 | 26.20× |
| `ms` | 53 | 46 | 0.85 | 21.29 | 25.02× |
| `leitura` | 33 | 28 | 0.53 | 12.96 | 24.46× |
| `escolher` | 12 | 10 | 0.19 | 4.63 | 24.02× |
| `parlamentar` | 38 | 31 | 0.61 | 14.34 | 23.52× |
| `planos` | 16 | 13 | 0.26 | 6.02 | 23.42× |
| `unidade` | 51 | 38 | 0.82 | 17.58 | 21.48× |

## Most overrepresented observed n-grams

Top 30 observed bigrams/trigrams with at least 5 target occurrences and a nonzero reference rate, ranked by target/reference rate ratio. Counts and rates are shown because high ratios can arise from small baselines. This ranking is a review queue, not a quality score.

| n-gram | n | Ref count | Target count | Ref / 10k | Target / 10k | Ratio |
|---|---:|---:|---:|---:|---:|---:|
| `dos contratos` | 2 | 2 | 32 | 0.03 | 14.81 | 461.20× |
| `teoria geral dos` | 3 | 2 | 26 | 0.03 | 12.03 | 374.72× |
| `ms 32` | 2 | 1 | 12 | 0.02 | 5.55 | 345.90× |
| `ms 32 033` | 3 | 1 | 11 | 0.02 | 5.09 | 317.07× |
| `lei antiga` | 2 | 1 | 11 | 0.02 | 5.09 | 317.07× |
| `32 033` | 2 | 1 | 11 | 0.02 | 5.09 | 317.07× |
| `da formação` | 2 | 1 | 10 | 0.02 | 4.63 | 288.25× |
| `32 033 df` | 3 | 1 | 9 | 0.02 | 4.16 | 259.42× |
| `033 df` | 2 | 1 | 9 | 0.02 | 4.16 | 259.42× |
| `pode continuar` | 2 | 1 | 7 | 0.02 | 3.24 | 201.77× |
| `o cnj` | 2 | 1 | 7 | 0.02 | 3.24 | 201.77× |
| `recepção e` | 2 | 1 | 6 | 0.02 | 2.78 | 172.95× |
| `não substitui` | 2 | 1 | 6 | 0.02 | 2.78 | 172.95× |
| `norma antiga` | 2 | 1 | 6 | 0.02 | 2.78 | 172.95× |
| `de imprensa` | 2 | 1 | 6 | 0.02 | 2.78 | 172.95× |
| `adpf 347` | 2 | 1 | 6 | 0.02 | 2.78 | 172.95× |
| `ms 24` | 2 | 2 | 11 | 0.03 | 5.09 | 158.54× |
| `uma incompatibilidade` | 2 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `recepção não` | 2 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `qual norma` | 2 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `o rótulo` | 2 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `lei de imprensa` | 3 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `define a` | 2 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `chefe de estado` | 3 | 2 | 10 | 0.03 | 4.63 | 144.12× |
| `a regra constitucional` | 3 | 1 | 5 | 0.02 | 2.31 | 144.12× |
| `quem pode` | 2 | 2 | 9 | 0.03 | 4.16 | 129.71× |
| `geral dos` | 2 | 7 | 26 | 0.11 | 12.03 | 107.06× |
| `tendente a abolir` | 3 | 3 | 9 | 0.05 | 4.16 | 86.47× |
| `unidade política` | 2 | 2 | 6 | 0.03 | 2.78 | 86.47× |
| `por que a` | 3 | 2 | 5 | 0.03 | 2.31 | 72.06× |

## Limitations

- Corpus sizes, topics, document types, and source-selection processes differ; term distribution is not controlled for lesson topic or legal subject.
- Staged HTML pages may include headings, navigation, captions, and interface labels. The extraction counts rendered text nodes, not browser-computed visibility for CSS classes or external stylesheets.
- Reference extracts may contain OCR/extraction artifacts and represent only the listed files, not Portuguese legal prose generally.
- Counts are corpus-level observations. They do not identify authors, measure quality, or justify banning any phrase; legal and pedagogical context requires human review.
- Word-token counts are not model-token counts. The 200k model-token requirement cannot be inferred from them.

## Reproduction

From the repository root run:

```sh
python3 work/slop-bench/corpus_discovery.py
```

The script uses only Python standard-library modules and rewrites this report from the current input files.
