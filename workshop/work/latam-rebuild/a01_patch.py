# LAT-1 · Latam Aula 01 (Constitucionalismo latino-americano): rebuild on the live page from the APPROVED blueprint
# (Claude, 05/10). Keeps the hero map, Haiti, the long-duration method, Figs. 1–3 (canonical), social constitutionalism
# and the quiz core; cuts the course catalogue from §00, the Engelmann comparison (Aula 02's), the fictional assembly
# minicase and the forward roadmap in Fig. 3's last card; folds "Aprofundamento" into the chapters it repeated
# (F-021); gives Cádiz its own chapter (arts. 1º, 3º, 22, 23, the paradox, the municipal question, Peru) and the
# recepções their own (Peru 1823, Argentina 1813–1853, Brasil 1824); removes the unsourced Gargarella attribution;
# ends with a historical exercise on dated episodes.
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
def lex(label, text, tone=''): return f'<p class="lex {tone}"><b>{label}</b>{text}</p>'
def item(q, a): return f'<details><summary>{q}</summary><p>{a}</p></details>'
def grab(pat):
    m = re.search(pat, s, re.S); assert m, pat[:40]; return m.group(0)

# ---------- pieces kept verbatim from the live page
i_c0 = s.index('<section class="chapter" aria-labelledby="c0"')
i_end = s.index('<nav class="endnav"')
scrolls = [m.start() for m in re.finditer(r'<div class="scrolly">', s)]
def scrolly(k):
    a = scrolls[k]
    return s[a:s.index('<section class="chapter"', a)] if k < 2 else s[a:s.index('<section class="chapter"', a)]
fig1_full = scrolly(0)           # Fig. 1 scrolly; the bet follows it inside the same span
bet_i = fig1_full.find('<div class="bet">')
fig1, bet = (fig1_full[:bet_i], fig1_full[bet_i:]) if bet_i > 0 else (fig1_full, '')
fig2 = scrolly(1)
fig3 = scrolly(2)
# hidden map defs (if any) between chapters: keep them wherever they were, right before Fig. 1
defs = ''.join(re.findall(r'<svg width="0" height="0"[^>]*>.*?</svg>', s[i_c0:i_end], re.S))
assert defs.count('<svg') == 2, defs.count('<svg')
p_method = [grab(r'<p>O ponto de partida é uma escolha de método:.*?</p>'),
            grab(r'<p>A hipótese que guia a aula vem de Waldo Ansaldi.*?</p>'),
            grab(r'<p>As palavras que atravessam a aula são as da Modernidade.*?</p>')]
p_haiti = [grab(r'<p>A história costuma começar pelas repúblicas hispano-americanas\..*?</p>'),
           grab(r'<p>O significado constitucional é duplo\..*?</p>')]
p_social = [grab(r'<p>No fim do século XIX, o constitucionalismo liberal.*?</p>'),
            grab(r'<p>A América Latina participou cedo dessa virada\..*?</p>')]
p_redemo = grab(r'<p>Depois das ditaduras da segunda metade do século, a pergunta ganhou urgência\..*?</p>')
p_danger = grab(r'<p>A comparação funciona melhor quando se pergunta qual perigo cada projeto tenta evitar\..*?</p>')
p_concess = grab(r'<p>Essa última combinação troca concessões nos dois sentidos\..*?</p>')
p_brasil = grab(r'<p>O caso brasileiro torna a combinação mais concreta\..*?</p>')
p_trap = grab(r'<p><strong>Armadilha de classificação\.</strong>.*?</p>')
p_three = grab(r'<p>A mudança do texto altera a pergunta institucional:.*?</p>')
old_items = re.findall(r'<details>.*?</details>', s[s.index('<div class="quiz">'):i_end], re.S)

# small edits inside kept pieces
p_method[1] = p_method[1].replace('A hipótese que guia a aula vem de', 'A hipótese de leitura vem de')
p_method[2] = p_method[2].replace('As palavras que atravessam a aula são', 'As palavras que atravessam essa história são')
p_haiti[0] = p_haiti[0].replace('A aula começa antes, em Saint-Domingue.', 'Ela começa antes, em Saint-Domingue.')
p_danger = p_danger.replace(' Em uma questão de prova, nomear apenas “liberal” ou “republicano” não basta: a resposta precisa apontar a regra de distribuição do poder e o direito ou risco que ela privilegia.',
                            ' Por isso, nomear “liberal” ou “republicano” não basta: é preciso apontar a regra de distribuição do poder e o direito ou o risco que ela privilegia.')
p_trap = p_trap.replace('<strong>Armadilha de classificação.</strong> ', '')

# ---------- figure cards: Cádiz and Brasil now have chapters of their own, so the cards keep only the map's claim;
# Fig. 3's last card stops listing future lessons
fig1 = set_step(fig1, 'p-cr2', h3='Cádiz atravessa o Atlântico', paras=['Em 19 de março de 1812, as Cortes reunidas em Cádiz promulgam uma Constituição para a Nação “de ambos os hemisferios”. O texto atravessa o Atlântico e é apropriado: em Lima, a primeira Constituição republicana do Peru, de 1823, carrega sua marca.'])
fig1 = set_step(fig1, 'p-cr3', paras=['A Corte portuguesa chega ao Rio em 1808, Cádiz chega a ser jurada no Brasil em 1821, e a independência de 1822 preserva a dinastia. O caminho brasileiro passa pela crise, mas termina numa monarquia constitucional.'])
fig3 = set_step(fig3, 'p-st3', paras=['Visto em corte, o método fica visível. A desigualdade da matriz colonial, o Executivo forte do pacto e os direitos generosos atravessam todas as camadas e afloram na superfície de hoje. Quando uma corte latino-americana decide, decide em cima dessas três veias.'])

# ---------- 00 · the three questions
c0 = chapter(0, 'Direitos, poder e cidadania', 'Três perguntas atravessam a história constitucional da região.') + longform(
    p('Toda Constituição responde, explícita ou implicitamente, a três perguntas: quem integra o povo soberano, onde o poder fica concentrado e quem pode exigir o que o texto promete. Na América Latina, as respostas mudaram muitas vezes, mas raramente começaram do zero.'),
    p('Em 1805, o Haiti fundou uma Constituição na ruptura com a escravidão. Em 1812, Cádiz declarou uma Nação de ambos os hemisférios e, no mesmo texto, condicionou a cidadania de quem tinha origem africana. Em 1824, o Brasil independente reconheceu direitos e concentrou o poder no imperador. Ler esses textos com as três perguntas em mente é o que permite reconhecer, nas Constituições e nas cortes de hoje, o que é novo e o que é herança.'),
)
c1 = chapter(1, 'Ler o passado que permanece', 'Continuidade não quer dizer que nada mudou.') + longform(*p_method)
c2 = chapter(2, 'Haiti: liberdade contra a escravidão', 'A primeira experiência constitucional latino-americana foi feita por pessoas escravizadas.') + longform(*p_haiti)

# ---------- 03 · 1808 and the American constitutions before Cádiz
c3 = chapter(3, 'Da crise de 1808 às constituições americanas', 'A invasão napoleônica abre um vazio de autoridade, e a América responde antes de Cádiz.') + fig1 + longform(
    p('A ordem das datas desfaz um equívoco comum, o de tratar Cádiz como o ponto zero do constitucionalismo americano. Socorro escreve sua ata constitucional em 1810; Cundinamarca, Venezuela, Tunja e as Províncias Unidas da Nova Granada têm textos em 1811; a Constituição de Cádiz é promulgada em março de 1812, no mesmo ano de Antioquia e Cartagena; Apatzingán, no México, vem em 1814. E o Haiti tinha Constituições desde 1801. Cádiz foi decisiva, mas entrou num continente que já escrevia Constituições.'),
)

# ---------- 04 · Cádiz
c4 = chapter(4, 'Cádiz: Nação ampla, cidadania condicionada', 'O mesmo texto que inclui também seleciona.') + longform(
    p('A própria convocação já era uma mudança. Diante do vazio, as Cortes deixaram de ser uma instituição que aconselhava o rei ou votava questões do reino e passaram a se apresentar como representantes da Nação, com poder de elaborar uma Constituição.'),
    p('Promulgada em 19 de março de 1812, a Constituição Política da Monarquia Espanhola pretendia constitucionalizar uma monarquia transatlântica: soberania nacional, monarquia constitucional, representação política, Cortes eleitas, separação de poderes, cidadania, direitos e limitação do poder real.'),
    lex('Constituição de Cádiz, arts. 1º e 3º', 'Art. 1º La Nación española es la reunión de todos los españoles de ambos hemisferios. Art. 3º La soberanía reside esencialmente en la Nación.'),
    p('A inclusão é real. Indígenas americanos são reconhecidos como cidadãos; os americanos passam a integrar formalmente a Nação; desaparece, no plano constitucional, a distinção política entre espanhóis peninsulares e americanos; e a cidadania se torna o fundamento da participação.'),
    lex('Constituição de Cádiz, art. 22', 'A los españoles que por qualquiera línea son habidos y reputados por originarios del África les queda abierta la puerta de la virtud y del merecimiento para ser Ciudadanos [...].', 'conc'),
    p('A exclusão está no mesmo texto. Pelo art. 22, as pessoas tidas como de origem africana são espanholas, com direitos civis, mas sem cidadania: só as Cortes poderiam conceder a “carta de ciudadano”, e apenas a quem prestasse serviços qualificados à pátria ou se distinguisse por talento e conduta, fosse filho de legítimo matrimônio de pais livres, casado com mulher livre, domiciliado nos domínios espanhóis e exercesse profissão ou ofício. O art. 23 mostra o que isso custava na prática: “Sólo los que sean Ciudadanos podrán obtener empleos municipales y elegir para ellos”. Cádiz universaliza a cidadania dentro de limites, e esses limites são profundamente marcados pela raça.'),
    p('Há um segundo paradoxo, este institucional. Cádiz rompe com o absolutismo: o rei deixa de ser a fonte do poder, a soberania passa à Nação, o poder se submete à Constituição. Mas quer preservar a monarquia e a unidade de um império dos dois lados do oceano. A tensão de fundo era se se tratava de constitucionalizar a monarquia ou de constituir novos Estados, e as independências resolveriam essa tensão contra Madri.'),
    h3('A revolução por baixo: o município'),
    p('A mudança mais duradoura talvez tenha sido local. Cádiz reorganizou o território em províncias, chefes políticos e <em>ayuntamientos</em> constitucionais com autoridades eleitas. O município deixou de ser só estrutura administrativa e virou espaço de representação, de eleição, de exercício da cidadania e de disputa pelo poder. No vice-reinado do Peru, estudos recentes, como o de Silvia Escanilla Huerta, mostram setores indígenas usando essas ferramentas gaditanas para afirmar formas de autogoverno, inclusive depois da revogação da Constituição.'),
) + bet + '\n'

# ---------- 05 · three receptions
c5 = chapter(5, 'Peru, Argentina e Brasil: recepções diferentes', 'Cádiz circulou, e cada lugar ficou com uma parte dela.') + longform(
    p('A recepção de Cádiz não foi passiva. Setores americanos contestavam a manutenção do vínculo colonial, a autoridade das Cortes, a forma da representação americana e as desigualdades entre peninsulares e americanos. O texto foi, ao mesmo tempo, apropriado e contestado, e o que cada país aproveitou dependeu do desenho de poder que venceu ali.'),
    p('<strong>Peru, 1823.</strong> A primeira Constituição republicana peruana, feita no calor da independência, é a que mais carrega a marca gaditana: soberania, representação, cidadania, separação de poderes e organização territorial. A marca mais nítida está nas municipalidades e na ideia de que o poder deve ser legitimado pelo sufrágio. Cádiz funcionou ali como ponte entre o reformismo imperial e o constitucionalismo republicano.'),
    p('<strong>Argentina, de 1813 a 1853.</strong> A Constituição de Cádiz nunca vigorou no Rio da Prata, mas deixou rastros na Assembleia de 1813, no Estatuto de 1815, no Regulamento Provisório de 1817 e nas Constituições de 1819 e 1826. A Constituição de 1853 seguiu outro modelo, o norte-americano, com federalismo, presidencialismo e divisão territorial do poder, e ainda assim conservou elementos da matriz hispânica e gaditana.'),
    p('<strong>Brasil, 1824.</strong> Aqui a crise de 1808 produziu continuidade, não ruptura: a Corte se instala no Rio, o Brasil vira Reino Unido em 1815, a Revolução do Porto de 1820 pressiona a monarquia, e em 1821 a Constituição de Cádiz chega a ser jurada no Brasil antes do retorno de D. João VI. A independência de 1822 preservou a dinastia, e a Constituição de 1824 escolheu monarquia constitucional, Executivo forte, Poder Moderador, Senado vitalício, centralização e unidade territorial. Cádiz fez parte da experiência brasileira, não do seu desenho final.'),
)

# ---------- 06 · three projects (canonical Fig. 2) and the liberal-conservative settlement
c6 = chapter(6, 'Três projetos e o acordo liberal-conservador', 'O século XIX discutiu duas ideias e acabou escolhendo uma combinação.') + longform(
    p('As guerras de independência queriam romper o poder político europeu no continente, e o fizeram num quadro de crise econômica, desordem política e injustiça social. Era nesse quadro que se escreviam as primeiras Constituições republicanas.'),
    p('O primeiro constitucionalismo, entre 1810 e 1850, pode ser organizado a partir de dois ideais em disputa: a autonomia individual e o autogoverno coletivo. Três projetos constituintes fundacionais responderam a eles de modos diferentes. São lentes para comparar argumentos, não partidos estáveis nem rótulos que descrevam um país inteiro: um mesmo texto pode combinar elementos de mais de um projeto.'),
) + fig2 + longform(p_danger, p_concess, p_brasil, p_trap)

# ---------- 07 · social constitutionalism
c7 = chapter(7, 'Direitos sociais e deveres de atuação', 'Quando a Constituição passa a exigir, alguém precisa cobrar.') + longform(
    *p_social,
    p('Cada experiência traduziu a virada à sua maneira. A Constituição brasileira de 1934 trouxe direitos sociais e trabalhistas, educação e um título sobre a ordem econômica e social. A reforma colombiana de 1936, que emendou a Carta de 1886, afirmou a função social da propriedade e a intervenção do Estado na economia. A Constituição boliviana de 1938 constitucionalizou direitos sociais, a função social da propriedade e a proteção do trabalho. Com isso, a Constituição passou a conter normas sobre trabalho, educação, saúde, propriedade, ordem econômica e intervenção estatal, e a exigir mecanismos mais sofisticados de controle de constitucionalidade.'),
    p_three,
    p('Um exemplo simples mostra a diferença. Uma Constituição que passa a reconhecer o direito à educação muda o parâmetro jurídico, mas não constrói escolas. Se uma corte ordena alguma medida, ainda é preciso perguntar que omissão foi demonstrada, que remédio foi adotado e como as competências dos demais poderes foram respeitadas.'),
)

# ---------- 08 · rebuilding democracy, and what persists (canonical Fig. 3)
c8 = chapter(8, 'Reconstrução democrática e continuidade', 'As novas garantias nasceram sobre camadas que não desapareceram.') + longform(
    p_redemo,
    p('O instrumental que se espalhou pela região, já desde o pós-guerra, tem nomes concretos: tribunais constitucionais, cortes supremas com jurisdição constitucional, ações de inconstitucionalidade, proteção judicial dos direitos fundamentais e controle dos atos dos poderes públicos. A constitucionalização dos direitos mudou também o papel dos juízes.'),
    p('Os desafios que essa reconstrução enfrentava estavam todos ligados às três perguntas do início: como impedir a repetição do autoritarismo e limitar de fato o poder da maioria e do Executivo; como proteger direitos fundamentais e enfrentar os legados das ditaduras; como garantir independência judicial e controlar a constitucionalidade das leis e dos atos do poder público.'),
) + fig3 + longform(
    '<p class="eixo"><b>A pergunta que segue</b>Se o constitucionalismo latino-americano sempre combinou direitos amplos com Executivos fortes, o que muda quando as cortes passam a ser chamadas a garantir esses direitos?</p>',
    p('A <a href="aula-02.html">Aula 02</a> responde com dados: quem são os juízes das cortes supremas, como chegam lá e por que algumas cortes ganharam autonomia e outras não.'),
)

# ---------- 09 · apply the history
c9 = chapter(9, 'Aplicar a história', 'Uma resposta histórica se sustenta com episódios datados.', 'dif') + longform(
    '<p class="eixo"><b>Exercício</b>Como a história constitucional latino-americana ajuda a explicar por que a reconstrução democrática ampliou direitos e fortaleceu mecanismos de garantia sem eliminar continuidades de exclusão e de concentração de poder? Responda com dois episódios datados.</p>',
    '<ol><li><strong>Tese.</strong> Uma frase que diga o que mudou e o que permaneceu.</li>'
    '<li><strong>Primeiro episódio.</strong> Haiti 1805 ou Cádiz 1812: o texto, a escolha sobre quem é cidadão (por exemplo, o art. 22) e a razão dela.</li>'
    '<li><strong>Segundo episódio.</strong> Brasil 1824 ou México 1917: a escolha sobre o poder ou sobre os deveres do Estado, e por que foi feita.</li>'
    '<li><strong>Nexo.</strong> Ligue os dois aos desafios da redemocratização: Executivo forte, direitos a garantir, desigualdade de base.</li>'
    '<li><strong>Distinção.</strong> Separe o direito escrito, a via para exigi-lo e a sua realização.</li></ol>',
)

# ---------- 10 · test: the old core kept, T1 and T3 added, one Cádiz item (the bet already tests art. 22)
old = {re.sub(r'<[^>]+>', '', re.search(r'<summary>(.*?)</summary>', x, re.S).group(1)): x for x in old_items}
keep = [x for q, x in old.items() if 'paradoxo de Cádiz' not in q]
new_items = [
    item('Cádiz é o ponto de partida do constitucionalismo americano?', 'Não. Haiti tinha Constituições desde 1801; Socorro (1810) e Cundinamarca, Venezuela, Tunja e as Províncias Unidas (1811) escreveram textos antes de Cádiz (março de 1812). Cádiz foi decisiva pela circulação, não pela anterioridade.'),
    item('Qual o “paradoxo de Cádiz”?', 'Rompe com o absolutismo (soberania da Nação, poder submetido à Constituição, representação) mas quer preservar a monarquia e a unidade do império: constitucionalizar a monarquia ou constituir novos Estados?'),
    item('Uma Constituição reconhece direitos individuais amplos e concentra competências no Executivo. Como classificá-la, e por quê?', 'Como liberal-conservadora: os direitos são a concessão dos conservadores, o Executivo concentrado é a dos liberais, contra o temor de maiorias “irracionais”. A presença de um elemento liberal não a torna liberal pura.'),
]
c10 = chapter(10, 'Teste', 'Responda antes de abrir.') + '<div class="wide">\n<div class="quiz">' + ''.join(keep + new_items) + '</div>\n</div>\n'

s = s[:i_c0] + defs + '\n' + c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + s[i_end:]
open(P, 'w').write(s)
print('ok', len(keep), 'old items kept')
