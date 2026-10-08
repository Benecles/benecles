# LAT-1 · Latam Aula 06 (Bolívia e OC-28): rebuild on the live page from the APPROVED blueprint (Claude, 05/10).
# Keeps ch. 01 text, the bet, the art. 256 lex, Fig. 1 (canonical p-us*), the dissent analysis and the old quiz;
# folds "O eixo, de novo" + "Aprofundamento" into the chapters (each fact once, F-021); fixes an attribution
# ("mientras el soberano así lo desee" is the petitioners' line, recorded in III.7.3, not the TCP's reasoning);
# adds the TCP's three moves, OC-28's restriction/sanction distinction, the four-step test, §§144–145;
# replaces the box-fork hero with a to-scale record of the four acts; ends on the eixo.
import re, sys
from datetime import date

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

# ---------- keep verbatim
i_c1 = s.index('<section class="chapter" aria-labelledby="c1"')
i_c2 = s.index('<section class="chapter" aria-labelledby="c2"')
c1_old = s[i_c1:i_c2]
bet = c1_old[c1_old.index('<div class="bet">'):].rstrip() if '<div class="bet">' in c1_old else ''
lex256 = re.search(r'<p class="lex[^"]*"><b>Constituição da Bolívia, art\. 256\.I</b>.*?</p>', c1_old, re.S).group(0)
first_paras = re.findall(r'<p>(A Constituição boliviana de 2009.*?)</p>|<p>(Em setembro de 2017.*?)</p>', c1_old, re.S)
para_rule = re.search(r'<p>A Constituição boliviana de 2009.*?</p>', c1_old, re.S).group(0)
para_action = re.search(r'<p>Em setembro de 2017.*?</p>', c1_old, re.S).group(0)
sc = s.index('<div class="scrolly">')
fig1 = s[sc:s.index('<section class="chapter"', sc)]
# the hidden defs svg for the map frame sits right before the scrolly
defs_i = s.rfind('<svg width="0" height="0"', 0, sc)
defs = s[defs_i:sc] if defs_i > i_c2 else ''
old_items = re.findall(r'<details>.*?</details>', s[s.index('<div class="quiz">'):], re.S)[:5]
i_end = s.index('<nav class="endnav"')
diss_pz = re.search(r'<p>L\. Patricio Pazmiño Freire.*?</p>', s, re.S).group(0)
diss_zf = re.search(r'<p>Eugenio Raúl Zaffaroni também.*?</p>', s, re.S).group(0)
diss_two = re.search(r'<p>A divergência entre os juízes, então.*?</p>', s, re.S).group(0)

# ---------- 01 · the rule the voters refused to change
c1 = chapter(1, 'A regra que o eleitor recusou mudar', 'A Constituição de 2009 permitia uma única reeleição consecutiva. Em 2016, o eleitorado recusou mudar isso.') + longform(
    para_rule, para_action, lex256,
    p('O art. 256 é a chave da estratégia: se a Convenção fosse “mais favorável” aos direitos políticos do que a Constituição, prevaleceria sobre ela. A pergunta, portanto, era a mesma de Gelman vista do avesso. Lá, uma decisão majoritária foi barrada pelos direitos das vítimas (<a href="aula-05.html">Aula 05</a>); aqui, um direito seria usado contra o resultado de uma votação.'),
) + bet + '\n'

# ---------- 02 · what the SCP actually did
c2 = chapter(2, 'O que a SCP 0084/2017 afastou', 'Duas operações no dispositivo, e nenhuma delas é anular o referendo.') + longform(
    p('Em 28 de novembro de 2017, a Sala Plena do Tribunal Constitucional Plurinacional (presidente e relator Macario Lahor Cortez Chávez) decidiu duas coisas diferentes. Primeiro, com base no art. 256, declarou a <strong>aplicação preferente</strong> do art. 23 da Convenção Americana, “por ser la norma más favorable en relación a los Derechos Políticos”, sobre as frases “por una sola vez de manera continua” dos arts. 156 e 168 e “de manera continua por una sola vez” dos arts. 285.II e 288 da Constituição. Segundo, declarou a <strong>inconstitucionalidade</strong> das mesmas expressões na Lei do Regime Eleitoral (Lei 026/2010).'),
    p('Os quatro artigos cobriam presidente e vice-presidente, governadores, assembleístas departamentais, prefeitos e vereadores. A Constituição não foi riscada nem reformada: suas frases deixaram de ser aplicadas porque o Tribunal considerou mais favorável a norma convencional. A lei, essa sim, teve as expressões declaradas inconstitucionais. Seis magistrados assinaram; um sétimo não assinou por não ter participado da sessão, o que não é voto vencido.'),
    p('O referendo de 21 de fevereiro de 2016 não era objeto da ação, e a sentença não o anulou nem disse que o “não” valia como “sim”. O que ela fez foi remover a barreira jurídica que o “não” havia mantido. O efeito prático foi o mesmo que a reforma rejeitada teria produzido, e o mais visível foi liberar uma nova candidatura de Evo Morales. Mas a decisão tratou de elegibilidade, não de vitória: quem vence continua sendo decidido nas urnas.'),
)

# ---------- 03 · the Bolivian reading of the right to be elected
c3 = chapter(3, 'A leitura boliviana do direito de ser eleito', 'Princípio contra regra, tratado contra Constituição, candidato contra candidato.') + longform(
    p('O Tribunal chegou ao dispositivo por três passos. O primeiro foi dentro da própria Constituição. Os arts. 156, 168, 285.II e 288 seriam <em>normas-regra</em>; os arts. 26 e 28, que reconhecem amplamente o direito de participar do poder político, nas vertentes de votar e de ser votado, seriam <em>normas-princípio</em>. Havendo “antinomia” entre elas, a regra que limita a reeleição cederia ao princípio que amplia a participação.'),
    p('O segundo passo trouxe o tratado. O art. 410.II da Constituição boliviana integra os tratados de direitos humanos ao bloco de constitucionalidade, e o art. 256 manda aplicar com preferência os que forem mais favoráveis. Somando a isso os princípios <em>pro homine</em> e de favorabilidade, o Tribunal leu o art. 23 da Convenção como mais generoso que a Constituição: o art. 23.1 garante votar e ser eleito, e o art. 23.2 diz que a lei pode regular esses direitos “exclusivamente” por idade, nacionalidade, residência, idioma, instrução, capacidade civil ou mental, ou condenação penal. Como o limite de mandatos não está na lista, seria uma restrição sem base.'),
    p('O terceiro passo foi a igualdade. Os autores da ação haviam sustentado que os limites eram discriminatórios e que não se pode restringir a participação “mientras el soberano así lo desee”, pois quem elege é o povo pelo voto. O Tribunal acolheu o núcleo do argumento: a frase “por una sola vez de manera continua” seria uma medida de exclusão de quem já exerceu o cargo após uma reeleição, frente a quem aspira a ele, sem justificativa objetiva e razoável.'),
    p('Aí está o paradoxo que o caso expõe. O vocabulário dos direitos políticos, invocado em nome do soberano, serviu para neutralizar o que o próprio soberano havia decidido no referendo. E a Convenção Americana, que em Gelman limitou a maioria para proteger vítimas, aqui foi usada para ampliar a posição de quem já governava.'),
)

# ---------- 04 · the 2021 advisory answer
c4 = chapter(4, 'A resposta consultiva de 2021', 'Consultada pela Colômbia, a Corte leu o mesmo art. 23 em sentido oposto.', 'dif') + longform(
    p('Em 21 de outubro de 2019, a Colômbia pediu à Corte Interamericana uma opinião consultiva: a reeleição presidencial indefinida é um direito humano protegido pela Convenção, e proibi-la é compatível com ela? A Corte respondeu em 7 de junho de 2021, por cinco votos a dois.'),
    lex('Corte IDH, OC-28/21, parte dispositiva', '2. La reelección presidencial indefinida no constituye un derecho autónomo protegido por la Convención Americana [...]. 3. La prohibición de la reelección indefinida es compatible con la Convención Americana [...] y la Carta Democrática Interamericana. 4. La habilitación de la reelección presidencial indefinida es contraria a los principios de una democracia representativa.', 'dif'),
    p('<strong>Primeiro, não há direito autônomo.</strong> O que a Convenção garante é ser eleito em eleições periódicas e autênticas; nenhum tratado reconhece um direito a ser reeleito para a Presidência. Os Estados escolhem seu sistema político e regulam a reeleição conforme sua história (§ 86), desde que dentro da Convenção.'),
    p('<strong>Segundo, a palavra “exclusivamente”.</strong> É aqui que a leitura boliviana se desfaz. A Corte distinguiu dois regimes. Quando o direito político é restringido por <em>sanção</em> a uma pessoa, como a destituição ou inabilitação de um eleito por autoridade administrativa, o “exclusivamente” vale à letra: só uma condenação penal por juiz competente pode fazê-lo (casos López Mendoza e Petro Urrego, § 107). Mas um sistema eleitoral precisa de <em>regras gerais</em> que vão muito além da lista do art. 23.2, e o parágrafo 2 não pode ser lido isolado do parágrafo 1. Por isso, “por el solo hecho de no estar incluida explícitamente en el artículo 23.2”, a limitação da reeleição não é contrária à Convenção (§ 112).'),
    p('<strong>Terceiro, o teste da restrição.</strong> Não estar na lista não basta para ser válida: a restrição precisa estar prevista em lei, perseguir fim legítimo e ser idônea, necessária e proporcional (§ 114). O fim é legítimo pelo art. 32 da Convenção: evitar que uma pessoa se perpetue no poder e assegurar pluralismo, alternância e freios entre os poderes (§ 119). É idônea, dada a concentração de poder na Presidência (§ 120), e a Corte não encontrou medida menos gravosa igualmente eficaz (§ 121). Na proporcionalidade, pesou dois direitos: o de quem ocupa o cargo, que não tem direito autônomo à reeleição e só perde a chance de concorrer de novo, e o dos demais cidadãos, cujo direito de votar não inclui opções ilimitadas de candidatos (§§ 123–125).'),
    p('<strong>Quarto, a maioria também tem limite aqui.</strong> A Corte afirmou que a eliminação dos limites “no debería ser susceptible de ser decidida por mayorías ni sus representantes para su propio beneficio” (§ 144), e que o maior perigo atual para as democracias da região não é a ruptura abrupta, mas a erosão gradual das salvaguardas, “incluso si este es electo mediante elecciones populares” (§ 145). A Corte também precisou o alcance: a opinião não restringe a reeleição presidencial em geral, mas a ausência de limitação razoável e os mecanismos que permitam a perpetuação de uma mesma pessoa na Presidência (§ 148).'),
    p('Esse quarto ponto responde à objeção da soberania. A Corte lembra que os Estados americanos consentiram, soberanamente, que o exercício efetivo da democracia é uma obrigação jurídica internacional (§ 147). Limitar a reeleição presidencial, nessa leitura, não é uma imposição externa contra o povo: é o cumprimento de um compromisso que o próprio Estado assumiu. E a razão de o limite recair sobre a Presidência é institucional: em sistemas presidenciais, como registrou a Comissão de Veneza citada pela Corte, o poder tende a concentrar-se no presidente, enquanto o Legislativo e o Judiciário são relativamente mais fracos (§ 121).'),
    p('Falta dizer o que a opinião não é. A Colômbia pediu uma interpretação em abstrato; a Corte não recebeu recurso contra o tribunal boliviano, não julgou a Bolívia em caso contencioso e não anulou a SCP 0084/2017 nem o resultado do referendo. A função consultiva fixa interpretação com autoridade de intérprete final da Convenção, que juízes e autoridades podem usar em controle de convencionalidade, mas não decide fatos, partes ou remédios de um litígio. Para a maioria, haver petições pendentes sobre tema próximo não impedia responder: interpretar em abstrato não é prejulgar aqueles casos.'),
)

# ---------- 05 · the dissents and the reach of each decision
c5 = chapter(5, 'O alcance dos votos e dos cargos', 'Dois dissensos que não dizem a mesma coisa, e dois dispositivos que não cobrem os mesmos cargos.') + longform(
    diss_pz, diss_zf, diss_two,
    h3('Até onde vai cada decisão'),
    p('A OC-28 responde sobre a <strong>reeleição presidencial indefinida</strong>. A SCP 0084/2017 afastou limites para quatro grupos de cargos, inclusive legislativos e subnacionais. Comparar os dois textos, portanto, não decide sozinho a validade de cada limite para prefeitos, vereadores ou assembleístas: para cada cargo, é preciso identificar a norma doméstica e o precedente pertinente. Do mesmo modo, a opinião não condena toda reeleição. Uma regra que permite uma reeleição consecutiva e proíbe a seguinte é exatamente o tipo de limitação razoável que ela considera compatível; quem disputa a única reeleição permitida não está no caso de quem busca um terceiro mandato seguido.'),
)

# ---------- 06 · three uses of the Convention (canonical Fig. 1)
c6 = chapter(6, 'Três usos da Convenção', 'O mesmo vocabulário, três direções.') + longform(
    p('Postas lado a lado, as três decisões mostram que “direitos humanos” não é um argumento que aponta sempre para o mesmo lado. Em cada uma, pergunte de quem é o direito invocado e contra quem ele é usado.'),
) + defs + fig1 + longform(
    p('Gelman e a OC-28 convergem num ponto que a SCP contrariou: há matérias que a maioria não decide sozinha. Em Gelman, a impunidade de graves violações (§ 239); na OC-28, a remoção dos limites à permanência no poder em benefício de quem o exerce (§ 144). O Tribunal boliviano fez o movimento inverso, usando um direito individual para desfazer, na prática, uma decisão majoritária que protegia a alternância.'),
)

# ---------- 07 · answer the eixo
c7 = chapter(7, 'Responder ao eixo com os casos', 'Tese, casos, divergência e posição.', 'dif') + longform(
    '<p class="eixo"><b>Eixo de discussão da aula</b>Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?</p>',
    '<ol><li><strong>Tese.</strong> A maioria tem limites, mas os limites não apontam todos para o mesmo lado.</li>'
    '<li><strong>Contraste.</strong> Corte IDH, Gelman (2011): o voto popular não legitima a impunidade de graves violações.</li>'
    '<li><strong>O caso boliviano.</strong> TCP, SCP 0084/2017: aplicação preferente do art. 23 sobre os limites constitucionais e inconstitucionalidade dos legais, por princípio contra regra, art. 256 e igualdade; sem anular o referendo.</li>'
    '<li><strong>A leitura interamericana.</strong> Corte IDH, OC-28/21 (5 × 2): não há direito autônomo à reeleição presidencial indefinida; o “exclusivamente” vale para sanções, não para regras gerais; a proibição passa no teste; e a remoção dos limites não deveria ser decidida por maiorias em benefício próprio. Opinião consultiva, não recurso.</li>'
    '<li><strong>Divergência.</strong> Pazmiño: admissibilidade, reformulação da consulta, igualdade eleitoral e pluralismo de modelos. Zaffaroni: competência para prescrever engenharia institucional e mandato sem eleição × candidatura reiterada.</li>'
    '<li><strong>Posição.</strong> Diga qual leitura do art. 23 você sustenta e por quê, separando o plano doméstico do interamericano.</li></ol>',
)

# ---------- 08 · test
new_items = [
    item('Por que a ausência da reeleição na lista do art. 23.2 não torna o limite inválido, segundo a OC-28?', 'Porque o “exclusivamente” se aplica às restrições por sanção individual (só por condenação penal de juiz competente, como em López Mendoza e Petro), não às regras gerais que todo sistema eleitoral precisa. O art. 23.2 não pode ser lido isolado do 23.1 (§§ 107–112). A restrição ainda precisa passar no teste de legalidade, fim legítimo, idoneidade, necessidade e proporcionalidade.'),
    item('A OC-28 proíbe que um prefeito boliviano dispute a reeleição, ou que um presidente dispute a única reeleição permitida?', 'Não decide nenhum dos dois. Ela responde sobre a reeleição presidencial indefinida; não transporta automaticamente a conclusão a cargos locais, e uma regra que permite uma reeleição e veda a seguinte é o tipo de limitação razoável que considera compatível.'),
    item('Eixo: um tribunal invoca o direito de ser eleito para afastar um limite de mandatos que o eleitorado se recusou a mudar. Responda com os casos.', 'Comece pelo contraste com Gelman (a maioria não legitima a impunidade). Descreva a SCP 0084/2017 com precisão (aplicação preferente e inconstitucionalidade; referendo não anulado; princípio × regra, art. 256, igualdade). Oponha a OC-28/21: não há direito autônomo, o limite passa no teste, e a remoção dos limites não deveria ser decidida por maiorias em benefício próprio (§ 144), lembrando que é consultiva. Registre Pazmiño e Zaffaroni separadamente. Conclua com sua leitura do art. 23.'),
]
c8 = chapter(8, 'Teste', 'Responda antes de abrir.') + '<div class="wide">\n<div class="quiz">' + ''.join(old_items + new_items) + '</div>\n</div>\n'

s = s[:i_c1] + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + s[i_end:]

# ---------- hero: a to-scale record of the four acts (replaces the box fork)
D0, D1 = date(2016, 2, 21), date(2021, 6, 7); X0, X1 = 90, 990
def x(d): return round(X0 + (d - D0).days / (D1 - D0).days * (X1 - X0), 1)
mono = 'font:12px var(--mono);letter-spacing:1px'
o = f'<text x="60" y="26" style="{mono};fill:var(--muted)">O VOTO, A SENTENÇA E A CONSULTA</text>'
o += f'<path class="draw" d="M{X0} 70H{X1}" style="fill:none;stroke:var(--ink);stroke-width:3"/>'
for y in range(2017, 2022):
    xx = x(date(y, 1, 1))
    o += f'<path d="M{xx} 64V76" style="stroke:var(--ink);stroke-width:1.4"/><text x="{xx}" y="54" text-anchor="middle" style="{mono};fill:var(--muted)">{y}</text>'
ev = [(D0, 'ink', 'REFERENDO · 2016', 'não à reforma', 'start'),
      (date(2017, 11, 28), 'conc', 'SCP 0084 · 2017', 'limite afastado', 'start'),
      (date(2019, 10, 21), 'dif', 'CONSULTA · 2019', 'pedido da Colômbia', 'end'),
      (D1, 'dif', 'OC-28 · 2021', 'limite compatível', 'end')]
for i, (d, tone, name, sub, anc) in enumerate(ev):
    xx = x(d); col = f'var(--{tone})'
    o += (f'<g class="pop" style="--d:{.3 + i * .3:.1f}s;{mono}"><circle cx="{xx}" cy="70" r="8" style="fill:{col}"/>'
          f'<text x="{xx}" y="102" text-anchor="{anc}" style="fill:{col};font-weight:600">{name}</text>'
          f'<text x="{xx}" y="124" text-anchor="{anc}" style="fill:var(--ink-2)">{sub}</text></g>')
o += (f'<path d="M{X0} 146H{x(date(2017, 11, 28))}" style="stroke:var(--conc);stroke-width:1.4"/>'
      f'<text x="{X0}" y="164" style="{mono};fill:var(--conc)">BOLÍVIA</text>'
      f'<path d="M{x(date(2019, 10, 21))} 146H{X1}" style="stroke:var(--dif);stroke-width:1.4"/>'
      f'<text x="{X1}" y="164" text-anchor="end" style="{mono};fill:var(--dif)">SISTEMA INTERAMERICANO · CONSULTIVO</text>')
hero = f'<svg class="hero-fork" viewBox="0 0 1080 172" aria-hidden="true">{o}</svg>'
s, n = re.subn(r'<svg[^>]*class="hero-fork[^"]*".*?</svg>', lambda m: hero, s, count=1, flags=re.S)
assert n == 1
open(P, 'w').write(s)
print('ok')
