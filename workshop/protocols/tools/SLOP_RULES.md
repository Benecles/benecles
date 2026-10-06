# `slop_lint` rule reference

Findings are review prompts, not automatic verdicts. HARD rules report every pattern hit with severity `hard`. RATE rules report each hit only when a page has at least 250 words and five sentences, and the pattern occurs at least twice; `paren-scarcity` instead reports one absence signal on an eligible page with no parenthetical text. JSON includes per-rule density and review ceilings. Findings never fail alone; `--max-per-1000 N` applies an explicit total-density budget. Examples below illustrate the current implemented patterns, not every grammatical variant.

## HARD rules

| Rule | Pattern intent | One-line fix | Positive example (flagged) | Negative example | False-positive context |
|---|---|---|---|---|---|
| `negative-parallelism` | Contrast framed with a negated proposition or “mais do que”. | State the affirmative legal rule, retaining a real distinction. | “A medida não é definitiva.” | “A medida permanece provisória.” | “Não é nulidade, mas anulabilidade” may state distinct legal categories; inspect both halves. |
| `puffery` | Inflated importance language such as “papel fundamental” or “pedra angular”. | Replace importance language with the operative rule, fact, or consequence. | “A regra desempenha papel fundamental no sistema.” | “A regra fixa o prazo do recurso.” | “Papel” can be literal in other contexts; only the listed collocations match. |
| `significance-gerund` | A comma-led gerund that claims importance or relevance. | Delete the evaluative tail or add a concrete fact. | “A regra foi aplicada, evidenciando a importância do tema.” | “A regra foi aplicada ao pedido.” | A gerund can add a real procedural fact; only the listed importance nouns match. |
| `formulaic-metatext` | Formulaic announcements, previews, recaps, or conclusions. | Remove the announcement and state the proposition. | “Vale destacar que o prazo termina hoje.” | “O prazo termina hoje.” | “Em conclusão” may occur in quoted source text; review the visible context. |
| `vague-attribution` | Unspecified authors or groups offered as authority. | Name the author, court, or position when the source identifies it. | “Muitos autores afirmam que o prazo é curto.” | “O prazo é de quinze dias.” | A genuine source may itself be anonymous or collective; preserve that limit accurately. |
| `reader-address` | Direct prompts to the reader. | State the rule or consequence directly. | “Perceba que o prazo termina hoje.” | “O prazo termina hoje.” | Direct address in an exercise instruction may be functional. |
| `AI-calque` | Listed translated or generic expressions, including “abordagem robusta” and “navegar”. | Replace the calque with the concrete legal action or plain verb. | “A decisão oferece abordagem robusta para navegar pelo cenário jurídico.” | “A decisão organiza o exame dos fatos.” | `jornada` is exempt in “jornada de trabalho/limitada/diária/semanal/máxima”; quoted language may be deliberate. |
| `backstage` | Production/source-process language, course materials, locators, or blueprint terms. | Keep the page focused on legal material; move provenance to the private ledger. | “Os slides apresentam o tema nesta leitura.” | “O tema aparece no primeiro capítulo.” | Mentions inside a quotation or discussion of teaching materials may be intentional. |
| `rhetorical-triad` | The emphasis phrases “e, sobretudo,” and “e, acima de tudo,”. | Keep emphasis only when the final item adds a legally necessary element. | “A regra protege forma, prazo e, sobretudo, segurança.” | “A regra protege forma, prazo e segurança.” | A real statutory triad is legitimate; this rule targets the rhetorical emphasis phrase, not a bare list. |

## RATE rules

| Rule | Pattern intent | One-line fix | Positive example (flagged) | Negative example | False-positive context |
|---|---|---|---|---|---|
| `colon-reveal` | Repeated claim followed by an expansion within the same sentence. | State the fact directly when the colon only dramatizes or rephrases it. | “A norma fixa o limite. O ponto é este: o prazo encerra a análise.” | “A norma fixa o prazo aplicável ao pedido.” | A colon that introduces genuinely new content, evidence, or a necessary list is useful. |
| `denial-restatement` | “não …, mas/e sim/senão …” contrast within one clause. | Apply the delete-the-não test; retain both halves for a real legal distinction. | “A regra não elimina o dever, mas muda seu momento.” | “A regra preserva o dever e define seu momento.” | Legal “não X, mas Y” distinctions (including category or remedy distinctions) are valid when both sides matter. |
| `rather-than` | Frequency of “em vez de”, “ao invés de”, and “em lugar de/da/do”. | Use a direct affirmative verb when the contrast adds no legal condition. | “A parte age em vez de aguardar.” | “A parte aguarda a intimação.” | A genuine choice between legally different acts should remain explicit. |
| `triad-density` | Three-item comma-plus-“e” construction. | Enumerate only the legal elements the source actually supplies. | “A lei prevê registro, prazo e recurso.” | “A lei prevê registro e recurso.” | Statutory triads and enumerated requirements are valid; do not collapse necessary elements. |
| `stance-adverb` | Frequency of the listed stance adverbs (e.g., “meramente”, “efetivamente”). | Remove emphasis if it adds no fact; keep a legally meaningful qualification. | “O ato foi simplesmente comunicado.” | “O ato foi comunicado.” | “Efetivamente” or similar may distinguish actual conduct from a proposed or presumed act. |
| `negation-chain` | Three or more repeated “sem …” clauses, or three consecutive “Não ….” sentences. | Convert rhetorical repetition while preserving enumerated legal requirements. | “O pedido veio sem prazo, sem assinatura, sem comprovante.” | “O pedido veio sem prazo e sem assinatura.” | Multiple statutory prerequisites or a deliberate exhaustive checklist should remain intact. |
| `same-opener-run` | Three consecutive sentences beginning with the same word/skeleton. | Vary openings when repetition is not needed for legal clarity. | “A lei fixa o prazo. A lei define a forma. A lei prevê recurso.” | “A lei fixa o prazo. O juízo define a forma. A parte apresenta recurso.” | Repetition may keep a complex series of actors or conditions unambiguous. |
| `semicolon-correction` | Repeated semicolon clauses, including correction markers such as “mas” or “na verdade”. | Keep semicolons for close independent clauses; remove correction theater. | “A decisão reconhece o pedido; na verdade, limita seu alcance.” | “A decisão reconhece o pedido e limita seu alcance.” | A semicolon can correctly join related independent clauses; the hit is only a review prompt. |
| `colon-appositive` | Definition/list introduced by a colon after “é”, “significa”, “consiste em”, “inclui”, etc. | Write a short definition in the same sentence when the colon adds no structure. | “O requisito é: prova documental suficiente.” | “O requisito exige prova documental suficiente.” | A colon can make a genuinely necessary definition or list easier to parse. |
| `load-bearing-adverb` | Frequency of emphasis adverbs such as “claramente”, “obviamente”, and “essencialmente”. | Delete the adverb if the proposition remains equally precise. | “A regra claramente fixa o prazo.” | “A regra fixa o prazo.” | An adverb that marks evidential certainty, scope, or a genuine qualification may carry meaning. |
| `nominalisation-pileup` | Listed abstract-noun chains, e.g. “implementação da verificação da execução”. | Put the action in a verb and name its actor when known. | “A implementação da verificação da execução cabe ao órgão.” | “O órgão verifica a execução.” | Some nominal forms are established legal terms; preserve them when replacing them would change the concept. |
| `paren-scarcity` | Absence of parenthetical text on an otherwise eligible long page. | Add parenthetical material only when it clarifies; never to satisfy the signal. | Eligible page with no `(…)` text. | “O termo (definido no artigo) aparece no pedido.” | Zero parentheses is not a defect; parentheticals are optional and should serve the reader. |

## Current implementation notes

- `colon-reveal` looks for the claim and colon expansion in the same sentence, as described in D9. A colon introducing genuinely new content remains a review-only match.
- `triad-density` is intentionally broad: a comma-separated three-part phrase may be a statutory triad. The rate threshold and minimum text gates limit noise; context remains decisive.
- Rate ceilings are included in each rule definition and echoed as finding density. They do not hide low-density matches; runs fail only when the caller supplies `--max-per-1000 N` and the aggregate exceeds that budget.
- `paren-scarcity` is an absence signal on eligible pages and is exempt from the two-positive-match gate by definition.

## 06/10 additions (CEO; sources: avoid-ai-writing, stop-slop, autonovel ANTI-SLOP, MariusAure, Writing Standard D10)

| Rule | Kind | Catches | Fix |
|---|---|---|---|
| `teaser-hook` | HARD | "O resultado? …" staged reveal | State the fact. |
| `self-labeling` | HARD | "Esse é o ponto central" | Cut the label. |
| `hedge-stack` | HARD | "pode potencialmente" | One qualifier, where the doubt is. |
| `false-concession` | HARD | "Embora X, Y continua um desafio" | Specific concession or cut (D10.5). |
| `staged-objection` | HARD | "Alguém poderia objetar…" | Fake disagreement (D10.1): named positions only. |
| `reader-steer-question` | HARD | "O que isso significa?" | Answer directly. |
| `circular-because` | HARD | "porque havia necessidade de…" | Name the cause (D10.2). |
| `stacked-questions` | RATE | two+ rhetorical questions in a row | At most one. |
| `transition-opener` | RATE (1.5/1000) | paragraphs opening on "Além disso / Contudo / Nesse sentido…" | Open on the subject (C3). |
| `fragment-run` | RATE | three+ consecutive ≤3-word sentences | Fold into sentences. |
| `uniform-paragraphs` | RATE | five consecutive ≥40-word paragraphs within ±15% | Reshape around the argument (D9). |

On live Latam Aulas 01–09 (06/10): `stacked-questions` 12 (true rhetorical stacks), `uniform-paragraphs` 5, the rest 0.

**Whole gate in one command:** `python3 work/slop-bench/slop_gate.py PAGE.html` → `lint.json` + `critic_input.md` for a separate reviewer; apply span patches only, re-run.

## 06/10 backtest retune (SLOP-3b)
Limits now come from data (`work/slop-bench/BACKTEST.md`): negative-parallelism became RATE 2.0/1k; new `negated-inference` 0.5/1k; colon-reveal 5.6; triad-density 12.3; denial-restatement 1.6; stance-adverb 1.2; `fragment-run` and `load-bearing-adverb` retired (measured backwards). Twelve SlopDetector/tropes.fyi ports added (tool-artifact, placeholder, chat-scaffolding, ai-self-reference, ritual-conclusion, challenges-future, evaluative-tail, count-announce, analogy-coach, where-it-lives, invented-label, stakes-inflation) plus RATE `ai-vocab-pt` 5.2/1k. Every finding carries `band: tell|style`.
