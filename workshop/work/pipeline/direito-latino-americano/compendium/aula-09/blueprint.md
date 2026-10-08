# Blueprint: Direito Latino-americano, Aula 09 (saúde e diálogo institucional)

**Estado da fonte após o painel REVISE.** Este arquivo planeja a reconstrução da página viva; registros de pesquisa não viram acórdãos. O material primário local contém uma página oficial do Tema 6 com o leading case, andamento e início do item 1, e um resultado de busca que apenas identifica STA 175 AgR (`chapters/re566471-official-docket/01-tema-6-docket-record.txt`; `chapters/sta175-official-search-record/01-official-search-result.txt`). Não há, no compêndio atribuído, atos oficiais completos de STA 175/178, acórdão/tese integral do Tema 6, Tema 1234 ou Tema 500, nem textos das SV 60/61. A escrita dos trechos dependentes fica condicionada à incorporação desses arquivos e a localizadores por página/item. A cerca, as lacunas e os localizadores permanecem privados.

## A0. Entradas lidas e função de cada uma

| Entrada | Tamanho/recorte | Uso neste plano |
|---|---:|---|
| S0, `course-map.md`, entrada `aula-09.html` | programa de 28/09, eixo e função | Contrato: direitos sociais, organização institucional do SUS, conhecimento técnico, audiências, diálogo e parâmetros; responder ao eixo com STA 175, Tema 6 e decisões posteriores sobre medicamentos. Pré-requisitos: Aulas 07 e 08. |
| `00-index.md`, `05-eixo.md`, `triage/aula-09.csv` | 2 primários, 20 fundos, sem apoio | Proveniência e lacunas, não doutrina adicional. O eixo é verbatim; a atividade cobra tribunal, ano, decisão, razão, dissenso e consequência. |
| `20-primary-001…re566471…txt` | um registro oficial breve | RE 566.471/RN; assunto, conclusão temporal de 2024 e **somente o início do item 1** da tese: ausência das listas do SUS impede, como regra, fornecimento judicial independentemente do custo. |
| `20-primary-002…sta175…txt` | resultado oficial de pesquisa | Apenas a identificação da classe STA 175 AgR. Não fornece ementa, votos, dispositivo, data de julgamento nem fundamentação. |
| `10-slides.txt`, `50-exercises-and-exams.txt` | marcadores de ausência | Sem deck de 28/09 nem prova própria indexados. As armadilhas vêm do contraste jurídico, não de uma suposta pergunta já aplicada. |
| Fundo Aulas 07/08 no S4 | T-153/1998, T-025/2004, Autos 176/2005 e 008/2009, ADPF 347/2023 | Transição breve: de falha estrutural e monitoramento à pergunta sobre acesso desigual e coordenação no SUS. Não reproduzir a aula colombiana. |
| Página viva `courses/direito-latino-americano/aula-09.html` | cerca de 3,3 mil palavras de prosa extraída, além de respostas e rótulos | Inventário de preservação abaixo. É texto a conferir, nunca fonte primária. `60-live-page.txt` tem 1 byte; por isso o inventário foi feito diretamente no HTML vivo. |
| Aula 05 viva; Controle Aula 01 viva com todos os `REF ·`; blueprint de referência e seus blocos Method | dois modelos | Modelo de caso com tribunal/ano/dispositivo/razões/dissenso/depois e pergunta-eixo; técnica de abertura concreta, lede, passagem de seção, figura que prova, caso trabalhado e teste. |
| `work/latam-prep/late-classes/plan-aula-09.md`, `work/depth/latam/aula-09-add.sources.md`, rascunho A09, `work/latam-build/a09.py` e versão `pre-deepen` | material anterior | Pistas de busca e conteúdo perdido/duplicado; nenhum substitui o primário de S4. O ledger antigo aponta páginas oficiais do STF a obter/conferir. |
| Issue workshop #25, corpo e comentários; RESUME HERE 05/10; FLIGHT-LOG F-019…F-027; Writing Standard; Visual Casting; Visual Genres | regras vigentes | Preservar por padrão, justificar cortes, separar fonte/holding/posição, sem bastidores; figura como instrumento e sem redesenhar figuras canônicas. |

**Razão de fontes.** Os dois primários de saúde somam apenas algumas centenas de palavras para uma página atual de mais de três mil. A razão fica abaixo de 2:1; logo não há profundidade documental suficiente para uma reescrita factual de 3,5–4,3 mil palavras. Os 20 fundos pertencem às aulas anteriores e não suprem o inteiro teor de STA 175 ou as teses posteriores. A condição de entrada da redação é anexar os textos oficiais faltantes ao arquivo privado, com item ou página exatos, e atualizar A4; isto não refaz S0–S4 já concluídos.

### Inventário da página viva: preservar por padrão

| Peça atual | Decisão | Razão e tratamento |
|---|---|---|
| Hero “Saúde e diálogo institucional” e tensão entre ordem individual e coordenação | **KEEP / melhorar** | A pergunta é boa e abre o eixo. Cronologia de 2009–2026, nomes e descrições do hero só permanecem onde houver primário; a forma temporal pode ser preservada. |
| §01, pedido individual dentro do SUS, orçamento e alternativas terapêuticas | **KEEP / melhorar** | É a ponte do ECI para o sistema de saúde. Tirar a formulação genérica sobre “milhares de decisões corretas” se não houver dado; entrar por um caso documentado. |
| Aposta inicial STA 175 e revelação | **KEEP, condicionada** | A forma pode testar contracautela e mérito após os atos oficiais. Hoje, o resultado de busca só identifica STA 175 AgR; não usar paciente, objeto, dispositivo ou dano inverso como resposta. |
| §02, audiência de 2009; STA 175 × STA 178; decisão presidencial × agravo | **KEEP, condicionada** | Preservar essa distinção se os autos oficiais separados confirmarem partes, objetos, datas e resultados. Até lá, não afirmar que STA 175 e 178 envolvem a mesma paciente, nem atribuir ao colegiado razões do relator. |
| §03, Fig. 1 em quatro passos e quatro cartões de classificação | **REPLACE WITH BETTER no desenho; KEEP na função** | O desenho atual é sobretudo losangos/retângulos com palavras e seus cartões repetem parte do texto (F-026). Fazer ficha de decisão que um juiz preencheria, com saídas jurídicas verificáveis; preservar a separação registro/incorporação/competência quando houver teses oficiais. |
| §04, comissão, acordos, Tema 1234, SV 60 e SV 61 | **KEEP, condicionada** | Pode responder à dimensão institucional do eixo. Falta fonte primária no compêndio; inserir acórdão, atos posteriores e textos oficiais das súmulas antes de conservar conteúdo, números, datas ou efeitos. |
| §05, tabela autocontenção/intervenção, contraste com T-025 | **KEEP / melhorar** | A tese em dois planos é útil; cada célula precisa de suporte. O contraste com Aula 08 basta em um parágrafo, sem reensinar T-025. |
| §06 “Aprofundamento”, roteiro, casos A/B, conta, armadilhas | **MOVE para as seções correspondentes** | Preservar análise e exercícios, mas integrar regra, perto do caso e de sua fonte. Retirar só repetições literais dos §§02–05; compensar com razões judiciais comprovadas, divergências e consequências. |
| §07, seis questões em `<details>` | **KEEP / atualizar** | Manter teste ativo, uma armadilha por item, e encerrar com resposta ao eixo por casos. Não repetir toda a aula nas respostas. |

## A1. Contrato com o leitor

- **Já sabe:** as Aulas 07 e 08 são pré-requisitos do programa; a aula pode retomar seus conceitos estruturais, mas só usará caso e fundamento de seus autos se os trechos atribuídos estiverem acessíveis e conferidos.
- **Consegue fazer depois:** (1) explicar o limite do registro oficial do RE 566.471/RN; (2) aplicar o início do item 1 do Tema 6 a uma variação explícita de inclusão em lista; (3) separar essa regra material de competência e coordenação, caso o Tema 1234 e suas súmulas sejam incorporados; (4) responder ao eixo com holdings, razões e consequências de casos distintos efetivamente documentados.
- **Uma sessão:** projetar 3.7–4.3 mil palavras, 20–25 minutos. A página atual não deve perder palavras sem corte justificado; redundância deslocada de §06 abre espaço para fatos, fundamentos e votos documentados.

## A2. Armadilhas que distribuem a atenção

| # | Confusão | Por que surge | Um lugar de correção | Um teste |
|---|---|---|---|---|
| T1 | Atribuir ao Plenário da STA 175 todos os parâmetros do voto/decisão presidencial | Mesmo número de processo, peças de natureza distinta | §02, após disposição oficial verificada | pergunta 1 |
| T2 | Tratar STA 175 e STA 178 como um processo ou atribuir-lhes partes, objeto ou resultado comuns | O rascunho herdado afirma paciente e ordem de origem comuns, mas os atos disponíveis não confirmam esses dados | §02, somente depois de conferir os autos separados | pergunta 1, uma vez, condicionada à fonte |
| T3 | Inferir do trecho inicial do Tema 6 uma regra sobre medicamento sem registro ou sobre todos os pedidos fora da lista | O trecho disponível trata da ausência em listas, mas não fornece a tese integral nem o Tema 500 | §03, limitar o exercício ao que o item 1 efetivamente diz | pergunta 2, uma vez |
| T4 | Tratar competência ou custeio como requisito clínico do Tema 6 | As matérias aparecem juntas em discussões sobre medicamentos, mas dependem de teses distintas | §04, após incorporar Tema 1234 | pergunta 4, se a fonte entrar |
| T5 | Prescrição isolada bastar para exceção ao item 1 do Tema 6 | O laudo é concreto e urgente | §03, prova exigida **somente após obter tese integral** | pergunta 3 |
| T6 | Responder ao eixo como se diálogo significasse só autocontenção ou só substituição administrativa | Apaga a diferença entre decisões materiais e regras de coordenação | §05, comparação apenas entre holdings verificados de processos distintos | última pergunta-eixo, condicionada às fontes |

## A3. Cerca de escopo — SÓ PLANEJAMENTO, NUNCA NA PÁGINA

Aula 07 possui ECI e ADPF 347; Aula 08 possui T-025 e seus autos. Aqui, a passagem serve só para formular o teste do sistema de saúde. Não reabrir a cronologia colombiana nem transformar T-025 em precedente sobre medicamentos; qualquer comparação depende dos trechos primários de background disponíveis e conferidos. Tema 500 fica fora desta reconstrução; não abrir uma fronteira sobre registro sanitário. Tema 793, política farmacêutica geral, reexame de eficácia pela Conitec e litígios não medicamentosos ficam fora. A súmula ou decisão posterior só entra quando seu texto oficial e seu estado temporal estiverem no arquivo privado. Na página, no máximo uma referência de fronteira à Aula 08 onde o raciocínio pede a comparação.

## A4. Inventário de afirmações e localizadores privados

| # | Afirmação completa ou condição de inclusão | Estado | Localizador privado | Objeto/caso | § |
|---|---|---|---|---|---|
| C1 | O programa de 28/09 vincula o direito à saúde à organização do SUS, conhecimento técnico, audiências públicas e diálogo institucional. | contrato didático | `work/pipeline/direito-latino-americano/course-map.md`, linha da Aula 09; `compendium/aula-09/05-eixo.md` | RE 566.471 como âncora do tema, sem importar fatos além do registro | 01 |
| C2 | A página oficial identifica RE 566.471/RN como leading case do Tema 6 e registra o encerramento do julgamento virtual em 20/09/2024 e a fixação da tese em 26/09/2024. | registro processual | `chapters/re566471-official-docket/01-tema-6-docket-record.txt`, blocos “Leading case” e “Andamento exibido” | RE 566.471/RN | 01/03 |
| C3 | O trecho disponível do item 1 do Tema 6 diz que a ausência do medicamento nas listas de dispensação do SUS impede, como regra geral, o fornecimento judicial, independentemente do custo. | tese, somente o trecho transcrito no arquivo | `chapters/re566471-official-docket/01-tema-6-docket-record.txt`, bloco “Tese — início do item 1” | variação didática explícita sobre a frase publicada, sem atribuir fatos ao processo | 03 |
| C4 | O resultado de pesquisa oficial identifica a classe STA 175 AgR e não contém ementa, voto, dispositivo, data de julgamento ou fundamentação. | identificação e limite do registro | `chapters/sta175-official-search-record/01-official-search-result.txt`, “Resultado exibido” e “Registro correspondente nesta lista” | STA 175 AgR | 02, só como identificação até fonte adicional |
| C5 | O eixo pergunta se o diálogo institucional representa autocontenção judicial ou uma nova forma de intervenção das Cortes nas políticas públicas. | eixo literal | `compendium/aula-09/05-eixo.md`, “Eixo”; `course-map.md`, linha da Aula 09 | comparação entre holdings distintos, se comprovados | 05 |
| C6 | O índice e a triagem da Aula 09 mapeiam unidades de T-025/2004 e dos Autos 008/2009 como background; esse metadado não prova o conteúdo das decisões. | metadado de seleção; nenhum claim jurídico liberado | `triage/aula-09.csv`; `chapters/auto-008-09/index.json`; as passagens de texto não estão neste checkout | possível comparação de pré-requisito | 01/05, somente se os textos forem obtidos e conferidos |
| C7 | A T-153/1998 formulou questão sobre condições de cárcere em tutela individual (§ 2), descreveu causas gerais/estruturais e ordens a distintas entidades (§ 53), declarou o estado inconstitucional (§ 65) e ordenou medidas a vários órgãos (dispositivo). | fundamento de pré-requisito; não é regra de saúde | `chapters/t-153-98/04-problema-juridico.txt` (§ 2), `55-consideracion-53.txt` (§ 53), `67-consideracion-65.txt` (§ 65), `68-decision.txt` (dispositivo) | transição conceitual, sem reensinar a Aula 07 | 01, opcional após conferência |

### Ledger de fontes ausentes e resolução obrigatória

| Caso/afirmação candidata | O que está no compêndio agora | Primário a incorporar e localizar | Resolução de escrita |
|---|---|---|---|
| STA 175 AgR | Só a identificação no resultado de busca oficial; nenhum mérito. | Ementa/acórdão integral e ato presidencial, com páginas/itens para partes, objeto, data, dispositivo, razões, votos e consequência. | Até entrar e ser conferido, não narrar paciente, medicamento, pedido, audiência, resultado, dano inverso ou holding. A identificação pode permanecer apenas neste plano. |
| STA 178 | Nenhuma unidade primária atribuída à Aula 09. | Ato oficial próprio da STA 178 e, se necessário, acórdão/decisão de origem, com os mesmos campos localizados separadamente da STA 175. | Não afirmar partes, objeto, relação com STA 175, paciente ou resultado comum; manter fora da página até a fonte sustentar cada relação. |
| RE 566.471 / Tema 6 | Registro oficial com tema, leading case, datas de andamento e somente o início do item 1. | Acórdão e tese integral oficiais, com item/parágrafo/página para cada requisito, fundamento, voto e desdobramento; texto oficial da SV 61. | Por ora, usar só C2–C3. Não incluir exceções, requisitos, NatJus, Conitec, divergência ou efeitos posteriores sem locador próprio. |
| RE 1.366.243 / Tema 1234 | Nenhum texto primário indexado nesta aula. | Acórdão/tese, acordos homologados, decisões/embargos posteriores até a data de redação e texto oficial da SV 60, cada qual com página/item e situação temporal. | Não afirmar competência, limiar, custeio, percentual, fluxo, regra oncológica, voto ou status atual enquanto faltar o locador. Comparação institucional só após essa resolução. |
| RE 657.718 / Tema 500 | Nenhum texto primário indexado nesta aula. | Acórdão/tese oficial com itens sobre registro sanitário, exceções, legitimidade e votos. | Tema 500 fica fora do corpo planejado. Só reabrir como fronteira se o texto oficial for incorporado; nesse caso, registrar os locadores e claims aqui antes de escrever. |
| SV 60 e SV 61, consideradas separadamente | Nenhum texto oficial indexado nesta aula. | Texto oficial de cada súmula e decisão que fixe seu alcance temporal, com enunciado e itens pertinentes. | Não atribuir conteúdo ou efeito temporal às súmulas a partir do nome, de resumo ou do HTML antigo. |

**Regra das fichas.** Para cada caso efetivamente mantido na página, preencher tribunal, ano, questão, decisão, razões, divergência identificada e sequência posterior com locadores do próprio ato. Se a fonte não registrar divergência, não inventar uma; a página também não precisa anunciar essa ausência. Separar sempre registro, decisão monocrática, voto e dispositivo colegiado. O material de T-025/T-153 só sustenta a ponte de pré-requisito indicada em C6/C7.

## A5. Fio: uma controvérsia real, em processos distintos

**Âncora escolhida:** RE 566.471/RN, identificado oficialmente como leading case do Tema 6. O fio pergunta como o Judiciário trata um pedido de medicamento fora das listas: primeiro, o que o registro disponível permite dizer sobre o RE 566.471/RN; depois, o que o trecho publicado do item 1 permite testar. As variações “consta/não consta” são exercícios declarados sobre esse texto, não fatos do RE. STA 175/178 e Tema 1234 podem entrar como carriers locais separados somente quando seus atos oficiais forem incorporados. Nunca apresentar STA 175, RE 566.471 e RE 1.366.243 como etapas do mesmo processo ou do mesmo paciente. O S3 lista fundos colombianos, mas a ausência de texto local impede usá-los por ora como prova de comparação.

| Candidato real | §01 problema | §02 caso | §03 regra material | §04 coordenação | §05 eixo | Veredito |
|---|---|---|---|---|---|---|
| RE 566.471/RN, leading case indicado no registro oficial | abre pelo objeto do tema e pelo limite do registro | aparece apenas como processo distinto se comparado à STA 175 verificada; sem presumir ligação factual | carrier principal do item 1, limitado ao trecho efetivamente disponível | só reaparece como processo distinto se a competência/coordenação tiver fonte própria | um dos casos comparados, sem inventar razões | **âncora escolhida**, pois o docket e o começo do item 1 estão nos primários locais |
| STA 175 AgR | não fornecer fato de abertura enquanto falta o ato | carrier local potencial, após acórdão/decisão primários | não transportar seus fatos para o Tema 6 | não é prova do Tema 1234 | pode responder ao eixo só após holding e fundamentos localizados | candidato condicional, atualmente só identificado por busca |
| STA 178 | não fornecer fato de abertura enquanto falta o ato | carrier separado potencial, após ato próprio | não importar resultado da STA 175 | não é prova do Tema 1234 | só entra se o ato permitir comparação | candidato condicional sem unidade primária atual |
| RE 1.366.243/Tema 1234 | não é a solicitação individual-âncora | caso institucional posterior, separado do RE 566.471 | não resolver a regra material do Tema 6 | carrier próprio de coordenação, apenas após acórdão/súmulas | compara desenho de fluxo com controle do caso individual | candidato condicional sem unidade primária atual |
| T-025 e Autos colombianos | só após obter os textos de background | caso de outra política | nenhuma tese de medicamento | não usar como prova de competência SUS | comparação apenas se as unidades forem conferidas | manter como pré-requisito potencial, sem segundo percurso |

**Teste de continuidade:** §01 parte do registro oficial do RE 566.471; §02 identifica separadamente o que falta para a STA, sem inventar o seu mérito; §03 aplica uma variação didática apenas ao início do item 1 do Tema 6; §04 só usa o Tema 1234 como processo distinto quando sua fonte chegar; §05 compara os limites institucionais que os atos oficiais efetivamente mostrarem. Se §02 ou §04 não receber fonte, não preencher a lacuna com RE 566.471 nem com detalhes do HTML antigo.

## A6. Plano das seções

| § | h2 informativo | Pergunta respondida | A4 | Carrier | Forma | Palavras | Ideia entregue à próxima seção |
|---|---|---|---|---|---|---:|---|
| hero | Saúde e diálogo institucional | Qual problema institucional está em jogo no fornecimento de medicamentos? | C1/C2/C5 | Tema do RE 566.471 conforme descrição oficial, sem fatos individuais não registrados | manter a tensão; sem cronologia factual sem fonte | 90 | há um processo identificável e um limite sobre o que seu registro informa |
| 01 | O pedido de medicamento dentro do SUS | O que se pode perguntar a partir do RE 566.471 sem completar o docket por inferência? | C1/C2 | RE 566.471/RN como âncora; sem ponte factual colombiana até conferir seus trechos | prosa concreta + exercício de leitura do registro | 480 | o registro identifica o Tema 6, mas não substitui o ato de outro processo |
| 02 | STA 175 e STA 178: atos separados | O que decidiu cada ato, e qual parte é colegiada? | C4 + ledger STA 175/178 | cada procedimento em sua própria ficha, só após primários incorporados | fichas separadas + razões; sem figura nova | 630, apenas se ambos os atos sustentarem o conteúdo | se a peça oficial confirmar a suspensão, seu resultado processual não vira a tese geral do Tema 6 |
| 03 | A lista do SUS e o início do item 1 do Tema 6 | O que o trecho disponível diz quando falta inclusão em lista? | C2/C3; ledger Tema 6 para qualquer extensão | RE 566.471/RN; variação explicitamente didática sobre a frase disponível | instrumento de decisão + aplicação limitada; sem exceções não documentadas | 950, expandir só após tese/acórdão integral | a regra material e a organização do processo são perguntas distintas |
| 04 | Competência e coordenação federativa | O que os atos do Tema 1234 determinam sobre fluxo e responsabilidades? | ledger Tema 1234 + SV 60 | RE 1.366.243 como processo distinto, se fontes oficiais incorporadas | prosa de caso e tabela de relações paralelas se os dados forem provados | 760, somente se a fonte for incorporada | o que o acórdão disser sobre fluxo deve ser separado da questão material, conforme locadores oficiais |
| 05 | Autocontenção judicial e intervenção institucional | Como os casos verificados respondem ao eixo literal? | C5 e claims adicionados após resolver o ledger | comparação de processos distintos com tribunal, ano, holding, razão e efeito comprovados; eventual ponte colombiana só com texto conferido | prosa argumentativa; sem tabela que repita as razões | 520, condicionado ao lastro de §§02–04 | a resposta final precisa citar casos distintos e a razão de cada um |
| 06 | Aplicação ao pedido de medicamento | O estudante separa o que o registro mostra, o que o Tema 6 diz e o que ainda exige outra tese? | C2/C3 e apenas claims com fonte resolvida | variações expressas sobre o texto real do RE 566.471 | `<details>`: questões independentes e pergunta final de eixo | 240 | termina com resposta ao eixo por casos efetivamente documentados |

**Total projetado:** cerca de 3.670 palavras mais títulos e respostas, condicionado às fontes necessárias para §§02, 04 e 05. A página atual ainda fornece baseline de palavras e itens aproveitáveis; o escritor mede-a imediatamente antes da edição e não reduz o total sem registrar em A8 cada corte e sua razão. As variações do Tema 6 são exercícios sobre o trecho publicado do RE 566.471, não novos fatos. Nenhuma seção pode usar os dados de STA 175/178 ou Tema 1234 para completar o RE 566.471, nem vice-versa. Se os primários faltantes não forem incorporados, não redigir os claims suspensos nem manter a página viva factual como se ela fosse fonte. A alternância é prosa em §01, fichas de caso em §02, instrumento em §03, prosa/tabela em §04 e prosa em §05. Cada seção termina na ideia que a seguinte precisa.

## A7. Elenco visual: escolher um instrumento para o juiz

**Movimento único:** dado um pedido real de medicamento, o leitor preenche os fatos juridicamente relevantes e vê qual pergunta o juiz ainda deve responder. A figura não deve prometer a solução que a fonte não entrega.

| Candidato, família | Swap / ledger / objeto / verbo | Decisão |
|---|---|---|
| Cronologia 2009–2026, como o hero atual | Datas específicas tornam o objeto próprio, mas a cronologia apenas **ordena**. O curso já usa várias; trocar nomes funcionaria em outra aula. Não decide o pedido. | **Manter como hero, condicionado** à fonte de cada marco; não escolher para a tese central. |
| Árvore de ramos, como a Fig. 1 atual | O objeto é o pedido, mas os retângulos e setas carregam palavras; sem texto sobra pouca decisão. A mesma forma serve a qualquer tese e o ledger marca `dla-a09-s2+3` apenas aceitável. | **Substituir com razão escrita:** F-026 e teste do objeto/verbos. Preservar suas distinções comprovadas. |
| Dossiê de um caso, com abas Fatos/Questão/Decisão/Razões/Depois | Ótimo para STA 175 e próprio da lei, mas o leitor apenas lê uma decisão passada; não executa os filtros de um novo pedido. A Aula 05 já usa o julgamento como objeto comentado. | Usar ficha textual no §02, não como figura central. |
| **Formulário de decisão para o pedido de medicamento** | O objeto do RE 566.471/RN e as palavras do item 1 sobre listas de dispensação e custo particularizam a ficha; o leitor **marca** presença/ausência e a consequência do trecho fica visível. | **Escolhido.** Só este faz o limite documentado trabalhar diante do leitor, sem tabelar a doutrina em SVG. |

**Folha escolhida, de cima para baixo.** Usar o RE 566.471/RN como carrier real. A ficha pergunta apenas se o medicamento consta nas listas de dispensação do SUS. Em “não”, mostra a consequência geral do início do item 1, inclusive “independentemente do custo”; em “sim”, marca “este trecho não resolve o resultado”. Não acrescentar campos de registro, prova clínica, negativa administrativa ou competência sem as respectivas teses oficiais. O cartão afirma somente a proposição C3 e aponta para esse mesmo processo, sem inventar paciente ou resultado. Em 375 px, manter a ficha retrato e textos em HTML, sem caixas SVG de parágrafos.

O desenho atual do hero e a Fig. 1 não são da lista de figuras canônicas A01/A03/A04/A05/A06/A07/A08 no RESUME HERE. Mesmo assim o padrão é preservá-los; a troca da Fig. 1 precisa passar nos quatro testes de Visual Casting e manter sua função. Não redesenhar figuras de outras aulas. Captura somente do seletor alterado, e nenhum novo achado em 1280/375 sobre a linha de base de Latam.

## A8. Cortes e deslocamentos justificados

- **Não cortar por conveniência de tamanho** a análise de STA 175/178, Tema 6, Tema 1234 e a resposta ao eixo; isso não libera claims sem fonte. Cada trecho só fica na versão reconstruída se as fontes do ledger A9 o sustentarem.
- **Cortar do corpo desta reconstrução** as afirmações herdadas sobre RE 657.718/Tema 500 e falta de registro: estão fora do escopo atual e não há primário atribuído. Não conservar requisitos, exceções ou legitimidade do HTML antigo.
- **Cortar até comprovação** fatos de paciente, medicamento, pedidos, audiência, resultado e razões de STA 175/178, assim como qualquer regra ou status do Tema 1234/SV 60/61 que não receba fonte oficial e locator próprio. A página viva não funciona como prova.
- **Deslocar** os quatro blocos de “Aprofundamento” para §§02–05: hoje repetem o roteiro, os três deveres e a oposição autocontenção/intervenção. Eliminar apenas a segunda enunciação de cada regra; usar o espaço para razões e votos efetivamente documentados. Registrar a conta de palavras antes/depois.
- **Cortar da página final** linguagem de bastidor como “a aula pergunta”, “armadilha de prova”, “aprofundamento” genérico e avisos de busca/processamento de fontes. Substituir por enunciados jurídicos e títulos informativos, sem compensação verbal.
- **Condicionar, não afirmar**, voto vencido em cada Tema, datas de embargos, percentuais de ressarcimento, limiar de 210 salários e efeitos oncológicos a localizadores oficiais atuais. Nenhuma alegação temporal provém dos dois primários S4.
- **Se T-025 permanecer na comparação**, limitar a um parágrafo e só usar unidades cujo texto primário esteja acessível e conferido; cronologia, ordens e orçamento permanecem na Aula 08.

## A9. Falhas próprias desta aula e contramedidas

| Risco | Contramedida concreta |
|---|---|
| Registro de busca virar acórdão | O arquivo STA 175 só autoriza identificar STA 175 AgR; não preencher decisão, razões, paciente ou resultado sem ato oficial. |
| STA 175 e STA 178 fundidas | Manter fichas e locadores separados. A relação entre partes, pedido e origem só aparece se cada ato a documentar. |
| Tese parcial virar tese completa | O arquivo do Tema 6 sustenta somente o início do item 1. Requisitos, exceções, NatJus, Conitec, votos e SV 61 aguardam fontes e itens próprios. |
| Tema 6 e Tema 1234 virarem um litígio | Marcar RE 566.471 e RE 1.366.243 como processos distintos; separar direito material, competência e custeio. |
| Tema 1234 ou súmula ficar temporalmente desatualizado | Antes de escrever, incorporar acórdão, homologações/incidentes posteriores e SV 60; conferir situação atual e registrar data/itens no ledger abaixo. |
| Tema 500 entrar por sobra do HTML | Tema 500 está fora do corpo. Reabrir só com RE 657.718 oficial no compêndio e claims/locadores novos em A4. |
| Fonte faltante ser narrada ao aluno | Lacunas e resoluções ficam aqui; a página simplesmente não contém claims sem fonte (F-019–F-021). |
| Eixo virar “ambos” sem argumento | Fecho responde literalmente se o diálogo expressa autocontenção ou nova intervenção, usando holding, razão e efeito documentados de cada processo comparado. |
| Figura virar tabela reescrita em SVG | Manter a ficha executável limitada ao trecho do item 1; retirar os nós de texto e confirmar que o instrumento ainda funciona (F-025/F-026). |
| Repetição e queda de volume | Uma regra em seu local e um teste; comparar o total ao baseline e registrar cada remoção no PR. |

### Resolução do ledger antes da escrita

A escrita de §§02–05 só começa depois de atualizar esta matriz com caminho exato do arquivo primário incorporado, páginas/itens, data de consulta, fatos resolvidos e claims liberados. O estado atual é “pendente” para todas as entradas abaixo, salvo o uso limitado de C2–C3 e C4.

| Entrada | Estado atual | Ação que libera uso | Claims liberáveis |
|---|---|---|---|
| STA 175 | Pendente; há apenas resultado de busca identificador | Incorporar e conferir ementa/acórdão e decisão presidencial; registrar partes, objeto, data, dispositivo, razões, votos e sequência com locadores separados por peça | Somente campos confirmados individualmente; não inferir STA 178 |
| STA 178 | Pendente; nenhum ato próprio no S4 | Incorporar decisão/acórdão oficial próprio e localizar partes, objeto e dispositivo | Somente sua ficha própria e relações explicitamente provadas com STA 175 |
| RE 566.471 / Tema 6 | Parcial; C2 e o início de C3 disponíveis | Acrescentar inteiro teor/tese oficial e mapear cada requisito, fundamento, voto e efeito; incorporar SV 61 e seu alcance | Expandir além do trecho de C3 apenas após os itens correspondentes serem conferidos |
| RE 1.366.243 / Tema 1234 | Pendente; nenhum primário local | Incorporar acórdão/tese, acordo(s), incidentes/embargos posteriores e SV 60; registrar estado atualizado com data e itens | Competência, fluxo, custeio, limiares, percentuais, regra oncológica e divergências, cada qual apenas se locado |
| SV 60 | Pendente; sem enunciado oficial local | Incorporar texto oficial e conferir sua relação com Tema 1234 e eventuais decisões posteriores | Só o alcance literal e temporal comprovado |
| SV 61 | Pendente; sem enunciado oficial local | Incorporar texto oficial e conferir a relação com Tema 6/acórdão | Só o alcance literal e temporal comprovado |
| T-025/2004, Autos 008/2009 e T-153/1998 (eventual comparação de pré-requisito) | Os índices/triage registram os IDs, mas parte dos textos de background não está disponível neste checkout | Tornar acessíveis e conferir as unidades exatas antes de usar qualquer holding, razão ou ordem | Sem texto conferido, não usar essas decisões como evidência no eixo |
| RE 657.718 / Tema 500 | Fora do escopo atual; nenhum primário local | Só se o escopo for alterado: incorporar acórdão/tese oficial, atualizar A3/A4 e localizar todas as condições | Se não resolvido, permanece excluído sem referência factual |

**Fonte a fonte:** ao incorporar um ato, conferir cada claim alterado exatamente no item/página anotado e manter claro se é registro, decisão monocrática, voto, acórdão colegiado ou súmula. Nenhum status de pauta antigo do rascunho vale como status atual sem nova consulta oficial.

## A10. Aceitação para as etapas seguintes

Antes de liberar escrita, atualizar A4 e a matriz A9 com os primários oficiais efetivamente incorporados, suas datas de consulta, trechos/itens e o resultado de cada pendência. Manter condicionais apenas no plano. O escritor só entrega tribunal, ano, decisão, razões, divergência documentada e sequência posterior por caso quando cada campo tiver locador próprio; STA 175, STA 178, RE 566.471 e RE 1.366.243 permanecem processos distintos. A última pergunta deve responder literalmente ao eixo com esses casos verificados. Depois da redação: `slop_lint` 0 hard, `check_all` PASS, `anatomy_check` PASS, `breakscan` sem achados novos a 1280/375, relógio “Leitura” alinhado ao índice, três parágrafos lidos em voz alta e palavras finais comparadas ao baseline/cortes de A8. A página não contém esta cerca, lacunas, localizadores privados ou comentários `REF ·`.
