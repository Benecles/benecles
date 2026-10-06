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
- line 207 `negative-parallelism`: “não é”
- line 222 `negative-parallelism`: “não foi”
- line 222 `negative-parallelism`: “não é”
- line 385 `negative-parallelism`: “não é”
- line 346 `negated-inference`: “não cria”
- line 353 `negated-inference`: “não torna”
- line 387 `negated-inference`: “não cria”
- line 396 `negated-inference`: “não converte”
- line 13 `colon-reveal`: “O controle preventivo age antes : sobre o projeto, não sobre a lei.”
- line 34 `colon-reveal`: “O marco didático é o encerramento da formação da norma: antes dele, o projeto ainda pode ser deliberado; depois, o ato formado pode ser objeto de controle repressivo.”
- line 80 `colon-reveal`: “Ele acontece em dois pontos da tramitação: dentro da própria Casa legislativa e nas mãos do Presidente da República, por meio do veto.”
- line 99 `colon-reveal`: “Dois órgãos fazem o controle preventivo dentro da Casa legislativa: as Comissões de Constituição e Justiça (art.”
- line 101 `colon-reveal`: “As CCJs não atuam sobre todos os projetos de atos normativos: ficam de fora, por exemplo, Medidas Provisórias, resoluções de tribunais e decretos, conforme as atribuições previstas no regimento interno de cada CCJ.”
- line 101 `colon-reveal`: “pela CCJ tem caráter terminativo (rejeição e arquivamento), cabendo recurso ao plenário da Casa: no Senado, ao menos um décimo dos membros pode recorrer contra o parecer não unânime; na Câmara, o recurso segue o regimento interno.”
- line 112 `colon-reveal`: “A doutrina batiza as duas hipóteses: veto por inconstitucionalidade é veto jurídico ; veto por contrariedade ao interesse público é veto político .”
- line 125 `colon-reveal`: “66 da CF, do caput ao § 7º, organiza o procedimento do veto na seguinte sequência: Envio para sanção (art.”
- line 136 `colon-reveal`: “A maioria absoluta é aferida por votação por estirpe : maioria dos deputados e maioria dos senadores, separadamente.”
- line 174 `colon-reveal`: “4º, impede que o Congresso delibere proposta de emenda tendente a abolir quatro núcleos protegidos: Constituição Federal · art.”
- line 194 `colon-reveal`: “coloca, mesmo assim, a votação de tal matéria em pauta, comete, em tese, uma ilegalidade : viola a garantia do parlamentar ao devido processo legislativo.”
- line 194 `colon-reveal`: “se exerce pela via de exceção ou defesa (incidental) , em defesa de direito do próprio parlamentar: mandado de segurança contra a mesa da Câmara dos Deputados ou do Senado Federal.”
- line 198 `colon-reveal`: “a qualquer terceiro, ainda que invoque a condição de futuro destinatário da lei ou da emenda: admitir isso equivaleria a criar, por via oblíqua, um controle preventivo abstrato, inexistente no sistema brasileiro.”
- line 207 `colon-reveal`: “033/DF: o alcance do controle preventivo judicial não é o mesmo para toda proposição.”
- line 207 `colon-reveal`: “por conteúdo; o controle judicial preventivo, aqui, restringe-se à regularidade do procedimento : ao devido processo legislativo.”
- line 209 `colon-reveal`: “033/DF: a liminar de abril de 2013 (que suspendeu o PLC 14/2013) foi decisão monocrática do relator originário, Min.”
- line 218 `colon-reveal`: “Por regra, é vedada pelo STF a interpretação das normas regimentais das Casas legislativas: ponto que permanece controverso .”
- line 220 `colon-reveal`: “O Plenário não conheceu do mandado de segurança: a discussão envolvia regras internas da Câmara e não havia direito subjetivo do impetrante a amparar a ação (Rel.”
- line 222 `colon-reveal`: “foi extinto sem julgamento de mérito), mas mostra que a barreira do interna corporis não é absoluta: onde o regimento realiza diretamente um comando constitucional, sua má aplicação pode deixar de ser assunto apenas interno da Casa.”
- line 245 `colon-reveal`: “Aponta-se lei casuística, voltada a impedir a implantação do partido Rede Sustentabilidade: possível violação do direito público subjetivo do parlamentar de não se submeter a processo legislativo inconstitucional.”
- line 256 `colon-reveal`: “mesa deve designar comissão especial para o exame do mérito, com prazo de 40 sessões para o parecer: comissão não instalada, o que indica tramitação suspensa.”
- line 260 `colon-reveal`: “Medida cautelar indeferida: sem notícia da comissão especial, falta o periculum in mora : a tramitação já estava, de fato, suspensa.”
- line 310 `colon-reveal`: “Seguimento negado: a vedação do art.”
- line 349 `colon-reveal`: “No julgamento de mérito, prevaleceu a divergência de Teori Zavascki: o Plenário revogou a liminar e denegou a segurança.”
- line 353 `colon-reveal`: “A diferença está no objeto: decidir se o conteúdo de um PL é compatível com direitos constitucionais é uma coisa; impedir que a Casa viole uma etapa que a Constituição impõe é outra.”
- line 385 `colon-reveal`: “A exceção não é uma ação popular contra emendas: o fundamento está na posição do parlamentar e na proibição constitucional de deliberar proposta tendente a abolir cláusula protegida.”
- line 387 `colon-reveal`: “O STF negou a segurança: discordância com o conteúdo de PL não cria direito subjetivo de barrar o debate.”
- line 396 `colon-reveal`: “o mesmo conteúdo, a gravidade da tese não converte o mandado de segurança em revisão material prévia: a Casa pode rejeitar, o Presidente pode vetar e, se o projeto virar lei, o controle será repressivo.”
- line 471 `colon-reveal`: “Por regra, não: a interpretação de matéria puramente regimental é tratada como ato interna corporis .”
- line 13 `triad-density`: “é sancionada ou vetada, promulgada e passa a vigorar”
- line 53 `triad-density`: “por regra, pelos Poderes Legislativo e Executivo”
- line 64 `triad-density`: “Enquanto a formação ainda está em curso, há projeto e controle preventivo”
- line 101 `triad-density`: “Medidas Provisórias, resoluções de tribunais e decretos, conforme as atribuições previstas no regimento int”
- line 140 `triad-density`: “66, §§ 5º e 7º)”
- line 180 `triad-density`: “secreto, universal e periódico”
- line 245 `triad-density`: “liminar afastou a possibilidade prevista no PLC 14/2013, que restringia o acesso ao fundo partidário e ao tempo de propaganda eleitoral a novos partidos, na migraç”
- line 349 `triad-density`: “o STF examinou mandado de segurança contra o PLC 14/2013, que alterava regras de distribuição do fundo partidário e do tempo de propaganda eleitoral envolvendo partidos recém-c”
- line 357 `triad-density`: “secreto, universal e periódico, a separação dos Poderes ou direitos e garantias i”
- line 367 `triad-density`: “033 preserva debate, emenda e veto”
- line 245 `uniform-paragraphs`: “Medida liminar afastou a possibilidade prevista no PLC 14/2013, que restringia o”

---
# Frozen draft: aula-09.html

Programa · III.1 Momentos do controle · III.1.1 Preventivo Prof. Marcelo Schenk Duque UFRGS · DIR03027 · 2026/2 

 A lei ainda não existe. 

 Toda lei nasce de um projeto, tramita, é sancionada ou vetada, promulgada e passa a vigorar. Em algum ponto desse trajeto, a Constituição passa a ser examinada. O controle preventivo age antes : sobre o projeto, não sobre a lei. O controle preventivo é exercido sobretudo pelo Legislativo e pelo Executivo; ao Judiciário cabe uma via excepcional para proteger o processo legislativo .

 
 
 Questão Quem pode parar a tramitação? 

 Leitura ≈ 14 min 

 Antes Aula 08 · Teorias do controle 

 Depois Aula 10 · Controle repressivo 

 

 

 
 
 01 
 Dois momentos, um marco

 Nesta aula e na próxima, azul marca o controle preventivo , antes de a lei existir, e vermelho marca o controle repressivo , depois. O marco didático é o encerramento da formação da norma: antes dele, o projeto ainda pode ser deliberado; depois, o ato formado pode ser objeto de controle repressivo.

 

 
 
 
 
 
 Fig. 1 · Dois momentos 1 / 2 

 
 

 
 
 Definição por contraste 
 Preventivo x repressivo

 O controle preventivo (prévio) é realizado durante o processo legislativo . A lei ainda não existe , só o projeto. É realizado, por regra, pelos Poderes Legislativo e Executivo .

 O controle repressivo (posterior) é feito sobre a lei, não mais sobre o projeto. Pressupõe o encerramento do processo legislativo , e não, necessariamente, o início de vigência da lei. É realizado, por regra, pelo Poder Judiciário .

 


 
 O marco temporal 
 A conclusão da formação separa as fases

 Enquanto a formação ainda está em curso, há projeto e controle preventivo . Encerrado o processo e formado o ato, o controle passa a ser repressivo ; a vigência pode começar depois.


 


 




 
 
 02 
 A regra: Legislativo e Executivo

 Por regra, o controle preventivo é político, não judicial. Ele acontece em dois pontos da tramitação: dentro da própria Casa legislativa e nas mãos do Presidente da República, por meio do veto.

 

 
 
 
 
 
 Fig. 2 · A regra: Legislativo e Executivo 

 
 

 
 
 Comissões e Plenário 
 Pelo Legislativo

 Dois órgãos fazem o controle preventivo dentro da Casa legislativa: as Comissões de Constituição e Justiça (art. 58 da CF) e o Plenário da respectiva Casa.

 As CCJs não atuam sobre todos os projetos de atos normativos: ficam de fora, por exemplo, Medidas Provisórias, resoluções de tribunais e decretos, conforme as atribuições previstas no regimento interno de cada CCJ. A decisão de inconstitucionalidade tomada pela CCJ tem caráter terminativo (rejeição e arquivamento), cabendo recurso ao plenário da Casa: no Senado, ao menos um décimo dos membros pode recorrer contra o parecer não unânime; na Câmara, o recurso segue o regimento interno.

 


 
 O veto presidencial 
 Pelo Executivo: veto jurídico e veto político

 Compete ao Presidente da República vetar o projeto, no todo ou em parte, quando o considerar inconstitucional ou contrário ao interesse público (art. 66, § 1º, da CF).

 A doutrina batiza as duas hipóteses: veto por inconstitucionalidade é veto jurídico ; veto por contrariedade ao interesse público é veto político .

 


 




 
 O procedimento do veto (art. 66 da CF)

 O art. 66 da CF, do caput ao § 7º, organiza o procedimento do veto na seguinte sequência:

 
 Envio para sanção (art. 66, caput). A Casa em que se concluiu a votação envia o projeto ao Presidente da República, que, aquiescendo, o sanciona.

 Veto presidencial (art. 66, § 1º). Se considerar o projeto, no todo ou em parte, inconstitucional ou contrário ao interesse público, o Presidente veta-o total ou parcialmente, em quinze dias úteis contados do recebimento, e comunica os motivos ao Presidente do Senado Federal em quarenta e oito horas .

 Limite do veto parcial (art. 66, § 2º). O veto parcial só pode abranger texto integral de artigo, parágrafo, inciso ou alínea.

 Silêncio é sanção (art. 66, § 3º). Decorrido o prazo de quinze dias, o silêncio do Presidente da República importa sanção.

 Apreciação em sessão conjunta (art. 66, § 4º). O veto é apreciado em sessão conjunta, em até trinta dias do recebimento, só podendo ser rejeitado pelo voto da maioria absoluta de Deputados e Senadores. A maioria absoluta é aferida por votação por estirpe : maioria dos deputados e maioria dos senadores, separadamente. A EC 76/2013 suprimiu o voto secreto dessa votação.

 Prazo esgotado tranca a pauta (art. 66, § 6º). Esgotado sem deliberação o prazo do § 4º, o veto entra na ordem do dia da sessão imediata, sobrestadas as demais proposições, até a votação final.

 Se não mantido, promulgação em cascata (art. 66, §§ 5º e 7º). Rejeitado o veto, o projeto é enviado para promulgação ao Presidente da República. Se este não promulgar a lei em quarenta e oito horas, promulga o Presidente do Senado; se este também não o fizer no mesmo prazo, promulga o Vice-Presidente do Senado.

 



 
 
 03 
 A exceção: o Judiciário

 Excepcionalmente, o próprio Judiciário controla preventivamente, ainda pelo lado azul do eixo, porque a lei ainda não existe. É controle incidental, movido por um único legitimado, com limites estreitos.

 

 
 
 
 
 
 
 
 Fig. 3 · A exceção pelo Judiciário 

 
 

 
 
 Fundamento 
 Um direito subjetivo do parlamentar

 O controle preventivo pelo Judiciário ocorre na via judicial, quando a Constituição, expressamente, prevê a impossibilidade de trâmite de uma determinada matéria ou espécie normativa. Ele diz respeito a um “direito função” do parlamentar ao processo legislativo “hígido” (sadio).

 O art. 60, § 4º, impede que o Congresso delibere proposta de emenda tendente a abolir quatro núcleos protegidos:

 
 Constituição Federal · art. 60 § 4º 
 Não será objeto de deliberação a proposta de emenda tendente a abolir:
 I - a forma federativa de Estado;
 II - o voto direto, secreto, universal e periódico;
 III - a separação dos Poderes;
 IV - os direitos e garantias individuais.
 
 
 A vedação alcança a própria deliberação. O parlamentar pode pedir proteção antes da votação de PEC que, de modo inequívoco, ataque uma cláusula pétrea.

 


 
 Mecanismo e legitimidade 
 Mandado de segurança, só do parlamentar

 Se a mesa da Casa legislativa coloca, mesmo assim, a votação de tal matéria em pauta, comete, em tese, uma ilegalidade : viola a garantia do parlamentar ao devido processo legislativo. O controle se exerce pela via de exceção ou defesa (incidental) , em defesa de direito do próprio parlamentar: mandado de segurança contra a mesa da Câmara dos Deputados ou do Senado Federal.

 A legitimidade para propor a ação é exclusiva do parlamentar . O STF fixou isso desde o leading case MS 20.257/DF, Min. Moreira Alves (RTJ 99/1031), reiterado em MS 20.452/DF (Min. Aldir Passarinho, RTJ 116/47), MS 21.642/DF (Min. Celso de Mello, RDA 191/200), MS 24.645/DF e MS 24.593/DF e MS 24.576/DF (2003) e MS 24.356/DF (Min. Carlos Velloso), na síntese do MS 24.667-AgR, Rel. Min. Carlos Velloso, julgamento em 4-12-2003, Plenário, DJ de 23-4-2004.

 A exclusividade é estrita: o STF nega legitimidade a qualquer terceiro, ainda que invoque a condição de futuro destinatário da lei ou da emenda: admitir isso equivaleria a criar, por via oblíqua, um controle preventivo abstrato, inexistente no sistema brasileiro. E a legitimidade não sobrevive à perda do mandato: encerrado o exercício parlamentar do impetrante, mesmo que o mandado de segurança já esteja em curso, falta-lhe condição para prosseguir com a ação, que se extingue por ausência de legitimidade ativa (MS 27.971, decisão monocrática do Min. Celso de Mello, j. 1º.07.2011).

 


 
 Alcance 
 PEC e projeto de lei não recebem o mesmo controle

 O STF distingue com precisão, desde o julgamento do MS 32.033/DF: o alcance do controle preventivo judicial não é o mesmo para toda proposição. Sobre PEC , o art. 60, § 4º veda a própria deliberação de emenda tendente a abolir cláusula pétrea, logo o controle alcança a matéria , não só o rito. Sobre projeto de lei , não há previsão constitucional equivalente que vede a deliberação por conteúdo; o controle judicial preventivo, aqui, restringe-se à regularidade do procedimento : ao devido processo legislativo.

 Essa distinção foi fixada no julgamento de mérito do próprio MS 32.033/DF: a liminar de abril de 2013 (que suspendeu o PLC 14/2013) foi decisão monocrática do relator originário, Min. Gilmar Mendes, favorável a uma leitura mais ampla do controle preventivo. No Plenário, prevaleceu a divergência aberta pelo Min. Teori Zavascki, que redigiu o acórdão, restringindo o cabimento do mandado de segurança preventivo a duas hipóteses apenas: PEC manifestamente ofensiva a cláusula pétrea, e projeto de lei ou PEC cuja tramitação viole manifestamente a norma que disciplina o próprio processo legislativo.

 


 
 Limites 
 Procedimento sim, mérito político não

 O controle preventivo exercido pelo Judiciário abrange apenas a garantia de um procedimento em total conformidade com a Constituição. Não lhe cabe estender o controle sobre aspectos discricionários relativos às questões políticas e aos atos internos ( interna corporis ). Por regra, é vedada pelo STF a interpretação das normas regimentais das Casas legislativas: ponto que permanece controverso .

 O MS 24.356/DF ilustra esse limite em um conflito sobre o arquivamento de denúncia por quebra de decoro parlamentar. O Plenário não conheceu do mandado de segurança: a discussão envolvia regras internas da Câmara e não havia direito subjetivo do impetrante a amparar a ação (Rel. Min. Carlos Velloso, julgamento em 13/02/2003).

 Para o Min. Gilmar Mendes (MS 26.915-MC/DF), o bloqueio à interpretação regimental merece temperamento quando a norma do regimento funciona como norma constitucional interposta : expressão de Gustavo Zagrebelsky para normas que, sem serem formalmente constitucionais, são chamadas pela própria Constituição a completá-la, de modo que violá-las é, mediatamente, violar a Constituição. A tese não foi pacificada pelo Plenário (o próprio MS 26.915 foi extinto sem julgamento de mérito), mas mostra que a barreira do interna corporis não é absoluta: onde o regimento realiza diretamente um comando constitucional, sua má aplicação pode deixar de ser assunto apenas interno da Casa.

 


 




 
 
 04 
 Dois casos, dois desfechos

 Uma liminar concedida e depois derrubada; uma cautelar simplesmente indeferida. Os dois casos mostram como a via é, na prática, estreita.

 
 
 
 
 MS 32.033/DF Rel. Min. Gilmar Mendes · STF, abril de 2013 
 
 Medida liminar afastou a possibilidade prevista no PLC 14/2013, que restringia o acesso ao fundo partidário e ao tempo de propaganda eleitoral a novos partidos, na migração partidária ocorrida durante a legislatura. Aponta-se lei casuística, voltada a impedir a implantação do partido Rede Sustentabilidade: possível violação do direito público subjetivo do parlamentar de não se submeter a processo legislativo inconstitucional.

 

 Liminar deferida em 24.4.2013; em 20.6.2013 o Plenário revogou a liminar e denegou a segurança.

 

 
 MS 32.036 e 32.037/DF Rel. Min. Dias Toffoli · STF, maio de 2013 
 
 Mandado de segurança impetrado para obstar a tramitação e a deliberação da PEC 33/2011 (que alteraria o controle das decisões do STF pelo Congresso Nacional). O regimento interno da Câmara prevê que, após a admissão pela CCJ, a mesa deve designar comissão especial para o exame do mérito, com prazo de 40 sessões para o parecer: comissão não instalada, o que indica tramitação suspensa.

 

 Medida cautelar indeferida: sem notícia da comissão especial, falta o periculum in mora : a tramitação já estava, de fato, suspensa.

 

 




 
 
 05 
 A via existe, mas raramente vinga

 A jurisprudência do STF delimita o cabimento do mandado de segurança parlamentar no controle preventivo.

 
 
 
 Premissas 
 A via é excepcional e se funda no direito público subjetivo do parlamentar a um processo legislativo hígido. O cabimento clássico é invocado quando a Constituição veda expressamente a deliberação de determinada matéria. Quanto às cláusulas pétreas, sustenta-se que o parlamentar tem direito a não ver deliberada PEC tendente a abolir os bens protegidos pelo art. 60, § 4º. 
 Ponto principal da jurisprudência 
 O STF admite, em tese, a possibilidade excepcional do controle preventivo por mandado de segurança. Nos precedentes reunidos abaixo, não houve ordem definitiva para barrar PEC por ofensa material a cláusula pétrea. No MS 32.033/DF houve suspensão temporária de um projeto de lei por liminar, depois revogada pelo Plenário. 
 

 
 
 Processo
 Proposição impugnada
 Resultado no STF
 
 
 MS 20.257/DF
 PEC que prorrogava mandatos municipais
 Precedente fundador. Reconhecida a legitimidade do parlamentar e a possibilidade abstrata do controle preventivo, mas segurança não concedida.
 
 MS 21.648/DF
 PEC do IPMF
 Perdeu o objeto após a promulgação da emenda; sem concessão da segurança.
 
 MS 24.138/DF
 Projeto de lei que alterava a CLT
 Segurança denegada por unanimidade; afastado o controle material preventivo sobre projeto de lei ordinária.
 
 MS 24.642/DF
 PEC da Reforma da Previdência
 Segurança indeferida; não reconhecida violação suficiente para sustar o processo legislativo.
 
 MS 30.956/DF
 Projeto sobre royalties do petróleo
 Seguimento negado: a vedação do art. 60, § 4º dirige-se a PECs, não a projetos de lei.
 
 MS 32.033/DF
 PLC 14/2013: fundo partidário e propaganda
 Liminar deferida em 24.4.2013 (Min. Gilmar Mendes); em 20.6.2013 o Plenário revogou a liminar e denegou a segurança.
 
 MS 34.448/DF
 PEC do teto de gastos (depois EC 95/2016)
 Liminar indeferida; processo extinto ou prejudicado pela promulgação da emenda.
 
 MS 34.518/DF
 PEC da vaquejada (depois EC 96/2017)
 Pedido de suspensão da tramitação não acolhido; promulgação posterior prejudicou o controle.
 
 MS 37.721/DF
 PEC das imunidades parlamentares
 Liminar indeferida; o relator afirmou que só situações extremas autorizariam intervenção judicial antes da conclusão do processo legislativo.
 
 
 
 


 
 Cabimento reconhecido em tese O STF admite, excepcionalmente, o mandado de segurança parlamentar para tutela do processo legislativo.

 Âmbito restrito O Tribunal é mais receptivo a vícios formais e procedimentais do que a um controle material preventivo amplo.

 Ponto distintivo O MS 32.033/DF é o caso mais expressivo de deferimento liminar, embora sem concessão final da ordem.

 



\n 
 05 O caso muda quando muda a proposição
 A Constituição proíbe deliberar certas propostas de emenda; não cria a mesma vedação para o conteúdo de um projeto de lei.
 
 
 No MS 32.033/DF , o STF examinou mandado de segurança contra o PLC 14/2013, que alterava regras de distribuição do fundo partidário e do tempo de propaganda eleitoral envolvendo partidos recém-criados. O relator, Gilmar Mendes, concedeu liminar para suspender a tramitação. No julgamento de mérito, prevaleceu a divergência de Teori Zavascki: o Plenário revogou a liminar e denegou a segurança.

 A maioria recusou o controle judicial preventivo do conteúdo material de projeto de lei. Enquanto a proposta tramita, o Legislativo pode debatê-la, emendá-la ou rejeitá-la, e o Executivo pode vetá-la. Antecipar o controle material por mandado de segurança daria ao parlamentar uma revisão abstrata que não pode provocar depois da promulgação. Se o projeto virar lei, permanece o controle repressivo.

 O resultado não torna o processo legislativo imune ao Judiciário. O STF admite MS de parlamentar quando um vício constitucional de procedimento já se concretizou. A diferença está no objeto: decidir se o conteúdo de um PL é compatível com direitos constitucionais é uma coisa; impedir que a Casa viole uma etapa que a Constituição impõe é outra.

 Por que a PEC tem uma exceção própria

 O art. 60, §4º, determina que não será objeto de deliberação proposta de emenda tendente a abolir a forma federativa, o voto direto, secreto, universal e periódico, a separação dos Poderes ou direitos e garantias individuais. A vedação alcança a própria deliberação. Por isso o parlamentar pode, em hipótese excepcional, pedir que o Judiciário impeça a tramitação de PEC que ataque de modo inequívoco uma dessas cláusulas.

 O limite é alto. No MS 37.721 AgR, sobre proposta relativa às imunidades parlamentares, a Primeira Turma reiterou que o controle preventivo de PEC exige afronta inequívoca a cláusula pétrea e que, fora de situações extremas, o Judiciário não deve impedir o Congresso de discutir matéria. Discordância com a política proposta ou redução de proteção não demonstram, sozinhas, tendência a abolir direito protegido.

 Proposição
 Via judicial preventiva
 Razão
 
 Projeto de lei: mérito material
 Em regra, não cabe MS para antecipar o juízo judicial
 MS 32.033 preserva debate, emenda e veto; após formada a lei, existe controle repressivo
 
 PL: vício constitucional do procedimento
 MS parlamentar pode caber se a violação já ocorreu
 Protege o direito de participar de processo legislativo constitucional
 
 PEC: proposta tendente a abolir cláusula pétrea
 Excepcionalmente, parlamentar pode pedir bloqueio da deliberação
 Art. 60, §4º; exige afronta inequívoca e intervenção extrema
 
 Disputa puramente regimental
 Em regra, não cabe ao STF substituir a Casa
 Sem ligação direta com comando constitucional, permanece matéria interna
 
 

 Três casos, três funções

 MS 20.257/DF é lembrado como precedente fundador sobre mandado de segurança parlamentar e PEC que prorrogava mandatos municipais. A exceção não é uma ação popular contra emendas: o fundamento está na posição do parlamentar e na proibição constitucional de deliberar proposta tendente a abolir cláusula protegida.

 No MS 24.138/DF , um parlamentar tentou impedir discussão de projeto que alterava a CLT. O STF negou a segurança: discordância com o conteúdo de PL não cria direito subjetivo de barrar o debate. Já o MS 24.356/DF tratava de denúncia por quebra de decoro e de procedimento interno da Câmara; o Plenário não conheceu do pedido, por falta de direito subjetivo demonstrado. Ele ilustra o limite das controvérsias puramente regimentais, não o mérito de uma lei.

 Roteiro de resolução

 Classifique a proposição. É projeto de lei, PEC ou outro ato em formação?
 Localize o vício. A violação de procedimento já ocorreu ou se pede avaliação antecipada do resultado?
 Mostre o comando constitucional. Qual artigo disciplina o rito ou qual cláusula pétrea estaria sendo abolida?
 Limite o pedido. O parlamentar pede tutela do próprio direito de participação ou tenta obter controle abstrato prévio?
 
 Exemplo. Se PEC propõe abolir eleições periódicas para determinado cargo, o art. 60, §4º, II, oferece fundamento textual para pedir que a deliberação seja interrompida, sujeito ao exame rigoroso do STF. Se um projeto de lei propõe o mesmo conteúdo, a gravidade da tese não converte o mandado de segurança em revisão material prévia: a Casa pode rejeitar, o Presidente pode vetar e, se o projeto virar lei, o controle será repressivo.




 
 
 06 
 Resumo lado a lado

 A regra e a exceção do controle preventivo, reunidas num único quadro.

 
 
 
 
 Critério 
 Regra: Legislativo e Executivo
 Exceção, Judiciário
 
 
 Órgão
 CCJ e Plenário da Casa; Presidente da República (veto)
 Órgão judicial, ao julgar mandado de segurança
 
 Objeto
 Todo projeto (com exceções regimentais para a CCJ)
 Conteúdo de PEC, apenas excepcionalmente; para PL, vício constitucional do rito
 
 Via
 Interna ao processo legislativo (parecer, votação, veto)
 Incidental: mandado de segurança contra a mesa
 
 Legitimado
 Órgãos da própria Casa; Presidente da República
 Exclusivamente o parlamentar
 
 Alcance
 Pode examinar mérito e forma, conforme o órgão
 Procedimento constitucional já violado; em PEC, excepcional limite material do art. 60, §4º; questões puramente internas ficam com a Casa
 
 Fundamento
 Arts. 58 e 66 da CF
 Art. 60, § 4º, da CF · direito do parlamentar a processo legislativo hígido
 
 
 
 




 
 
 06 
 Teste rápido

 Responda antes de abrir.

 
 
 
 Uma CCJ rejeita e arquiva um projeto por considerá-lo inconstitucional. Essa decisão é definitiva?
 Não. A decisão da CCJ tem caráter terminativo, mas cabe recurso ao plenário da Casa legislativa.
 
 Qual a diferença entre veto jurídico e veto político?
 O veto jurídico se funda em inconstitucionalidade ; o veto político, em contrariedade ao interesse público (art. 66, § 1º, da CF).
 
 Se o Presidente fica em silêncio pelos 15 dias úteis do art. 66, § 1º, o que acontece?
 O silêncio importa sanção (art. 66, § 3º, da CF).
 
 Um parlamentar pretende impedir, por via judicial, que sua Casa vote uma PEC que julga abolir cláusula pétrea. Qual o instrumento e quem pode usá-lo?
 Mandado de segurança contra a mesa da Casa legislativa, de legitimidade exclusiva do parlamentar .
 
 O Judiciário, nesse controle preventivo excepcional, pode examinar se a interpretação do regimento interno da Casa foi correta?
 Por regra, não: a interpretação de matéria puramente regimental é tratada como ato interna corporis . No MS 24.356/DF, o STF também apontou a ausência de direito subjetivo do impetrante.
 
 Qual foi o desfecho do MS 32.033/DF?
 A liminar suspendeu temporariamente a tramitação do projeto de lei; o Plenário depois a revogou e denegou a segurança.
