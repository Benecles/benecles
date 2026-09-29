from kit import *

# hero: a cost line that runs flat, then jumps mid-contract
hero = ('<path d="M30 140H1050" style="stroke:var(--ink);stroke-width:1.5;fill:none"/>'
        '<path class="draw" d="M30 120H520C560 120 580 110 600 40H1050" style="stroke:var(--conc);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:.4s"><circle cx="30" cy="120" r="8" style="fill:var(--ink)"/></g>'
        '<g class="pop" style="--d:1.4s"><circle cx="600" cy="40" r="10" style="fill:var(--conc)"/></g>'
        '<g class="pop" style="--d:1.6s;font:12px var(--mono);letter-spacing:1px"><text x="30" y="162" style="fill:var(--ink)">CELEBRAÇÃO</text>'
        '<text x="620" y="30" style="fill:var(--conc)">FATO SUPERVENIENTE</text><text x="1050" y="162" text-anchor="end" style="fill:var(--ink)">EXECUÇÃO</text></g>')

# ---- Fig 1: risk band chart
def risk(k):
    o = T(40, 60, 'CUSTO DA PRESTAÇÃO AO LONGO DO CONTRATO', 't-small', style='letter-spacing:.1em')
    o += P('M70 440H560M70 90V440', 'ink')
    o += T(560, 466, 'tempo', 't-small', anchor='end') + T(60, 96, 'custo', 't-small', anchor='end')
    o += G(R(70, 270, 490, 110, 'w-dif', extra=' stroke="none" opacity=".7"'), 'fade', d=0) + T(90, 294, 'ÁLEA NORMAL · O RISCO DO NEGÓCIO', 't-small tc-dif')
    if k == 0:
        o += P('M70 340C140 330 180 350 240 320S360 300 420 330S520 300 560 310', 'c-conc grow', style='--d:.2s')
        o += G(T(300, 520, 'oscilou dentro do esperado: fica com quem assumiu', 't-hand', anchor='middle'), 'fade', d=1)
    else:
        o += P('M70 340C140 330 180 350 240 320S300 330 320 320C340 300 350 140 380 130S520 140 560 135', 'c-conc grow', style='--d:.2s')
        o += G(C(380, 130, 10, 'f-ink', style='fill:var(--conc)') + T(392, 116, 'FATO EXTRAORDINÁRIO?', 't-small tc-conc'), 'pop', d=1.1)
        o += G(T(300, 520, 'saiu da faixa: agora vale perguntar pela lei', 't-hand', anchor='middle'), 'fade', d=1.3)
    return o
alloc = (T(40, 60, 'ANTES DA LEI, O CONTRATO', 't-small', style='letter-spacing:.1em')
         + G(doc(60, 90, 200, 260, None, lines=9), 'pop', d=.1)
         + G(R(70, 150, 180, 26, 'w-grey ink') + T(80, 168, 'preço fixo por 1 ano', 't-small'), 'pop', d=.3)
         + G(R(70, 210, 180, 26, 'w-grey ink') + T(80, 228, 'risco cambial: B', 't-small'), 'pop', d=.5)
         + G(R(70, 270, 180, 26, 'w-grey ink') + T(80, 288, 'reajuste pelo IPCA', 't-small'), 'pop', d=.7)
         + P('M270 220H330', 'c-dif grow', m='p-alloc-d', extra=' style="--d:.9s"')
         + G(box(340, 150, 220, 140, 'QUEM ABSORVE?', 'o que o contrato', 'dif', ctx='alloc', sub2='já distribuiu') + T(354, 272, 'fica onde foi posto', 't-small'), 'pop', d=1.1)
         + G(T(300, 430, 'o nome do evento (“crise”)', 't-hand', anchor='middle') + T(300, 460, 'não decide nada sozinho', 't-hand', anchor='middle'), 'fade', d=1.3))

# ---- Fig 2: three doors
DOORS = [('ART. 317', 'CORRIGE O VALOR', ['motivo imprevisível', 'desproporção manifesta', 'valor devido × na execução'], 'dif'),
         ('ARTS. 478–480', 'RESOLVE (OU EVITA)', ['execução continuada/diferida', 'onerosidade excessiva', 'extrema vantagem do outro', 'fato extraordinário e imprevisível'], 'conc'),
         ('CDC · ART. 6º, V', 'REVÊ A CLÁUSULA', ['relação de consumo', 'fato superveniente', 'prestação excessivamente onerosa'], 'mix')]
def doors(k):
    o = ''
    for i, (art, eff, _, tone) in enumerate(DOORS):
        x = 50 + i * 180
        on = i == k
        cls = f'w-{tone} ink' if on else 'f-paper ink'
        o += G(R(x, 60, 140, 190, cls, style='' if on else 'opacity:.45') + C(x + 118, 160, 5, 'f-ink', style='' if on else 'opacity:.45')
               + T(x + 70, 280, art, 't-small' + (f' tc-{tone}' if on else ''), anchor='middle', style='' if on else 'opacity:.5'), 'pop' if on else '', d=.1)
        if on:
            o += T(x + 70, 110, eff.split(' ')[0], f't-small tc-{tone}', anchor='middle') + T(x + 70, 128, ' '.join(eff.split(' ')[1:]), f't-small tc-{tone}', anchor='middle')
    art, eff, reqs, tone = DOORS[k]
    o += T(40, 330, 'O QUE PRECISA ESTAR PRESENTE', 't-small', style='letter-spacing:.1em')
    for j, r in enumerate(reqs):
        o += G(R(40, 346 + j * 46, 30, 30, 'f-paper ink') + check(55, 361 + j * 46) + T(86, 367 + j * 46, r, 't-serif'), 'pop', d=.3 + .15 * j)
    return o
resol = (T(40, 60, 'ARTS. 478 A 480 · A ROTA RESOLUTIVA', 't-small', style='letter-spacing:.1em')
         + G(box(40, 90, 240, 100, 'DEVEDOR', 'pede a resolução', 'conc', ctx='res', sub2='(art. 478)'), 'pop', d=.1)
         + P('M280 140H330', 'c-conc grow', m='p-resol-c', extra=' style="--d:.3s"')
         + G(box(340, 90, 220, 100, 'RÉU', 'pode oferecer', 'dif', ctx='res', sub2='modificação equitativa') , 'pop', d=.5)
         + P('M450 190V230', 'c-dif grow', m='p-resol-d', extra=' style="--d:.7s"')
         + G(box(340, 236, 220, 90, 'SEM RESOLUÇÃO', 'art. 479', 'dif', ctx='res'), 'pop', d=.9)
         + G(R(40, 236, 240, 90, 'f-paper ink', style='stroke-dasharray:5 4') + T(56, 268, 'SENTENÇA', 't-small') + T(56, 288, 'efeitos retroagem', 't-small') + T(56, 306, 'à citação (art. 478)', 't-small'), 'pop', d=1.0)
         + G(box(40, 380, 520, 110, 'ART. 480', 'se só uma parte tem obrigações, ela pode pedir', 'grey', ctx='res', sub2='redução da prestação ou outro modo de executar'), 'pop', d=1.2))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Uma alta de custo basta?', 'Uma empresa promete entregar refeições por preço fixo durante um ano. Um ingrediente encarece muito. O caixa sofre, mas a pergunta jurídica é outra: esse risco estava dentro do que o contrato distribuiu?', 'conc')
b += scrolly('Comece pelo risco', [('p-r0', risk(0), 'Álea normal'), ('p-r1', risk(1), 'Fora da faixa'), ('p-alloc', alloc, 'Alocação')], [
    S('p-r0', 'Álea normal', 'Todo contrato já carrega risco', '<p>Oscilações ordinárias de preço, câmbio ou demanda fazem parte do negócio. Quem fixou um preço por um ano assumiu, em princípio, que os custos variariam nesse período. Ficar mais caro, sozinho, não é fundamento de revisão.</p>'),
    S('p-r1', 'Fora da faixa', 'Quando o fato sai do esperado', '<p>A pergunta muda quando o evento foge objetivamente do risco próprio daquela contratação. Só aí faz sentido testar os requisitos legais. Dificuldade financeira de uma das partes não prova nenhum deles.</p>', 'conc'),
    S('p-alloc', 'O contrato primeiro', 'Leia a alocação de riscos', '<p>Preço fixo, índice de reajuste, cláusula cambial, faixas de consumo, força maior: o contrato costuma dizer quem absorve certas mudanças. Se o risco cambial foi expressamente posto numa parte, a desvalorização tende a ficar com ela.</p>', 'dif'),
])
b += chapter('02', 'c2', 'Três portas legais', 'O Código Civil não tem uma regra única de “reequilíbrio”. O art. 317 corrige o valor de uma prestação; os arts. 478 a 480 tratam da resolução e de como evitá-la; no consumo, o art. 6º, V, do CDC tem requisitos próprios.', 'dif')
b += scrolly('Qual porta abrir', [(f'p-dr{k}', doors(k), DOORS[k][0]) for k in range(3)] + [('p-resol', resol, '478–480')], [
    S('p-dr0', 'Art. 317', 'Corrigir o valor da prestação', '<p>Quando, por motivos imprevisíveis, surge desproporção manifesta entre o valor da prestação devida e o valor no momento da execução, o juiz pode corrigi-lo, a pedido da parte, para assegurar quanto possível o valor real da prestação.</p><p>O foco é o valor de uma prestação, não o destino do contrato. O alcance exato do artigo é discutido.</p>', 'dif'),
    S('p-dr1', 'Art. 478', 'Resolver por onerosidade excessiva', '<p>O art. 478 exige mais: contrato de execução continuada ou diferida, prestação excessivamente onerosa, <strong>extrema vantagem</strong> para a outra parte e acontecimento <strong>extraordinário e imprevisível</strong>. Presentes os requisitos, o devedor pode pedir a resolução.</p>', 'conc'),
    S('p-dr2', 'CDC · art. 6º, V', 'No consumo, outra pergunta', '<p>O consumidor tem direito à modificação de cláusulas que estabeleçam prestações desproporcionais e à revisão por fatos supervenientes que as tornem excessivamente onerosas. O texto não exige imprevisibilidade, extraordinariedade nem extrema vantagem da outra parte.</p><p>Isso não é direito automático a novo preço: ainda é preciso provar a relação de consumo, o fato posterior e a onerosidade. Só não se transplantam para cá os requisitos do art. 478.</p>'),
    S('p-resol', 'Arts. 479 e 480', 'Evitar a resolução', '<p>O réu pode evitar a resolução oferecendo-se a modificar equitativamente as condições do contrato (art. 479). E se as obrigações couberem a uma só parte, ela pode pedir a redução da prestação ou a alteração do modo de executá-la (art. 480).</p><p>Não misture as rotas: o art. 317 corrige um valor; os arts. 478 e 479 abrem a porta da resolução.</p>', 'conc'),
])
b += chapter('03', 'c3', 'Quem pode pedir revisão?', 'O art. 478 dá ao devedor o pedido de resolução, e o art. 479 dá ao réu a oferta de modificação. A pergunta aberta é se o próprio devedor pode pedir, direto, que o juiz reescreva o contrato.', 'conc')
b += wide(table(['Leitura', 'O que admite', 'Limite'], [
    ['Textual restritiva', 'O devedor pede resolução; o credor evita o fim oferecendo modificação equitativa.', 'Não há pedido geral do devedor para reescrever o contrato pelos arts. 478 e 479, nem revisão de ofício.'],
    ['Integrativa', 'Revisão judicial pedida pela parte onerada, para conservar o contrato, com base na equidade e na boa-fé.', 'Continua exigindo os pressupostos; não é licença para consertar qualquer mau negócio. Recomenda-se pedir a resolução como pedido sucessivo.'],
    ['Intermediária', 'Rejeita impor revisão ao credor pelos arts. 478 e 479, mas vê no art. 317 uma via própria, mais estreita, de correção da prestação.', 'Depende do alcance que se dá ao art. 317.'],
], hcls=['', 'conc', 'dif']) + '<p class="note">São posições doutrinárias concorrentes. Na prova, diga qual adota e formule os pedidos de modo coerente com ela. A exigência de “extrema vantagem” continua no texto do art. 478, ainda que parte da doutrina a relativize.</p>')
b += chapter('04', 'c4', 'Teste', 'Teste o caminho antes de escolher o remédio.')
b += quiz([
    ('Uma empresa perde margem porque o custo de um insumo sobe dentro da variação usual do setor. O que verificar antes de invocar o art. 478?', 'Se o preço e a matriz de riscos já cobriam essa variação; se o evento foge da álea normal; se há onerosidade excessiva e extrema vantagem; e se a execução é continuada ou diferida. Alta de custo sozinha não passa no teste.'),
    ('Numa compra parcelada, um motivo imprevisível cria diferença manifesta entre o valor devido e o valor na data de pagamento. Qual dispositivo trata diretamente da correção?', 'O art. 317, que permite ao juiz corrigir o valor real da prestação a pedido da parte.'),
    ('Numa relação de consumo, um fato posterior tornou a prestação excessivamente onerosa, mas não era extraordinário. Isso encerra a análise?', 'Não. O art. 6º, V, do CDC não exige fato extraordinário e imprevisível. Ainda é preciso provar relação de consumo, fato superveniente e onerosidade.'),
    ('O devedor pede resolução pelo art. 478 e o credor oferece modificação equitativa. O que é certo e o que é discutido?', 'É certo que a oferta pode evitar a resolução (art. 479). É discutido se o devedor poderia, desde o início, pedir diretamente a revisão.'),
    ('A transportadora assumiu expressamente o risco cambial num preço anual fixo. A moeda desvaloriza. Por onde começa a análise?', 'Pela cláusula: se o risco foi alocado a ela, a perda tende a ficar com ela. Só se o evento fugir do que a cláusula cobre é que se testam os arts. 317 ou 478.'),
])
page('aula-12.html', '12', 'Revisão: o que mudou na execução',
     'Revisão dos contratos II: álea normal, art. 317, arts. 478 a 480, CDC art. 6º, V, e o debate sobre revisão pedida pelo devedor.',
     ['Unidade 7 · Revisão', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'O que mudou', 'na execução',
     'Uma prestação ficou muito mais difícil depois da assinatura. Antes de pedir ajuste, descubra <strong class="dif">qual risco foi assumido</strong>, qual regra se aplica e quem pode pedir <strong class="conc">cada remédio</strong>.',
     hero, [('Unidade', '7 · Revisão II'), ('Leitura', '≈ 14 min'), ('Antes', 'Aula 11 · Desequilíbrio na origem'), ('Depois', 'Aula 13 · Base do negócio')], b,
     ('aula-11.html', '← Aula 11', 'Desequilíbrio na formação'), ('aula-13.html', 'Aula 13 →', 'A base comum do negócio'), unit='7')
