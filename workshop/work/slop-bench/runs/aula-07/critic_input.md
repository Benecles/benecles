# Span-level prose critic

## Role
You are an editorial critic for Portuguese legal teaching prose. Review a frozen draft against `protocols/STYLE.md` and Part D of `protocols/Writing Standard.md`. This is not an AI detector and must not judge authorship.

## Modes
- **Conform** (default): bring site prose toward STYLE.md.
- **Preserve**: when the chairman's own prose or a source quotation is being edited, protect its voice and wording; flag only concrete defects within the requested scope.

## Review method
Read the whole page for its legal thread and teaching purpose. Return only spans whose exact words create a specific reader-facing problem. A pattern-list match is not a reason by itself. Preserve legal terms of art, statutory language, quotations, accurate repetition, genuine legal contrasts, necessary caveats, and enumerated requirements. Do not invent doctrine, sources, facts, examples, or uncertainty.

Two quick tests for any suspect sentence (MariusAure): **meaning** — restate it in its boring version; if that is "things matter" or "this is complex", it carries no proposition; **fungibility** — if it could be pasted into an unrelated lesson unnoticed, it is filler.

Review these dimensions separately: information density; restatement; fake contrast; fake nuance; causal depth (circular explanation); forced symmetry; metadiscourse; significance inflation; conclusion pressure; formatting pressure; D10 fake disagreement; circular causal explanation; unnecessary restatement; excessive sectioning; reflexive qualification.

For every span, give:
1. exact quoted span (smallest phrase/sentence that carries the issue);
2. dimension;
3. why it impedes this page's legal teaching purpose, naming the missing or duplicated proposition;
4. smallest replacement, or `delete` if no proposition is lost.

Do not rewrite paragraphs, whole sections, or unflagged text. If a dimension has no supported issue, return an empty list for it. Do not require changes to satisfy a quota.

## Output JSON
Return valid JSON only:
```json
{
  "page": "...",
  "mode": "Conform",
  "scores": {
    "information_density": {"score": 0, "evidence": "short exact quotation or none"},
    "restatement": {"score": 0, "evidence": "..."},
    "fake_contrast": {"score": 0, "evidence": "..."},
    "fake_nuance": {"score": 0, "evidence": "..."},
    "causal_depth": {"score": 0, "evidence": "..."},
    "forced_symmetry": {"score": 0, "evidence": "..."},
    "metadiscourse": {"score": 0, "evidence": "..."},
    "significance_inflation": {"score": 0, "evidence": "..."},
    "conclusion_pressure": {"score": 0, "evidence": "..."},
    "formatting_pressure": {"score": 0, "evidence": "..."},
    "fake_disagreement": {"score": 0, "evidence": "..."},
    "circular_causal_explanation": {"score": 0, "evidence": "..."},
    "unnecessary_restatement": {"score": 0, "evidence": "..."},
    "excessive_sectioning": {"score": 0, "evidence": "..."},
    "reflexive_qualification": {"score": 0, "evidence": "..."}
  },
  "spans": [
    {"quote":"...", "dimension":"...", "reason":"...", "replacement":"..."}
  ]
}
```
Scores run 0 (no observed issue) to 100 (pervasive, evidenced issue), with the quoted evidence explaining any nonzero score. A score is not a grade of the author.


Mode: **conform**

---
# STYLE.md
# STYLE.md — target for Portuguese legal teaching

This is a positive target for the site, not a voice imitation or authorship test. The reference set is Portuguese legal scholarship and the reviewed house lessons. The current discovery report measured 9 legal-text reference candidates (622,934 word tokens) and 20 staged lesson-page proxies (21,611 word tokens); the page writers are unlabeled and these are not confirmed model samples. See `work/slop-bench/report.md`. No numeric style threshold is calibrated from those proxies, and no frequency is treated as a quality score.

## Attributes

| Dimension | Target | Reader-facing check |
|---|---|---|
| Information density | High: each sentence adds a rule, reason, application, or consequence. | Can the sentence be removed without losing a proposition? |
| Paragraph length | Highly variable, following the paragraph's job. | Does each paragraph establish one point, apply one rule, or present one named position? |
| Sentence length | Variable; moderate default, with longer sentences where legal conditions depend on each other. | Is the actor and operative verb easy to find? |
| Argument | Causal and evidentiary. State who acted, under which rule, and with what effect. | Does each explanation add a fact, rule, or actor instead of renaming the result? |
| Transitions | Mostly implicit; explicit connectors only when they clarify a real relation. | Is the relation actually causal, contrasting, or dependent? |
| Headings | Sparse navigation at real changes in the question. | Does the section answer a different question? |
| Lists | Only for enumerable, genuinely parallel items. | Is this a list of legal requirements/categories, or reasoning that belongs in prose? |
| Conclusions | Optional; no recap-only ending. | Does the final sentence add a consequence or answer, rather than restate? |
| Restatement | Very low, except where a legal term or comparison needs stable repetition. | Does the repeated phrase preserve precision, or only echo? |
| Metacommentary | None in reader-facing exposition. | Is the sentence about the lesson/text instead of the law? |
| Qualification | Only where the source or doctrine leaves genuine doubt; name its reason once. | Can the hedge be tied to an authority, split, or open issue? |
| Examples | Concrete and legally grounded: article, case, parties, vote, date, procedural act. | Can the student apply the rule to a real carrier? |
| Rhetorical symmetry | Low; position lengths follow their arguments, not a balanced template. | Is a contrast or triad doctrinally necessary? |
| Rhetorical questions | Rare; use as headings or when the case itself poses the question. | Does the question orient a real decision? |
| Legal vocabulary | Stable and exact. Repeat terms of art instead of varying them for elegance. | Would a synonym change the legal category? |

Numeric corpus distributions are descriptive in the current pilot, not targets. Once the discovery report has enough correctly labeled Portuguese data, it may add ranges for paragraph and sentence distributions; it must not optimize vocabulary diversity or a single aggregate score.

## Short reference passages

These are brief excerpts from local Brazilian constitutional-law treatise extracts. They illustrate legal exposition, not mandatory wording. Preserve quoted source language and terminology when teaching from these works.

> “O controle de constitucionalidade é um desses mecanismos”
>
> — Luís Roberto Barroso, local extract `work/controle-depth/extracts/barroso-pdf-20-362.txt`.

> “As Constituições escritas são apanágio do Estado Moderno.”
>
> — Gilmar Ferreira Mendes, local extract `work/controle-depth/extracts/mendes-branco-pdf-1853-2610.txt`.

> “O controle de constitucionalidade se define como ‘juízo relacional que procura estabelecer uma comparação valorativamente relevante’”
>
> — Dimitri Dimoulis and Soraya Lunardi, local extract `work/controle-depth/extracts/dimoulis-lunardi-pdf-82-185.txt`.

## Editing modes

- **Conform:** default for site prose. Apply these attributes and the Writing Standard Part D.
- **Preserve:** when editing the chairman's own prose or a quoted/source passage. Correct only the requested issue; retain meaningful voice, quotation, and legal terms.

A style flag is not evidence that a person used AI. Patch only the flagged span and preserve every unaffected proposition.


---
# Writing Standard, Part D
## Part D. Banned and limited patterns

Hard bans get zero tolerance. Limits are per lesson. Terms of art are always allowed (see D6).

**What slop is.** Slop is rhetorical machinery standing in for information: a contrast, triad, concession, reveal, or moral produced where the content asked for none. These are ordinary Portuguese structures; frequency and function matter more than isolated occurrence. Research also cautions against a single objective slop label: judgments vary across people and domains, so this standard treats findings as dimensions for editorial review, not authorship evidence ([Shaib et al.](https://arxiv.org/html/2509.19163)).

Three findings shape this policy:
- **Vocabulary variety is not a target.** In SlopBench's 18-model, English benchmark, models were more lexically diverse than human references; its composite rankings changed with metric weights and did not track crowd Elo reliably ([SlopBench](https://arxiv.org/html/2609.33905)). Repeat the precise legal term rather than thesaurus it. This result is not a Portuguese legal-writing measurement.
- **No punctuation mark proves slop.** Pew's 490,000-page English Common Crawl study used an AI detector and cautions that a page can be misclassified; punctuation alone is not proof ([Pew report](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/)). Em dashes are limited here by C10 as house style, not as evidence of AI.
- **Full rewrites can flatten variation.** Across seven datasets and more than 880,000 texts, one study reports that LLM polishing/rewriting reduced writing-complexity variance by 21–50% ([Sourati et al.](https://www.nature.com/articles/s41562-026-02550-0)). Human post-editing also did not erase all measured LLM-style traces in one personal-writing study ([Baumler et al.](https://aclanthology.org/2026.acl-long.2030/)). These results do not predict effects on our pages; they support local, span-level edits over automatic full-draft rewrites.

The order of priority when editing: (1) maximize propositions per sentence and delete machinery that carries none; (2) impose no structure the content did not ask for (no automatic contrast, triad, summary, section, concession, reveal or closing moral); (3) never manufacture nuance: if the obvious reading is right, state it; a distinction exists because the law has it; (4) allow asymmetry: a point gets the sentences it needs, lists the items they have, paragraphs the length their job takes; (5) explain by mechanism (who did what, under which rule, with which effect), not by relabelling; (6) judge known tells by density; (7) never "humanize": no fragments, slang, fake opinions, invented anecdotes or planted errors.

### D1. Negative parallelism (hard ban)
- "não é X, é Y" / "não é X, e sim Y" / "não se trata de X, mas de Y" / "mais do que X, Y" / "X, não Y" used as a flourish.
- **Legal exception:** a genuine legal distinction may use "não… mas" when both halves carry law: "A resposta tardia não forma contrato, mas vale como nova proposta." The test: if you delete the "não" half, is law lost? If not, delete it.
- "não apenas/só X, mas também Y": banned unless both halves are necessary information. Even then, prefer "X e Y".

### D2. Puffery and significance claims (hard ban)
- "papel crucial/fundamental/central", "pedra angular", "marco", "divisor de águas", "ganha destaque", "reflete a importância", "evidencia a relevância", "revela-se essencial", "merece atenção especial".
- Trailing gerunds that add significance ("…, evidenciando / reforçando / consolidando / demonstrando a importância de …").
- If something matters for the exam, show that it does: a trap, a vote count, a consequence.

### D3. Formulaic connectors and meta-text
- **Hard ban:** "vale ressaltar/destacar/notar/lembrar", "cabe destacar", "é importante notar/ressaltar/destacar", "é interessante observar", "nesta aula veremos", "como vimos", "como veremos", "vamos entender", "em conclusão", "por fim, mas não menos importante", "à luz do exposto".
- **Limit 1 per lesson each:** "em suma", "em síntese", "em resumo", "ou seja", "dessa forma", "nesse sentido", "além disso", "ademais".

### D4. Slogans, aphorisms and dramatic closers (hard ban)
- Short quotable sentences that compress a rule into a maxim: "Interpretar revela o que foi combinado e não escreve outro contrato."
- Paragraph endings that deliver a moral.
- Staged reveals with a colon.
- House tics found on our own site (2026-09-25 audit), limit 1 per lesson: "A pergunta é se…", "A pergunta decisiva…", "Tudo começa…", "Tudo depende…".

### D5. Vague attribution and fake balance (hard ban)
- "especialistas apontam", "muitos autores", "a doutrina moderna", "há quem diga", "alguns críticos": ban all of these when the source names who.
- "Por um lado… por outro…" with no resolution.

### D6. Intensifiers (limit 3 per lesson, total)
- "crucial", "fundamental", "essencial", "central", "decisivo", "significativo", "extremamente", "bastante", "realmente", "de fato", "claramente", "evidentemente".
- **Terms of art don't count:** "direitos fundamentais", "elementos essenciais do contrato", "erro essencial", "questão central" when it's a technical usage.
- If you remove the intensifier and the sentence loses nothing, remove it.

### D7. Reader address (hard ban)
- Cheerleading and faux-dialogue: "Você já deve ter percebido", "Não se preocupe", "Pense nisso", "Perceba que", "Repare:".
- Direct instructions in exam-practice contexts are fine ("Responda antes de abrir a solução").

### D8. Formatting tics
- Plain bold is retired (CASA-1, 06/10): the only bold in running text is `.held` and `.limit` (see C10b). Run-in labels inside a structured block (Tese., Casos.) may stay bold. Never bold whole sentences.
- No emoji.
- No headings that contain only other headings.
- No horizontal rules as decoration.

---

### D9. Density limits (structural tells; set from the 06/10 backtest, `work/slop-bench/BACKTEST.md`)
Counted by `slop_lint` (⚙). Each limit is the smallest rate at which ≤ 10% of human Portuguese doctrine would alarm; a hit over the limit is a reason to look, not an automatic edit. Findings carry a band: **tell** (model habit) or **style** (house rule humans also break).
- ⚙ **Negated inference** ("não basta / substitui / resolve / autoriza / prova / transforma / significa…"): ≤ 0.5 per 1,000 words. Our pages ran 2.43 vs human doctrine 0.14 (~18×): our strongest house tic. State what the decision did; keep a limit sentence only where the reader would otherwise assume the opposite.
- ⚙ **"Não é X" frames** (D1): ≤ 2.0 per 1,000 words, legal test still applies to each.
- ⚙ **Colon reveals** (claim, colon, expansion in one sentence): ≤ 5.6 per 1,000 words (human ~3, our pages 7–8).
- ⚙ **Triads** ("X, Y e Z"): ≤ 12.3 per 1,000 words; two triads in one paragraph is still worth a look.
- ⚙ **"em vez de / ao invés de / em lugar de"**: ≤ 1 per 1,000 words (13–15× the human rate).
- ⚙ **Stacked rhetorical questions**, **same-opener runs**, **uniform paragraphs** (five consecutive within ±15%), **no parentheses on a long page**: model-only patterns; any run is a finding.
- ⚙ **AI vocabulary basket** ("crucial, fundamental, essencial, robusto, abrangente, panorama, nuance…"): ≤ 5.2 per 1,000 words.
- ⚙ **Style band** (applies to everyone): stance adverbs ≤ 1.2/1k, "não X, mas Y" ≤ 1.6/1k, no "Em suma," wrap-ups, no "vale destacar".
- Read, not counted: nominalization pile-ups (C1), participial and "o que demonstra…" tails (⚙ hard), sentences that restate an earlier one (D10.3).

### D10. The five pathologies generic guides miss (chairman, 05/10; hard bans)
1. **Fake disagreement.** Staging an opposing view nobody in the sources holds, so the text can refute it. Only named positions with reasons (C6) are disputed.
2. **Circular causal explanation.** The "because" clause restates the effect ("a Corte interveio porque havia necessidade de intervenção"). Test: does the reason name a fact, a rule or an actor not already in the claim? If not, find the cause in the sources or cut the "because".
3. **Unnecessary restatement.** A sentence, paragraph or section summary that repeats what the reader just read. Delete-test: if removing it loses no proposition, remove it. Chapter ledes state the question, not a preview of the answer.
4. **Excessive sectioning.** A heading for every two paragraphs, a list where three sentences reason. One page answers one question (A0); a section exists when the question changes.
5. **Reflexive qualification.** A hedge, caveat or "em certa medida" attached by habit. C7 governs: hedge once, where the doubt is, with its reason. A concession that changes nothing is cut.



---
# Deterministic findings (review prompts, not verdicts)
- line 157 `backstage`: “Fontes e limites”
- line 159 `backstage`: “dos slides”
- line 161 `backstage`: “Os slides”
- line 161 `backstage`: “os slides”
- line 31 `negated-inference`: “não apaga”
- line 47 `negated-inference`: “não decide”
- line 76 `negated-inference`: “não cria”
- line 125 `negated-inference`: “não substitui”
- line 125 `negated-inference`: “não basta”
- line 11 `colon-reveal`: “Diante de uma norma anterior, separe duas perguntas: o conteúdo cabe na nova ordem, ou a alegação aponta um defeito formal da época em que ela nasceu?”
- line 33 `colon-reveal`: “Já uma norma anterior pode suscitar alegações diferentes: uma sobre o conteúdo diante da Constituição nova, outra sobre a forma observada quando foi editada.”
- line 94 `colon-reveal`: “A CF/88 serve à outra pergunta: se o conteúdo antigo pode continuar na nova ordem.”
- line 159 `colon-reveal`: “Base: slides “Juízo de não recepção × inconstitucionalidade”, do Prof.”
- line 35 `triad-density`: “Ponto de partida Antes de escolher o resultado, identifique a data da norma e o aspecto questionado”
- line 47 `triad-density`: “Se o conteúdo é compatível, a norma pode ser recebida e continuar vigente”
- line 113 `triad-density`: “de norma pré-constitucional pode ser levada ao STF por ADPF, se houver lesão a §§§§§§§§§§§§§§§§§§§§ e se estiverem presentes os demais requisitos de cabimento”
- line 61 `stacked-questions`: “Foi recebida pela nova Constituição? É compatível com a Constituição vigente?”
- line 136 `stacked-questions`: “O roteiro Quando a norma foi editada? A alegação trata do conteúdo perante uma Constituição nova ou da forma de origem?”
- line 11 `uniform-paragraphs`: “Diante de uma norma anterior, separe duas perguntas: o conteúdo cabe na nova ord”
- line 84 `uniform-paragraphs`: “O Supremo Tribunal Federal , na ADI 2, distingue o juízo de recepção do juízo de”

---
# Frozen draft: aula-07.html

Programa · I.9 Não recepção × inconstitucionalidade Prof. Marcelo Schenk Duque UFRGS · DIR03027 · 2026/2 

 Uma Constituição muda. E as leis antigas? 

 Diante de uma norma anterior, separe duas perguntas: o conteúdo cabe na nova ordem, ou a alegação aponta um defeito formal da época em que ela nasceu? A primeira leva à recepção ou à não recepção; a segunda usa o parâmetro então vigente.

 
 

 Leitura ≈ 5 min 

 Antes Aula 06 · Natureza do vício 

 Depois Aula 08 · Teorias do controle 

 

 
 01 Duas datas, dois juízos
 A data situa a norma; a alegação indica qual Constituição deve medi-la.
 
 
 Direito pré-constitucional é a norma editada antes da Constituição atualmente vigente. Uma lei hipotética de 1980 , por exemplo, é pré-constitucional em relação à Constituição de 1988 . A expressão localiza quando a norma foi feita; não diz, por si só, se ela continua válida ou se tem um vício.

 A entrada de uma Constituição nova não apaga automaticamente as normas que já existiam. Cada norma anterior pede exame próprio. Se o conteúdo puder conviver com a nova ordem, ela pode continuar nela; se houver incompatibilidade material, a ordem nova não a recebe.

 A lei posterior à Constituição usada como parâmetro não passa por juízo de recepção. A análise recai sobre sua constitucionalidade. Já uma norma anterior pode suscitar alegações diferentes: uma sobre o conteúdo diante da Constituição nova, outra sobre a forma observada quando foi editada.

 Ponto de partida Antes de escolher o resultado, identifique a data da norma e o aspecto questionado.





 02 Recepção depende do conteúdo
 A Constituição nova não reaprecia a forma de origem para decidir se o conteúdo antigo continua na ordem.
 
 
 A recepção pergunta se uma norma anterior pode continuar na ordem constitucional que entrou em vigor. A comparação recai sobre o conteúdo da regra antiga e o novo parâmetro.

 Se o conteúdo é compatível, a norma pode ser recebida e continuar vigente. Se há incompatibilidade material, o juízo é de não recepção. A data antiga, sem essa comparação, não decide o resultado.

 Essa análise não responde se o processo de formação da norma antiga respeitou a Constituição de sua época. Da mesma forma, identificar um possível defeito formal originário não responde se o conteúdo sobreviveu à mudança constitucional.

 A recepção trata da continuidade do conteúdo na nova ordem; o vício formal de origem pede outro parâmetro. 



 
 Situação
 Norma anterior
 Norma posterior
 
 Pergunta
 Foi recebida pela nova Constituição?
 É compatível com a Constituição vigente?
 
 Juízo
 Recepção ou não recepção
 Constitucionalidade ou inconstitucionalidade
 
 Incompatibilidade
 Não recepção
 Inconstitucionalidade, conforme o juízo próprio
 
 



 03 A Constituição nova não cria um vício de origem
 O parâmetro de validade acompanha o momento em que a norma foi formada.
 
 
 Chamar de “inconstitucionalidade superveniente” a incompatibilidade material entre uma lei anterior e uma Constituição posterior mistura dois momentos. A Constituição que viria depois ainda não existia quando a lei foi editada; por isso, ela não podia medir a atuação do legislador naquele momento.

 A nova Constituição mede o que pode continuar em vigor a partir de sua entrada. Se a regra antiga não puder conviver com ela, o resultado é não recepção. A incompatibilidade posterior não é vício de origem. 

 O Supremo Tribunal Federal , na ADI 2, distingue o juízo de recepção do juízo de constitucionalidade. Na hipótese de incompatibilidade entre norma pré-constitucional e Constituição posterior, a ação direta não serve para declarar inconstitucionalidade superveniente; a controvérsia é de recepção ou não recepção.





 04 O vício formal olha para a origem
 Uma alegação sobre a formação da lei usa a Constituição vigente quando o processo legislativo ocorreu.
 
 
 Volte à lei hipotética de 1980 , editada sob a Constituição de 1969 . Se alguém afirma que havia um defeito formal quando ela foi formada, o parâmetro temporal é a Constituição de 1969 . A CF/88 serve à outra pergunta: se o conteúdo antigo pode continuar na nova ordem.

 A hipótese não afirma que a lei de 1980 realmente tenha sido aprovada com defeito. O enunciado não identifica uma etapa irregular nem informa o conteúdo da lei. Por isso, ele não permite concluir que houve vício formal, recepção ou não recepção.

 A data do processo atual também não muda o parâmetro. Uma controvérsia pode surgir anos depois, mas a alegação sobre a forma continua ligada ao momento em que a lei foi formada. O parâmetro de origem não define a via. 



 
 Constituição de origem e Constituição nova

 
 


 05 A via exige um exame próprio
 A ADPF pode discutir norma anterior, desde que seus requisitos estejam satisfeitos.
 
 
 Uma controvérsia sobre a recepção de norma pré-constitucional pode ser levada ao STF por ADPF, se houver lesão a preceito fundamental e se estiverem presentes os demais requisitos de cabimento.



 
 Lei 9.882/1999 art. 1º, parágrafo único, I; art. 4º, § 1º 
 Parágrafo único. Caberá também argüição de descumprimento de preceito fundamental:
 I - quando for relevante o fundamento da controvérsia constitucional sobre lei ou ato normativo federal, estadual ou municipal, incluídos os anteriores à Constituição.
 § 1º Não será admitida argüição de descumprimento de preceito fundamental quando houver qualquer outro meio eficaz de sanar a lesividade.
 
 
 
 A ADI não substitui a ADPF para transformar a incompatibilidade de norma pré-constitucional com a Constituição nova em inconstitucionalidade superveniente. Na hipótese de um possível vício formal originário, o parâmetro é o da época; essa escolha não basta para indicar uma ação contra a lei anterior.

 Parâmetro temporal e cabimento são perguntas distintas. Primeiro, identifique o juízo pedido; depois, examine se a via processual pode conduzir a ele.





 ↺ Roteiro de resposta
 Nomeie a alegação antes de escolher o juízo.
 
 O roteiro Quando a norma foi editada? A alegação trata do conteúdo perante uma Constituição nova ou da forma de origem? Compare o aspecto alegado com o parâmetro correspondente.

 Quatro questões de treino

 
 Uma lei anterior à CF/88 tem conteúdo incompatível com a Constituição nova. Qual é o juízo?
 Não recepção. A incompatibilidade material impede a continuidade da norma na nova ordem.
 
 A entrada de uma nova Constituição encerra automaticamente a vigência de toda lei anterior?
 Não. O exame é norma a norma; a compatibilidade do conteúdo é que permite a recepção.
 
 Uma lei de 1980 teria vício formal. Qual Constituição serve de parâmetro?
 A Constituição vigente quando a lei foi formada; no exemplo, a Constituição de 1969.
 
 ADI e ADPF são caminhos equivalentes para qualquer problema de lei antiga?
 Não. A ADPF pode discutir recepção se seus requisitos forem atendidos. O parâmetro da forma de origem, sozinho, não demonstra o cabimento de uma ação.
 



 
 Fontes e limites desta página

 Base: slides “Juízo de não recepção × inconstitucionalidade”, do Prof. Dr. Marcelo Schenk Duque (DIR03027, UFRGS, 2026/2), 6 páginas, conforme o digesto visual. Os rótulos “Slide(s)” identificam a origem de cada explicação e diagrama. As figuras são reconstruções inline dos esquemas descritos no digesto; não reproduzem imagens dos slides.

 Os slides 1 (capa) e os slides textuais 2 e 4 foram condensados na introdução; o diagrama central vem do slide 3; a regra geral vem do slide 5; e a hipótese excepcional vem do slide 6. O quadro e o recap são reorganizações editoriais. A referência à Constituição de 1969 e ao exemplo da lei de 1980 foi preservada como aparece na fonte. Esta página não acrescenta pesquisa jurisprudencial nem detalha requisitos processuais de ADPF ou ADI.
