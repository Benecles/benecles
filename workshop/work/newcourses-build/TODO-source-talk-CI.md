# Constitucional I, Aulas 05–25: clean before publishing (cloud session, 2026-09-29)

Specs for every key are written (`specs/constitucional/05.json` … `25.json`, `06c`, `21c`) and the keys are registered in `build.py`, but the drafts still contain **visible source talk** (sentences about "o capítulo", "o livro", "o texto do pacote", "esta aula/página", what the sources do not say). Rewrite each as a direct statement of the law or the author's position, or cut it; limits belong in the ledger. Line numbers are from the spec agents' reports (drafts under `course-drafts-2026-09-28/constitucional/`). Also delete any first-line "PROVISIONAL, awaiting Claude review" header from `draft.md` before rendering.

- **05** draft: 77 ("O detalhe pertence à unidade de reforma; aqui importa…"), 89 ("O capítulo não apresenta um caso…"), 97 ("tema que Tavares deixa em aberto neste capítulo").
- **06** draft: 55, 59 ("O capítulo…"), 90 ("as fontes desta aula não decidem isso"; "O capítulo não trata…"), 106, 110 ("As fontes desta aula não incluem decisão judicial").
- **06c** dossier: 3 (header), 5 ("O dossiê não atribui…"), 23 ("O texto do pacote contém…"), 25, 51 ("que o pacote não contém"), 63, 77.
- **07** draft: 9, 33, 102, 106 ("o capítulo…"), 110 (borderline), 120 ("O texto é hipotético").
- **08** draft: 21, 33 ("O extrato termina no início de uma ressalva…", clearest case), 77. Also names **Ellwanger** (HC 82.424, private person): use "o editor".
- **09** draft: 9, 49 ("O capítulo…"), 55, 57 (borderline).
- **10** draft: 75 ("O capítulo enfrenta…"), 124 ("interessam a esta aula"), 136.
- **11** draft: clean; but names **Firmenich** (Ext 417, private person): consider "o extraditando".
- **12** draft: 17 ("o trecho constitucional… a teoria aqui estudada não constrói…").
- **13** draft: 13 ("que o curso desenvolverá…", "Para esta classificação").
- **15** draft: 1 (header), 85 (borderline).
- **16** draft: 3 ("esta página a segue também").
- **17** draft: 55, 57 ("O livro… A edição de 2019…"), 59, 61, 67 ("a página não atribui ao Tribunal…").
- **18** draft: 137 ("a edição de referência foi fechada").
- **19** draft: 63 ("O livro relata este precedente só pelo resultado…"), 7 (borderline).
- **20** draft: 9, 27, 31, 45, 57, 67, 79, 83 (eight "O capítulo…" sentences).
- **21c** dossier: 1 (header), 3 ("serve de fonte da página da unidade").
- **22** draft: 5 ("Este texto parte…"). Spec splits before "Proibição de retrocesso e limites aos limites" (3.9k/1.7k); a more even split is before "Quando o juiz pode impor uma prestação".
- **24** draft: 19 ("a exposição de Sarlet, fechada em 2018, não contém o inciso"), 47 ("O trecho disponível não fornece…"); **51 "Ingo Wolfgang Silva" is an error** (check who is meant); 31 bare "Gomes".
- **25** draft: 9, 19 ("a fonte a citar numa questão"), 75, 96 ("A ementa e o dispositivo… não dão a contagem"), 110.

Content doubts to settle (from the agents): 06c Celso de Mello's vote vs. the proclaimed result on EC 30 art. 2º; 25 tese III vs. IV–V (marco temporal); 13 hierarchy of treaties (Sarlet/Piovesan vs. Gilmar Mendes) kept as the draft states.
Case dossiers 07c, 15c, 16c, 18c, 19c were still being written at handoff: register and spec them once they have `build-report.md`.

## C3 resolutions — 29/09 (for Claude to apply)

The five case dossiers named above have since been registered, specified and built into scratch staging. The line list above is still Claude's editorial cleanup queue; do not treat it as a list of unresolved factual disputes. Full private source notes are in `work/c3-source-doubts-2026-09-29/`.

- **06c, EC 30 art. 2º.** Distinguish the individual vote from the result. Celso de Mello's written conclusion requests suspension only of the expression “os precatórios pendentes na data de promulgação desta Emenda” in ADCT art. 78. The final ata proclaims, by majority **nos termos do voto do Relator** Néri da Silveira, suspension of the efficacy of the whole EC 30/2000 art. 2º. State the latter as the collegiate result; never attribute its broader reach to Celso's written request. ADI 2.356-MC, PDF pp. 118–121; see `ec30.md` for ready wording and quiz correction.
- **25, Tema 1.031 theses III versus IV–V.** Thesis III rejects 5 October 1988 occupation and renitente esbulho as prerequisites for recognition of Indigenous original territorial rights. Items IV–V use conditions at that date to distinguish consequences for private titles and compensation, including benfeitorias and, under item V's conditions, terra nua. Thus 1988 is not a cutoff for the Indigenous right; it helps select the private patrimonial regime. RE 1.017.365, ementa PDF pp. 9–11 and thesis pp. 11–12; see `marco-temporal.md`. Do not claim the excerpt proves the full theoretical justification for the indemnity line.
- **13, treaty hierarchy.** The draft correctly separates Sarlet/Piovesan's doctrinal constitutional-rank argument, the STF's supralegal rank for human-rights treaties incorporated without CF art. 5º § 3º procedure, and the § 3º rule of equivalence to amendment when the qualified procedure is met. Sarlet et al. pp. 438–440 support the author attribution and report dissensus in the STF. When describing Gilmar Mendes's reasoning, say “Segundo a síntese de Sarlet et al.”: the packet has that secondary account, not his full vote. Do not portray it as unanimous Court reasoning. See `treaties.md`.
- **24, names.** “Ingo Wolfgang Silva” is stale in this TODO: the current draft line 51 names Sarlet and paraphrases an unnamed Silva cited by Sarlet, without the erroneous compound name. The bare “Gomes” at current line 31 follows the assigned Sarlet reading (printed p. 899, note 802), whose extract does not identify his first name. Keep the surname or write “Sarlet atribui a Gomes”; do not infer it is Canotilho. See `names-and-seam.md`.
- **22, page division.** The current split before “Proibição de retrocesso e limites aos limites” leaves approximately 145/47 draft lines. Splitting instead before “Quando o juiz pode impor uma prestação” gives approximately 105/87 while preserving complete topic sections. Recommend the latter seam when Claude applies the spec change; this is a structural decision, not a factual correction.
