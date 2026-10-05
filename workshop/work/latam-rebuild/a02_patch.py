# LAT-1 · Latam Aula 02 (Cortes e democratização): rebuild on the live page (Claude, 05/10).
# Blueprint written by Codex, reviewed by the CEO in place of the S5a panel: APPROVED with one change (the
# Gelman/SCJ 20/2013 micro-case is Aula 05's and is not imported here; its T4 test goes with it).
# Keeps hero, the paradox, the study's method, Fig. 1 (axis), Fig. 2 (atlas), the 19-country table and the quiz;
# folds the ~1,900-word "Aprofundamento" into the chapters (F-021); removes exam talk and the roadmap (F-019/F-020);
# fixes three facts (Argentina diffuse / Uruguay concentrated with effects in the case; the Colombian Supreme Court
# studied ≠ the Constitutional Court; the undated table is not "hoje"); adds the five countries' histories from
# Engelmann & Bandeira (1994 and 2003 in Argentina, AI-2/AI-5 and 1988 in Brazil, Allende/Pinochet in Chile,
# 1957/1991/Uribe in Colombia, 1968/1999/2002 in Venezuela) and the sample's limits.
import re, sys
sys.path.insert(0, '/Users/benecles/Developer/ordenacoes-filipinas-workshop/work/latam-rebuild')
from fk import set_step

P = sys.argv[1]
s = open(P).read()
def chapter(n, title, lede, tone=''):
    return (f'<section class="chapter" aria-labelledby="c{n}"><span class="num {tone}" aria-hidden="true">{n:02d}</span>'
            f'<h2 id="c{n}">{title}</h2><p class="lede">{lede}</p></section>\n')
def longform(*paras): return '<div class="longform"><div>' + ''.join(paras) + '</div></div>\n'
def p(t): return f'<p>{t}</p>'
def h3(t): return f'<h3>{t}</h3>'
def item(q, a): return f'<details><summary>{q}</summary><p>{a}</p></details>'
def grab(pat, src=None):
    m = re.search(pat, src or s, re.S); assert m, pat[:50]; return m.group(0)

i_c1 = s.index('<section class="chapter" aria-labelledby="c1"')
i_end = s.index('<nav class="endnav"')
scrolls = [m.start() for m in re.finditer(r'<div class="scrolly">', s)]
def until_next(a, marker):
    return s[a:s.index(marker, a)]
fig1 = until_next(scrolls[0], '<section class="chapter"')
fig2_block = until_next(scrolls[1], '<section class="chapter"')       # scrolly + wide table + its longform
fig2 = fig2_block[:fig2_block.index('<div class="wide">')]
table = grab(r'<div class="wide">\s*<div class="table-wrap".*?</table></div>\s*</div>', fig2_block)
bet = grab(r'<div class="bet">.*?(?=<section class="chapter")')
defs = ''.join(re.findall(r'<svg width="0" height="0"[^>]*>.*?</svg>', s[i_c1:i_end], re.S))
old_items = re.findall(r'<details>.*?</details>', s[s.index('<div class="quiz">'):i_end], re.S)

p_paradox = grab(r'<p>A aula parte de um estudo de Fabiano Engelmann.*?</p>').replace('A aula parte de um estudo', 'O ponto de partida é um estudo').replace('O ponto de partida é um paradoxo.', 'O estudo começa por um paradoxo.')
p_method = grab(r'<p>A maior parte da literatura sobre “judicialização da política”.*?</p>')
p_traits = grab(r'<p>Alguns traços aparecem em toda parte.*?</p>')
p_ethos1 = grab(r'<p>Garantias escritas organizam o cargo.*?</p>')
p_ethos2 = grab(r'<p>Isso explica por que origem profissional e regra de nomeação.*?</p>').replace(' A prova deve indicar qual poder ganha influência, que proteção institucional aparece e qual custo de representação ou fechamento acompanha o arranjo.', ' Uma análise precisa indicar qual poder ganha influência, que proteção institucional aparece e que custo de representação ou de fechamento acompanha o arranjo.')
p_q3a = grab(r'<p>A literatura que Engelmann e Bandeira organizam.*?</p>')
p_q3b = grab(r'<p>Essas perguntas não se substituem\..*?</p>')
p_counter = grab(r'<p>O argumento contramajoritário parte de um problema real:.*?</p>')
p_objection = grab(r'<p>A objeção democrática também tem força:.*?</p>')
p_patho = grab(r'<p>Engelmann e Bandeira descrevem duas patologias.*?</p>')
p_composition = grab(r'<p>A coluna de composição e seleção também mede coisas diferentes\..*?</p>')
p_temporal = grab(r'<p>A temporalidade impõe outro cuidado\..*?</p>')
p_apply = grab(r'<p>Para responder se o fortalecimento das Cortes favorece a democratização.*?</p>')
p_apply2 = grab(r'<p>Esse roteiro mantém separadas as evidências das duas leituras\..*?</p>')
p_expansion = grab(r'<p>A expansão da jurisdição constitucional é a resposta da redemocratização.*?</p>')

# ---------- Fig. 1 card fix: the Colombian court studied is the Supreme Court, not the Constitutional Court
fig1 = fig1.replace(' É a Corte que as Aulas 04 e 07 mostram em ação.', ' A Corte estudada aqui é a Corte Suprema de Justicia; desde 1991, a revisão constitucional cabe a outro órgão, a Corte Constitucional.')
assert 'Aulas 04 e 07' not in fig1

# ---------- 01 · the question
c1 = chapter(1, 'A pergunta', 'Por que, depois das ditaduras, algumas cortes latino-americanas viraram atores políticos centrais e outras não?') + longform(
    p('A <a href="aula-01.html">Aula 01</a> terminou com a redemocratização entregando às cortes a guarda de Constituições cheias de direitos. Resta saber o que aconteceu com essa entrega. Todas as cortes da região ganharam o mesmo poder? Usaram-no do mesmo jeito?'),
    p_paradox,
    p('O teste mais claro do paradoxo é um par. Brasil e Argentina escolhem os ministros da corte mais alta pela mesma porta, indicação do presidente com aprovação do Senado, e mesmo assim tiveram histórias opostas: uma corte reiteradamente trocada por cada governo, outra estável desde 1988. A regra de nomeação explica pouco; a pergunta é o que explica o resto.'),
)

# ---------- 02 · three questions that are often mixed
c2 = chapter(2, 'Autonomia, protagonismo e direitos', 'Três perguntas diferentes sobre a mesma corte.') + longform(
    p_q3a, p_q3b,
    p('Daí as três perguntas que o senso comum costuma misturar. <strong>Autonomia</strong>: a corte está protegida de pressões externas? <strong>Protagonismo</strong>: ela intervém em disputas políticas? <strong>Proteção de direitos</strong>: a intervenção serve a quem? Uma corte pode ter autonomia alta e pouco protagonismo, ou muito protagonismo sem proteger direitos. O estudo de Engelmann e Bandeira responde sobretudo à primeira pergunta.'),
)

# ---------- 03 · who entered the five courts
c3 = chapter(3, 'Quem entrou nas cinco cúpulas, 1990–2015', 'Não pelas decisões, mas pelas pessoas que as tomam.') + longform(
    p_method,
    p('As fichas cobrem 18 ministros na Argentina, 31 no Brasil, 67 no Chile, 74 na Colômbia e 96 na Venezuela. Os números refletem o desenho de cada corte, não o tamanho do problema: a Corte Suprema chilena tem 21 cadeiras vitalícias, e a colombiana, 23 membros com mandatos de oito anos desde 1994. As fontes também são desiguais. Os sites das cortes, em quase todos os casos, eram insuficientes, e foi preciso recorrer aos principais jornais de cada país. No Chile, não se obteve informação sobre 15 dos 67 magistrados, nove deles indicados por Pinochet. A amostra permite descrever padrões, não calcular um índice de independência.'),
    p('Um cuidado de nome evita um erro recorrente. Na Colômbia, os 74 ministros estudados são da <strong>Corte Suprema de Justicia</strong>. A Constituição de 1991 transferiu o controle de constitucionalidade para um órgão novo, a <strong>Corte Constitucional</strong>, que não está no universo do estudo.'),
    p_traits,
    p('As diferenças aparecem quando se cruzam esses dados com a história política de cada país. É aí que surgem os dois caminhos.'),
) + bet + '\n'

# ---------- 04 · same door, two paths (Fig. 1 kept)
c4 = chapter(4, 'A mesma porta de entrada, duas trajetórias', 'Argentina e Brasil nomeiam do mesmo jeito e chegaram a lugares opostos.') + defs + fig1 + longform(
    h3('Argentina: a corte trocada a cada governo'),
    p('A instabilidade argentina vem de longe. A própria Corte validou por acordadas os golpes de 1930, 1943, 1955, 1962, 1966 e 1976, e em 1947 o governo eleito de Perón destituiu quatro dos cinco ministros justamente por terem legitimado o golpe de 1930. O padrão se repetiu na democracia. Nos primeiros meses de governo, Menem ampliou a Corte de cinco para nove ministros; dois juízes renunciaram em protesto, e os seis nomeados, com laços estreitos com o presidente, ficaram conhecidos como a “maioria automática”. Ainda assim, foi sob Menem que a reforma constitucional de 1994 introduziu concurso público para os tribunais inferiores e ampliou a maioria do Senado exigida para aprovar os ministros da Corte Suprema.'),
    p('Em 2003, Néstor Kirchner propôs o impeachment dos quatro ministros que restavam da “maioria automática”: três renunciaram e um foi destituído pelo Congresso. Para preencher as vagas, em vez de nomeações políticas, vieram mecanismos que limitam a discricionariedade do presidente: a composição deve refletir diversidade de gênero, de especialidade e de origem regional, e os candidatos passaram a ser divulgados, com uma instância de participação pública. É o ponto em que a autonomia da Corte argentina se torna mais visível, inclusive em confrontos abertos com o Executivo.'),
    h3('Brasil: a mesma porta, outra história'),
    p('O Judiciário brasileiro esteve historicamente ligado ao poder político, muitas vezes exercido pelas mesmas pessoas. A profissionalização começou, paradoxalmente, sob Vargas, com o concurso para a primeira instância e a preferência por ministros do STF menos ligados à vida partidária. A ditadura atingiu a corte diretamente: depois de habeas corpus contrários ao governo, o AI-2 aumentou o STF de 11 para 16 ministros e mandou julgar civis na Justiça Militar; com o AI-5, em 1968, três ministros foram cassados e dois renunciaram em solidariedade.'),
    p('Depois de 1988, o quadro se inverte: o recrutamento passa a valorizar a expertise e a origem no próprio meio jurídico, e a composição do STF deixa de ser alvo de trocas por pressão política. Para os autores, o que separa o Brasil da Argentina não é a regra de nomeação, que é a mesma, mas a estabilidade institucional e a preocupação das elites políticas com a legitimação jurídica de suas decisões.'),
)

# ---------- 05 · cooptation, closure and political pressure
c5 = chapter(5, 'Cooptação, fechamento e pressão política', 'Chile, Colômbia e Venezuela mostram o que a regra escrita não mostra.') + longform(
    h3('Chile: independência corporativa, para quê?'),
    p('A Corte Suprema chilena acumula, desde o século XIX, faculdades disciplinares e participação na escolha de seus juízes: o presidente nomeava a partir de listas elaboradas com a própria instituição. Essa cooptação produziu uma carreira altamente estruturada, em que os ministros percorrem todas as instâncias antes de chegar ao topo. Mas a independência corporativa não se traduziu em defesa de direitos. Durante o governo Allende, a Corte usou pela primeira vez, de modo sistemático, o poder disciplinar para expulsar juízes simpáticos às ideias do governo. Depois do golpe de 1973, a junta assegurou o funcionamento normal do Judiciário, e os tribunais sustentaram a estrutura institucional do regime ancorados no discurso da própria independência.'),
    h3('Colômbia: cooptação, quotas e uma corte que perdeu o controle constitucional'),
    p('Na Colômbia, a independência orgânica veio em 1957, quando a Junta Militar que ordenou a transição para a Frente Nacional incluiu no referendo a cooptação direta da Corte Suprema. A cooptação não impediu a divisão: as quotas partidárias foram mantidas informalmente durante a Frente Nacional. Nos anos 1980, a Corte acumulou vitórias contra o governo, a ponto de se falar em “governo dos juízes”. A Constituição de 1991 respondeu com carreira judicial e concursos para a primeira instância, um Conselho Superior da Judicatura que passou a participar das nomeações e a criação da Corte Constitucional, cujos ministros o Senado escolhe a partir de listas do presidente, da Corte Suprema e do Conselho de Estado.'),
    p('Mesmo sem o controle de constitucionalidade, a Corte Suprema manteve protagonismo, sobretudo nos processos de desmobilização de paramilitares e guerrilhas, e nem sempre foi respeitada: o embate com Álvaro Uribe (2002–2010) chegou ao escândalo das <em>chuzadas</em>, as interceptações ilegais descobertas contra os juízes.'),
    h3('Venezuela: regras escritas, prática provisória'),
    p('Na Venezuela, a estabilidade política do pacto de elites converteu a judicatura em área de repartição entre os partidos. O Consejo de la Judicatura, criado em 1968 para nomear e disciplinar os juízes de primeira e segunda instância, foi rapidamente instrumentalizado: deixou de fazer os concursos previstos e consolidou a prática de designar juízes suplentes ou provisórios. A Constituição de 1999 previu ingresso na carreira por concurso, com formação pela Escuela Nacional de la Magistratura, mas desde 2002 não houve novos concursos, e as designações seguiram sem controle. É o caso que mostra com mais nitidez a distância entre a regra escrita e a prática.'),
    h3('A autonomia também se constrói por práticas'),
    p_ethos1, p_ethos2,
)

# ---------- 06 · where review happens (Fig. 2 + table kept, prose corrected)
c6 = chapter(6, 'Onde a revisão constitucional acontece', 'Dezenove países, quatro formas de organizar o controle de constitucionalidade.') + longform(
    p('Um quadro das cortes constitucionais latino-americanas responde a outra pergunta: não como as cortes conquistaram autonomia, mas que desenho cada país deu ao controle de constitucionalidade, tal como o quadro o registra, sem indicar ano-base.'),
) + fig2 + table + '\n' + longform(
    p('O asterisco indica o número de integrantes da sala constitucional, e não da corte suprema inteira. Lido em colunas, o quadro mostra quatro coisas.'),
    p('<strong>Onde está o controle.</strong> Há tribunais constitucionais autônomos, separados do Judiciário ordinário (Bolívia, Chile, Colômbia, Equador, Guatemala, Peru, República Dominicana); salas constitucionais dentro das cortes supremas (Costa Rica, El Salvador, Honduras, Nicarágua, Paraguai, Venezuela); cortes supremas que acumulam a função (Argentina, Brasil, México, Panamá, Uruguai); e um caso de controle político, Cuba, onde quem controla é a própria Assembleia.'),
    p('<strong>Quem escolhe.</strong> A maioria combina Executivo e Legislativo, às vezes com maioria qualificada de dois terços (Argentina, Costa Rica, Uruguai). Alguns dão peso à própria magistratura (República Dominicana, Honduras, Paraguai) ou a concursos (Equador). Bolívia e México, segundo o quadro, escolhem seus juízes constitucionais pelo voto popular. Cooptação, nomeação política e eleição direta são três respostas diferentes à mesma tensão entre independência e legitimidade democrática.'),
    p('<strong>Como se controla.</strong> O controle pode ser difuso, exercido por qualquer juiz no caso concreto, como na Argentina, ou concentrado num órgão. Concentrado não quer dizer efeitos gerais: no Uruguai, o controle é concentrado na Suprema Corte, mas seus efeitos ficam limitados ao caso. Pode ainda ser preventivo, antes de a lei valer, como no Chile e na República Dominicana, ou repressivo. O Brasil combina tudo, num sistema difuso e concentrado “muito amplo”.'),
    p('<strong>Quem chega à corte.</strong> Tutela, amparo e habeas corpus são vias pelas quais o cidadão leva diretamente uma violação de direitos à jurisdição constitucional. Foi pela tutela colombiana que chegaram à Corte Constitucional os casos das prisões e do deslocamento forçado.'),
    p_composition, p_temporal,
)

# ---------- 07 · are strong courts good for democracy?
p_expansion = p_expansion.replace('A Aula 01 mostrou por que isso importa numa região de presidentes fortes.', 'Numa região de presidentes fortes, isso importa.')
c7 = chapter(7, 'Cortes fortes são boas para a democracia?', 'O estudo não responde com um sim; mostra por que a pergunta é ambivalente.') + longform(
    p_expansion, p_counter, p_objection, p_patho,
    p('Aplicadas aos cinco países, as três perguntas do início dão respostas diferentes. Na leitura dos autores, o Chile combina autonomia alta com distância das transformações do país, e sua independência conviveu com a ditadura; o Brasil tem autonomia e protagonismo, e a proteção de direitos varia conforme o caso, inclusive com um ativismo punitivo no “combate à corrupção”; a Argentina mostra que autonomia pode ser conquistada tarde, por regras que limitam o presidente; a Venezuela, que regras sem prática não bastam.'),
)

# ---------- 08 · answer with design and countries
c8 = chapter(8, 'Responder com o desenho e com os países', 'Separar as evidências antes de concluir.', 'dif') + longform(
    p_apply, p_apply2,
    '<p class="eixo"><b>Exercício</b>Em que condições a autonomia das cúpulas judiciais favorece a democratização, e quando pode coexistir com fechamento corporativo ou com pressão política? Responda comparando pelo menos dois dos cinco países de Engelmann e Bandeira, com o desenho de controle de cada um.</p>',
)

# ---------- 09 · test
def q_of(x): return re.sub(r'<[^>]+>', '', re.search(r'<summary>(.*?)</summary>', x, re.S).group(1))
new_items = [
    item('A Corte Suprema chilena é autônoma. Isso mostra que ela protegeu direitos?', 'Não. A cooptação deu independência corporativa, mas a Corte usou o poder disciplinar contra juízes simpáticos a Allende e, depois de 1973, sustentou a estrutura institucional do regime em nome da própria independência. Autonomia, protagonismo e proteção de direitos são perguntas distintas.'),
    item('Os 74 ministros colombianos do estudo são da Corte Constitucional?', 'Não. São da Corte Suprema de Justicia. Desde 1991, o controle de constitucionalidade cabe à Corte Constitucional, que o estudo não cobre e cujos ministros o Senado escolhe a partir de listas do presidente, da Corte Suprema e do Conselho de Estado.'),
    item('O quadro dos 19 países descreve os tribunais como são em 2026?', 'Não necessariamente. Ele não indica ano-base; serve para comparar desenhos tal como apresentados. Afirmar a situação atual exigiria uma fonte datada.'),
]
c9 = chapter(9, 'Teste', 'Responda antes de abrir.') + '<div class="wide">\n<div class="quiz">' + ''.join(old_items + new_items) + '</div>\n</div>\n'

s = s[:i_c1] + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + s[i_end:]
open(P, 'w').write(s)
print('ok', len(old_items), 'old items')
