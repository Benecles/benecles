from common import *
from maps import latam_map, map_defs, flow

hero = ('<g class="pop" style="--d:.1s"><rect x="40" y="62" width="250" height="46" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
        '<text x="165" y="90" text-anchor="middle" style="font:600 13px var(--mono);letter-spacing:1px;fill:var(--ink)">CONVENÇÃO, ART. 23</text></g>'
        '<path class="draw" d="M290 85C430 85 470 40 640 40" style="fill:none;stroke:var(--conc);stroke-width:3"/>'
        '<path class="draw" d="M290 85C430 85 470 130 640 130" style="fill:none;stroke:var(--dif);stroke-width:3;--d:.5s"/>'
        '<g class="pop" style="--d:1s;font:12px var(--mono);letter-spacing:1px">'
        '<text x="652" y="36" style="fill:var(--conc)">TCP DA BOLÍVIA · 2017</text>'
        '<text x="652" y="54" style="fill:var(--ink-2)">o limite à reeleição viola o direito de ser eleito</text>'
        '<text x="652" y="126" style="fill:var(--dif)">CORTE IDH · OC-28 · 2021</text>'
        '<text x="652" y="144" style="fill:var(--ink-2)">reeleição indefinida não é direito humano</text></g>')

# ---- Fig: who invoked the Convention, against what
ROWS = [('GELMAN · 2011', 'Corte IDH', 'contra uma lei confirmada', 'pelo voto popular', 'protege as vítimas', 'conc'),
        ('SCP 0084 · 2017', 'TCP da Bolívia', 'contra a própria Constituição', '(e o "não" de 2016)', 'amplia o direito de quem governa', 'conc'),
        ('OC-28 · 2021', 'Corte IDH', 'a favor dos limites', 'constitucionais', 'protege a alternância', 'dif')]
SJ, MVD, SUC, BOG = (-84.08, 9.93), (-56.2, -34.9), (-65.26, -19.05), (-74.07, 4.71)
SJPIN = (SJ[0], SJ[1], 'San José · Corte IDH', 'end', -30, 44)
def uses(k):
    if k == 0:
        o = latam_map({'URY': 'conc', 'CRI': 'dif'}, [], skip_seas=('OCEANO PACÍFICO', 'OCEANO ATLÂNTICO'), pins=[(MVD[0], MVD[1], 'Montevideo', 'start', 44, 26), SJPIN],
                      title='GELMAN · 2011', extra=flow(MVD, SJ, 'o caso vai a San José', bend=-.28, tone='conc', dy=-8))
    elif k == 1:
        o = latam_map({'BOL': 'conc'}, ['BOL'], skip_seas=('OCEANO PACÍFICO',), pins=[(SUC[0], SUC[1], 'Sucre · TCP', 'start', 12, 18), SJPIN],
                      title='SCP 0084 · 2017', note='a Convenção aplicada em casa, contra a Constituição')
    else:
        o = latam_map({'COL': 'dif', 'CRI': 'dif', 'BOL': 'grey'}, [], skip_seas=('OCEANO PACÍFICO',), pins=[(BOG[0], BOG[1], 'Bogotá', 'start', 10, 16), SJPIN],
                      title='OC-28 · 2021', extra=flow(BOG, SJ, 'consulta · 2019', bend=.35, tone='dif', dy=-10))
    a, who, v1, v2, why, tone = ROWS[k]
    o += G(T(24, 404, who.upper(), 't-small', style='letter-spacing:.08em') + T(24, 424, v1, 't-small') + T(24, 440, v2, 't-small')
           + T(24, 460, why, 't-small tc-' + tone), 'fade', d=.3)
    return o

b = map_defs()
b += chapter('01', 'c1', 'A Bolívia e o limite à reeleição', 'A Constituição de 2009 permitia uma única reeleição consecutiva. Em 2016, o eleitorado recusou mudar isso.', 'dif')
b += longform(
    '<p>A Constituição boliviana de 2009 fixa o mandato do presidente e do vice-presidente em cinco anos, com possibilidade de reeleição "por una sola vez de manera continua" (arts. 156 e 168), e aplica a mesma regra a governadores, assembleístas e autoridades municipais (arts. 285.II e 288). Em 21 de fevereiro de 2016, um referendo sobre a reforma que permitiria uma nova candidatura de Evo Morales terminou com a vitória do "não".</p>',
    '<p>Em setembro de 2017, uma senadora e onze deputados da Assembleia Legislativa Plurinacional propuseram uma <strong>ação de inconstitucionalidade abstrata</strong> com dois pedidos. Primeiro, a inconstitucionalidade dos dispositivos da Lei do Regime Eleitoral (Lei 026/2010) que reproduziam o limite. Segundo, e mais ousado, a <strong>inaplicabilidade</strong> dos próprios artigos da Constituição que o estabelecem, por "contradição intraconstitucional" com os arts. 26 e 28 (direitos políticos) e por contrariarem os arts. 1.1, 23, 24 e 29 da Convenção Americana.</p>',
    lex('Constituição da Bolívia, art. 256.I', 'Los tratados e instrumentos internacionales en materia de derechos humanos que hayan sido firmados, ratificados o a los que se hubiera adherido el Estado, que declaren derechos más favorables a los contenidos en la Constitución, se aplicarán de manera preferente sobre ésta.'),
    '<p>O art. 256 é a chave da estratégia: se a Convenção fosse "mais favorável" aos direitos políticos do que a Constituição, prevaleceria sobre ela.</p>')

b += bet('A Constituição permite uma única reeleição consecutiva. Esse limite viola o direito de ser eleito garantido pela Convenção Americana?', [
    ('Sim: a Convenção só admite restrições por idade, nacionalidade, residência e motivos parecidos.', 'TCP da Bolívia (2017)'),
    ('Não: reeleição indefinida não é direito humano, e o limite protege a alternância no poder.', '*Corte IDH, OC-28 (2021)'),
], '<p>As duas respostas foram dadas por tribunais. O TCP boliviano ficou com a primeira em 2017; a Corte Interamericana, com a segunda em 2021. A segunda é hoje a leitura da própria Corte Interamericana, intérprete final da Convenção; como é consultiva, não anulou a sentença boliviana, mas orienta os juízes que fazem controle de convencionalidade.</p>')
b += chapter('02', 'c2', 'A SCP 0084/2017', 'O Tribunal Constitucional Plurinacional aplicou a Convenção por cima da Constituição.')
b += longform(
    '<p>Em 28 de novembro de 2017 (relator Macario Lahor Cortez Chávez), a Sala Plena declarou a <strong>aplicação preferente do art. 23 da Convenção Americana</strong>, "por ser la norma más favorable en relación a los Derechos Políticos", sobre as expressões "por una sola vez de manera continua" dos arts. 156, 168, 285.II e 288 da Constituição, e a inconstitucionalidade das expressões equivalentes da lei eleitoral.</p>',
    '<p>O raciocínio parte do art. 23 da Convenção, que garante o direito de votar e ser eleito, e da lista fechada de motivos pelos quais a lei pode regulá-lo (idade, nacionalidade, residência, idioma, instrução, capacidade civil ou mental, condenação penal). Como o limite à reeleição não está nessa lista, restringiria sem justificativa o direito de ser eleito. O Tribunal acrescenta um argumento democrático: quem escolhe é o soberano pelo voto; se confia nos candidatos, eles vencerão, e não se pode limitar a possibilidade de ser eleito "mientras el soberano así lo desee".</p>',
    '<p>O paradoxo é o que a aula de 31/08 quer que você veja. O mesmo vocabulário dos direitos políticos, usado pelo Tribunal, abriu caminho para a candidatura que a maioria havia recusado no referendo de 2016. A sentença não anulou o referendo, que nem era o objeto da ação: afastou as regras constitucionais e legais que limitavam a reeleição, e o efeito prático foi o mesmo que o “sim” teria produzido. E a Convenção Americana, que em Gelman limitou a maioria para proteger vítimas, aqui foi usada para ampliar o direito de quem já governa.</p>')

b += chapter('03', 'c3', 'A resposta da Corte Interamericana: OC-28/21', 'Consultada pela Colômbia, a Corte disse que reeleição indefinida não é direito humano.', 'dif')
b += longform(
    '<p>Em 21 de outubro de 2019, a Colômbia pediu uma <strong>opinião consultiva</strong> sobre a reeleição presidencial indefinida no sistema interamericano. A Corte a emitiu em <strong>7 de junho de 2021</strong>, por cinco votos a dois.</p>',
    lex('Corte IDH, OC-28/21, parte dispositiva', '2. La reelección presidencial indefinida no constituye un derecho autónomo protegido por la Convención Americana [...]. 3. La prohibición de la reelección indefinida es compatible con la Convención Americana [...] y la Carta Democrática Interamericana. 4. La habilitación de la reelección presidencial indefinida es contraria a los principios de una democracia representativa.'),
    '<p>A Corte trata a possibilidade de concorrer a um novo mandato como uma <strong>modalidade</strong> do direito de ser eleito, que cada Estado regula conforme sua história, e não como um direito autônomo. A proibição persegue uma finalidade legítima: impedir que uma pessoa se perpetue no poder, o que ameaça a representação e aproxima o governo de uma autocracia, "incluso existiendo elecciones periódicas". A democracia representativa exige <strong>pluralismo e alternância</strong>: que um projeto de governo possa ser substituído por outro.</p>',
    '<p>Os juízes Patricio Pazmiño Freire e Eugenio Raúl Zaffaroni divergiram, e ambos contestaram a própria competência da Corte para emitir a opinião. Zaffaroni argumenta que a consulta estava ligada a fatos concretos, em especial os da Bolívia, que poderiam chegar à Corte como casos contenciosos, e que uma opinião consultiva não deveria antecipar esse julgamento.</p>')
b += scrolly('Três usos da Convenção', [(f'p-us{k}', uses(k), ROWS[k][0]) for k in range(3)], [
    S('p-us0', 'Gelman', 'A Convenção contra a maioria, a favor das vítimas', '<p>Em Gelman, a Corte IDH usou a Convenção para afirmar que uma decisão majoritária (a Lei de Caducidade, confirmada em referendo e plebiscito) não pode impedir a investigação de graves violações. O limite protege as vítimas.</p>', 'conc'),
    S('p-us1', 'Bolívia', 'A Convenção contra a Constituição', '<p>O TCP declarou a aplicação preferente do art. 23 da Convenção sobre as frases “por una sola vez de manera continua” da Constituição e declarou inconstitucionais as mesmas frases da Lei do Regime Eleitoral. O referendo de 2016 não foi anulado, mas perdeu efeito prático: a candidatura que ele recusara ficou liberada. O "direito" protegido era o de quem ocupava o poder de concorrer outra vez.</p>', 'conc'),
    S('p-us2', 'OC-28', 'A Convenção a favor dos limites', '<p>Em 2021, respondendo a uma consulta da Colômbia, a Corte IDH disse que a Convenção não garante reeleição presidencial indefinida, e que proibi-la é compatível com ela. A opinião consultiva não revisa nem anula a sentença boliviana; mas, lidas lado a lado, as duas decisões interpretam o mesmo art. 23 em sentidos opostos. Aqui a Convenção protege a alternância e, com ela, os direitos políticos de todos os demais.</p>', 'dif'),
])

b += chapter('04', 'c4', 'O eixo da aula, de novo', 'Quais são os limites da soberania popular?')
b += longform(
    eixo('Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?'),
    '<p>Juntando as Aulas 05 e 06, a resposta ganha duas faces. Em Gelman, a soberania popular encontra um limite nos direitos das vítimas: a maioria não pode decidir que graves violações fiquem impunes. Na Bolívia, o risco é o inverso: um tribunal invoca direitos e a própria "vontade do soberano" para neutralizar, na prática, o que a maioria decidiu no voto e para enfraquecer uma garantia da democracia, a alternância. A OC-28 mostra que o sistema interamericano também protege as regras que impedem a perpetuação no poder.</p>',
    '<p>Uma boa resposta escrita distingue os dois movimentos e não trata "direitos humanos" como argumento que sempre aponta na mesma direção. Pergunte, em cada caso, de quem é o direito invocado e contra quem ele é usado.</p>')

b += deep_chapter('06', '05', ())
b += chapter('06', 'c6', 'Teste', 'Responda antes de abrir.')
b += quiz([
    ('Qual dispositivo da Constituição boliviana permitiu ao TCP aplicar a Convenção por cima dela?', 'O art. 256: tratados de direitos humanos que declarem direitos mais favoráveis aplicam-se de maneira preferente sobre a Constituição.'),
    ('O que a SCP 0084/2017 decidiu, exatamente?', 'Declarou a aplicação preferente do art. 23 da Convenção sobre as expressões "por una sola vez de manera continua" dos arts. 156, 168, 285.II e 288 da Constituição, e a inconstitucionalidade das expressões equivalentes da Lei 026/2010 (regime eleitoral).'),
    ('Por que a decisão boliviana é um "paradoxo" da soberania popular?', 'Porque invocou direitos políticos para liberar a candidatura que a maioria havia recusado no referendo de 2016. O Tribunal não anulou o referendo: afastou as regras que limitavam a reeleição, com o mesmo efeito prático que o “sim” teria tido.'),
    ('Quais são as três respostas da OC-28/21?', 'A reeleição presidencial indefinida não é direito autônomo; sua proibição é compatível com a Convenção, a Declaração Americana e a Carta Democrática; e habilitá-la é contrário aos princípios da democracia representativa. Votação: 5 × 2 (vencidos Pazmiño Freire e Zaffaroni).'),
    ('Como Gelman e a SCP 0084/2017 usam a Convenção em direções opostas?', 'Em Gelman, a Convenção limita a maioria para proteger as vítimas. Na Bolívia, é aplicada com preferência sobre a Constituição para ampliar o direito de quem governa de concorrer outra vez, apesar do resultado do referendo.'),
])

lesson('06', 'aula-06.html', 'Reeleição e direitos políticos: Bolívia e OC-28',
       'TCP da Bolívia, SCP 0084/2017: aplicação preferente do art. 23 da Convenção sobre os limites constitucionais à reeleição; Corte IDH, OC-28/21: a reeleição indefinida não é direito humano.',
       'Reeleição e', 'direitos políticos',
       'Em Gelman, a Convenção limitou a maioria para proteger vítimas. Na Bolívia, um tribunal a usou para <strong class="conc">liberar a candidatura que o referendo recusou</strong>. Em 2021, a Corte Interamericana <strong class="dif">leu o mesmo artigo ao contrário</strong>.',
       hero, [('Aula', '31/08 · Soberania popular'), ('Leitura', '≈ 16 min'), ('Antes', 'Aula 05 · Gelman'), ('Depois', 'Aula 07 · Estado de coisas')], b,
       ('aula-05.html', '← Aula 05', 'Gelman e a soberania popular'), ('aula-07.html', 'Aula 07 →', 'Estado de coisas inconstitucional'), '31/08')
