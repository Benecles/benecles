from kit import *

# hero: one contract seen through five lenses
labs = ['FORMAÇÃO', 'TEMPO', 'NEGOCIAÇÃO', 'ESTRUTURA', 'FUNÇÃO']
hero = ('<g class="pop" style="--d:.2s"><rect x="480" y="22" width="120" height="118" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
        '<path d="M500 60h80M500 80h80M500 100h50" style="stroke:var(--ink);stroke-width:1"/></g>')
xs = [70, 280, 540, 800, 1010]
for i, (l, x) in enumerate(zip(labs, xs)):
    if i == 2: continue
    y = 60 if i in (0, 4) else 120
    hero += (f'<path class="draw" style="--d:{.3+.2*i}s;stroke:var(--{"conc" if i < 2 else "dif"});stroke-width:1.5;fill:none;stroke-dasharray:5 4" d="M{x} {y}L{480 if x < 540 else 600} 90"/>'
             f'<g class="pop" style="--d:{.8+.15*i}s"><circle cx="{x}" cy="{y}" r="7" style="fill:var(--{"conc" if i < 2 else "dif"})"/>'
             f'<text x="{x}" y="{y+30}" text-anchor="middle" style="font:12px var(--mono);letter-spacing:1px;fill:var(--ink)">{l}</text></g>')
hero += '<g class="pop" style="--d:1.4s"><text x="540" y="163" text-anchor="middle" style="font:12px var(--mono);letter-spacing:1px;fill:var(--ink)">NEGOCIAÇÃO</text></g>'

def hands(cx, cy):
    return (P(f'M{cx-38} {cy}H{cx+38}', 'ink', style='stroke-width:2.5')
            + C(cx - 52, cy, 16, 'w-conc c-conc', extra=' stroke-width="2"') + C(cx + 52, cy, 16, 'w-dif c-dif', extra=' stroke-width="2"')
            + T(cx - 52, cy + 5, 'A', 't-small tc-conc', anchor='middle') + T(cx + 52, cy + 5, 'B', 't-small tc-dif', anchor='middle'))
cons = (T(40, 64, 'CONSENSUAL', 't-small', style='letter-spacing:.1em')
        + P('M60 300H540', 'ink', style='stroke-width:2')
        + G(hands(170, 220), 'pop', d=.1) + G(C(170, 300, 10, 'f-ink', style='fill:var(--dif)'), 'pop', d=.3)
        + T(170, 340, 'ACORDO', 't-small tc-dif', anchor='middle') + T(170, 360, 'o contrato existe', 't-small', anchor='middle')
        + G(R(400, 190, 60, 50, 'w-grey ink') + P('M400 190l30 -18l30 18', 'ink'), 'pop', d=.6) + G(C(430, 300, 8, 'f-paper ink'), 'pop', d=.6)
        + T(430, 340, 'ENTREGA', 't-small', anchor='middle') + T(430, 360, 'já é cumprimento', 't-small', anchor='middle')
        + G(box(40, 420, 520, 100, 'REGRA', 'basta o acordo de vontades', 'dif', ctx='cons'), 'pop', d=.9))
real = (T(40, 64, 'REAL', 't-small', style='letter-spacing:.1em')
        + P('M60 300H540', 'ink', style='stroke-width:2')
        + G(hands(170, 220), 'pop', d=.1) + C(170, 300, 8, 'f-paper ink')
        + T(170, 340, 'ACORDO', 't-small', anchor='middle') + T(170, 360, 'ainda não basta', 't-small', anchor='middle')
        + G(R(400, 190, 60, 50, 'w-conc ink') + P('M400 190l30 -18l30 18', 'ink'), 'pop', d=.6) + G(C(430, 300, 10, 'f-ink', style='fill:var(--conc)'), 'pop', d=.7)
        + T(430, 340, 'ENTREGA', 't-small tc-conc', anchor='middle') + T(430, 360, 'o contrato se forma', 't-small', anchor='middle')
        + P('M230 200C300 150 360 150 396 186', 'c-conc grow', m='p-real-c', extra=' style="--d:.5s"')
        + G(box(40, 420, 520, 100, 'EXEMPLOS', 'comodato, mútuo, depósito', 'conc', ctx='real'), 'pop', d=1.0))
form = (T(40, 64, 'FORMA · ARTS. 107 A 109', 't-small', style='letter-spacing:.1em')
        + G(box(40, 90, 520, 90, 'ART. 107 · LIBERDADE', 'a regra: qualquer forma, até verbal', 'grey', ctx='form'), 'pop', d=.1)
        + T(40, 230, 'VALOR DO IMÓVEL', 't-small') + P('M40 250H560', 'ink', style='stroke-width:2')
        + G(R(360, 240, 200, 20, 'w-conc', extra=' stroke="none"'), 'pop', d=.4) + P('M360 232V268', 'c-conc', style='stroke-width:3')
        + T(360, 290, '30 SALÁRIOS MÍNIMOS', 't-small tc-conc', anchor='middle')
        + G(doc(460, 300, 80, 96, None, 'w-conc ink', lines=4), 'pop', d=.7) + T(500, 418, 'escritura', 't-small', anchor='middle')
        + G(T(80, 330, 'acima: escritura pública', 't-hand') + T(80, 360, 'para direito real (108)', 't-hand'), 'fade', d=.8)
        + G(box(40, 450, 520, 90, 'ART. 109 · CONVENCIONAL', 'as partes combinam que só vale com certa forma', 'dif', ctx='form'), 'pop', d=1.1))

def timeline(k):
    o = T(40, 64, 'QUANDO SE CUMPRE', 't-small', style='letter-spacing:.1em')
    rows = [('IMEDIATA', [90]), ('DIFERIDA', [430]), ('CONTINUADA', list(range(150, 541, 45)))]
    for i, (lab, pts) in enumerate(rows):
        y = 140 + i * 110
        on = (k == 3) or (i == k)
        o += T(40, y - 20, lab, 't-small' + (' tc-dif' if on and i else ' tc-conc' if on else ''), style='' if on else 'opacity:.4')
        o += P(f'M40 {y}H560', 'ink' if on else 'thin', style='stroke-width:1.5')
        o += C(60, y, 6, 'f-ink')
        for j, x in enumerate(pts):
            o += G(C(x, y, 9, 'f-ink', style=f'fill:var(--{"dif" if i else "conc"})' if on else 'opacity:.3'), 'pop' if on else '', d=.2 + .08 * j)
    if k == 3:
        o += G(R(300, 250, 260, 240, 'w-conc', extra=' stroke="none" opacity=".45"'), 'fade', d=.2)
        o += G(box(40, 470, 520, 90, 'ART. 478', 'onerosidade excessiva: só com tempo no meio', 'conc', ctx='tl'), 'pop', d=1.0)
    else:
        o += T(60, 164 + k * 110, 'celebração', 't-small')
        notes = ['cumpre-se de uma vez, logo', 'de uma vez, mas no futuro', 'ao longo do tempo (locação)']
        o += G(T(300, 520, notes[k], 't-hand', anchor='middle'), 'fade', d=.6)
    return o

def sheet(x, y, w, h, cls='f-paper ink'):
    o = R(x, y, w, h, cls)
    for i in range(6): o += P(f'M{x+18} {y+26+i*20}h{w-36 if i%3!=2 else (w-36)*.6:.0f}', 'thin')
    return o
par = (G(sheet(200, 90, 200, 190), 'pop', d=.1)
       + G(person(110, 170, None, 'c-conc'), 'pop', d=.2) + G(person(490, 170, None, 'c-dif'), 'pop', d=.3)
       + P('M140 190C170 170 190 150 220 150', 'c-conc grow', extra=' style="--d:.5s"') + P('M460 190C430 170 410 190 380 190', 'c-dif grow', extra=' style="--d:.7s"')
       + G(T(300, 330, 'as duas redigem', 't-hand', anchor='middle'), 'fade', d=.9)
       + G(box(40, 400, 520, 100, 'PARITÁRIO', 'cláusulas negociadas em pé de igualdade', 'dif', ctx='par', sub2='presumido nos civis e empresariais (421-A)'), 'pop', d=1.1))
ade = (G(sheet(60, 90, 220, 220, 'w-conc ink'), 'pop', d=.1) + T(170, 340, 'PRONTO', 't-small tc-conc', anchor='middle')
       + G(R(360, 130, 180, 50, 'w-dif ink') + T(450, 161, 'ACEITO TUDO', 't-small tc-dif', anchor='middle'), 'pop', d=.5)
       + G(R(360, 200, 180, 50, 'f-paper ink') + T(450, 231, 'RECUSO TUDO', 't-small', anchor='middle'), 'pop', d=.7)
       + P('M290 180H352M290 220H352', 'thin')
       + G(T(450, 290, 'escolher entre opções', 't-hand', anchor='middle') + T(450, 318, 'não é negociar', 't-hand', anchor='middle'), 'fade', d=.9)
       + G(box(40, 390, 250, 150, 'CÓDIGO CIVIL', 'ambiguidade: pró-aderente (423)', 'conc', ctx='ade', sub2='renúncia antecipada nula (424)'), 'pop', d=1.1)
       + G(box(310, 390, 250, 150, 'CDC', 'tudo se interpreta', 'grey', ctx='ade', sub2='a favor do consumidor (47)'), 'pop', d=1.3))

acc = (G(sheet(60, 90, 200, 170), 'pop', d=.1) + T(160, 290, 'DÍVIDA', 't-small', anchor='middle') + T(160, 308, '(principal)', 't-small', anchor='middle')
       + G(sheet(340, 130, 170, 130, 'w-dif ink'), 'pop', d=.4) + T(425, 290, 'FIANÇA', 't-small tc-dif', anchor='middle') + T(425, 308, '(acessório)', 't-small', anchor='middle')
       + P('M262 175C300 175 300 195 338 195', 'c-dif grow', m='p-acc-d', extra=' style="--d:.6s"')
       + G(P('M70 380H250', 'c-conc', style='stroke-width:4') + T(160, 360, 'EXTINTA', 't-small tc-conc', anchor='middle')
           + P('M350 380H500', 'c-conc', style='stroke-width:4') + T(425, 360, 'EXTINTA TAMBÉM', 't-small tc-conc', anchor='middle'), 'pop', d=1.0)
       + G(T(300, 480, 'o acessório segue a sorte', 't-hand', anchor='middle') + T(300, 510, 'do principal', 't-hand', anchor='middle'), 'fade', d=1.3))
misto = (T(40, 64, 'UM SÓ CONTRATO · HOSPEDAGEM', 't-small', style='letter-spacing:.1em')
         + R(140, 100, 320, 330, 'f-paper ink')
         + G(R(140, 100, 320, 110, 'w-conc', extra=' stroke="none"') + T(300, 162, 'LOCAÇÃO', 't-mid tc-conc', anchor='middle'), 'pop', d=.2)
         + G(R(140, 210, 320, 110, 'w-dif', extra=' stroke="none"') + T(300, 272, 'SERVIÇOS', 't-mid tc-dif', anchor='middle'), 'pop', d=.4)
         + G(R(140, 320, 320, 110, 'w-grey', extra=' stroke="none"') + T(300, 382, 'DEPÓSITO', 't-mid', anchor='middle'), 'pop', d=.6)
         + R(140, 100, 320, 330, 'ink', style='fill:none;stroke-width:2')
         + G(T(300, 490, 'elementos de vários tipos', 't-hand', anchor='middle') + T(300, 520, 'num só vínculo', 't-hand', anchor='middle'), 'fade', d=.9))
colig = (T(40, 64, 'VÁRIOS CONTRATOS · UMA OPERAÇÃO', 't-small', style='letter-spacing:.1em')
         + G(C(300, 300, 64, 'w-conc ink') + T(300, 296, 'COMPRAR', 't-small tc-conc', anchor='middle') + T(300, 314, 'O CARRO', 't-small tc-conc', anchor='middle'), 'pop', d=.1)
         + G(sheet(60, 100, 130, 110) + T(125, 232, 'COMPRA E VENDA', 't-small', anchor='middle'), 'pop', d=.3)
         + G(sheet(410, 100, 130, 110) + T(475, 232, 'FINANCIAMENTO', 't-small', anchor='middle'), 'pop', d=.5)
         + G(sheet(235, 420, 130, 110) + T(300, 552, 'SEGURO', 't-small', anchor='middle'), 'pop', d=.7)
         + P('M160 240L252 260M440 240L348 260M300 364V414', 'c-conc grow', style='--d:.9s'))

rel = (T(40, 64, 'DESCONTÍNUO', 't-small', style='letter-spacing:.1em')
       + G(C(120, 150, 26, 'w-grey ink') + C(480, 150, 26, 'w-grey ink') + P('M150 142H450', 'ink', m='p-rel-i') + P('M450 160H150', 'ink', m='p-rel-i'), 'pop', d=.1)
       + T(300, 210, 'uma troca e acabou', 't-hand', anchor='middle')
       + T(40, 280, 'RELACIONAL', 't-small tc-dif', style='letter-spacing:.1em')
       + G(C(120, 400, 26, 'w-dif ink') + C(480, 400, 26, 'w-dif ink'), 'pop', d=.4)
       + P('M146 390C220 320 380 320 454 390', 'c-dif grow', m='p-rel-d', extra=' style="--d:.6s"')
       + P('M454 410C380 480 220 480 146 410', 'c-dif grow', m='p-rel-d', extra=' style="--d:.9s"')
       + P('M200 350C230 380 260 350 290 380M310 420C340 450 370 420 400 450', 'c-dif grow', style='stroke-width:1.5;--d:1.1s')
       + G(T(300, 540, 'ajustes durante a execução', 't-hand', anchor='middle'), 'fade', d=1.3))
exi = (T(40, 64, 'A FUNÇÃO DO CONTRATO', 't-small', style='letter-spacing:.1em')
       + R(40, 110, 520, 30, 'f-paper ink') + G(R(40, 110, 260, 30, 'w-conc', extra=' stroke="none"'), 'pop', d=.1) + G(R(300, 110, 260, 30, 'w-dif', extra=' stroke="none"'), 'pop', d=.2)
       + T(40, 170, 'EXISTENCIAL', 't-small tc-conc') + T(560, 170, 'DE LUCRO', 't-small tc-dif', anchor='end')
       + T(40, 190, 'saúde · moradia · alimentação', 't-small') + T(560, 190, 'empresas · investidores', 't-small', anchor='end')
       + G(box(170, 250, 260, 70, 'PLANO DE SAÚDE', None, 'grey', ctx='exi'), 'pop', d=.5)
       + P('M220 320C200 360 150 360 120 380', 'c-conc grow', m='p-exi-c', extra=' style="--d:.8s"') + P('M380 320C400 360 450 360 480 380', 'c-dif grow', m='p-exi-d', extra=' style="--d:.8s"')
       + G(box(40, 390, 250, 80, 'PARA O PACIENTE', 'existencial', 'conc', ctx='exi'), 'pop', d=1.0)
       + G(box(310, 390, 250, 80, 'PARA A EMPRESA', 'de lucro', 'dif', ctx='exi'), 'pop', d=1.1)
       + G(T(300, 530, 'decide a função, não a intenção', 't-hand', anchor='middle'), 'fade', d=1.3))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Formação e forma', 'Um mesmo contrato pode ser consensual, de execução diferida, de adesão e acessório. As classificações se acumulam porque cada uma olha para um aspecto.')
b += scrolly('Como o contrato se forma', [('p-cons', cons, 'Consensual'), ('p-real', real, 'Real'), ('p-form', form, 'Forma')], [
    S('p-cons', 'Consensuais', 'Basta o acordo', '<p>Nos contratos consensuais, o acordo de vontades forma o contrato. A entrega da coisa, quando vem, já é cumprimento de um contrato que existe.</p>', 'dif'),
    S('p-real', 'Reais', 'Só com a entrega', '<p>Nos contratos reais, o contrato só se forma com a entrega da coisa: comodato, mútuo, depósito. Antes dela, pode haver promessa, mas não o contrato real.</p>', 'conc'),
    S('p-form', 'Formais', 'A forma', '<p>A regra é a liberdade de forma (art. 107). A exceção mais importante é a escritura pública para negócios sobre direitos reais em imóveis de valor superior a trinta salários mínimos (art. 108): é a <strong>forma legal</strong>. As partes também podem combinar que o contrato só vale se tiver certa forma (art. 109): é a <strong>forma convencional</strong>.</p><p>Um contrato não é formal só porque foi escrito.</p>'),
])
b += chapter('02', 'c2', 'O tempo do cumprimento', 'A prestação pode ser cumprida logo, de uma vez no futuro, ou ao longo do tempo.', 'conc')
b += scrolly('Execução', [(f'p-tl{k}', timeline(k), l) for k, l in enumerate(['Imediata', 'Diferida', 'Continuada', 'Art. 478'])], [
    S('p-tl0', 'Imediata', 'Execução imediata', '<p>A prestação é cumprida de uma vez, logo após a celebração. A compra no balcão é o exemplo.</p>', 'conc'),
    S('p-tl1', 'Diferida', 'Execução diferida', '<p>A prestação é cumprida de uma vez, mas numa data futura. A entrega marcada para o mês que vem não muda a formação: o contrato consensual já existe.</p>', 'dif'),
    S('p-tl2', 'Continuada', 'Execução continuada', '<p>Também chamada de trato sucessivo: a prestação se cumpre ao longo do tempo, em parcelas que se renovam, como o aluguel na locação.</p>', 'dif'),
    S('p-tl3', 'Por que importa', 'Onerosidade excessiva', '<p>O art. 478 só se aplica aos contratos de execução continuada ou diferida, porque é neles que o tempo entre a celebração e o cumprimento pode desequilibrar as prestações. Na execução imediata, não há esse intervalo.</p>', 'conc'),
])
b += chapter('03', 'c3', 'Paritários × de adesão', 'A pergunta é quem redigiu as cláusulas e se a outra parte pôde discuti-las.', 'dif')
b += scrolly('Quem define as cláusulas', [('p-par', par, 'Paritário'), ('p-ade', ade, 'Adesão')], [
    S('p-par', 'Paritário', 'Negociado', '<p>No contrato paritário, as partes negociam as cláusulas em pé de igualdade. O art. 421-A presume paritários os contratos civis e empresariais, até prova em contrário.</p>', 'dif'),
    S('p-ade', 'Adesão', 'Pegar ou largar', '<p>No de adesão, uma parte redige as cláusulas, e a outra só pode aceitar ou recusar o conjunto. Poder escolher entre algumas opções prontas não é negociar.</p><p>Adesão não é o mesmo que consumo: há contratos de adesão entre empresas. No Código Civil, cláusulas ambíguas ou contraditórias se interpretam a favor do aderente (art. 423), e é nula a renúncia antecipada a direito resultante da natureza do negócio (art. 424). No CDC, todas as cláusulas se interpretam da maneira mais favorável ao consumidor (art. 47).</p>', 'conc'),
])
b += chapter('04', 'c4', 'Principais, acessórios, mistos e coligados', 'Há um contrato ou vários? Se vários, um depende juridicamente do outro?')
b += scrolly('A estrutura do vínculo', [('p-acc', acc, 'Acessório'), ('p-misto', misto, 'Misto'), ('p-colig', colig, 'Coligados')], [
    S('p-acc', 'Principal e acessório', 'Um depende do outro', '<p>O contrato acessório existe para servir ao principal e segue a sua sorte: extinta a dívida, extingue-se a fiança que a garantia.</p>', 'dif'),
    S('p-misto', 'Misto', 'Um contrato, vários tipos', '<p>Um só contrato combina elementos de tipos diferentes. A hospedagem reúne locação, prestação de serviços e depósito num único vínculo.</p>'),
    S('p-colig', 'Coligados', 'Vários contratos, um fim', '<p>Vários contratos, cada um com sua individualidade, ligados por uma finalidade econômica comum. Na compra de um carro financiado, a compra e venda e o financiamento servem à mesma operação. A doutrina usa \"coligados\" e \"conexos\" quase como sinônimos.</p><p>Coligação não é acessoriedade: os contratos continuam distintos, e nenhum existe só para garantir o outro.</p>', 'conc'),
])
b += wide(table(['', 'O que significa', 'Cuidado'], [
    ['Típico', 'A lei oferece um modelo para aquele tipo contratual.', 'Não quer dizer frequente, padronizado ou escrito.'],
    ['Atípico', 'Não se enquadra inteiro num modelo legal. O art. 425 permite, observadas as normas gerais.', 'Misto e atípico não são sinônimos: combinar prestações conhecidas pode dar um contrato misto.'],
], hcls=['', 'conc', 'dif']))
b += chapter('05', 'c5', 'Relacionais, existenciais e de lucro', 'Outras classificações olham para o modo como a relação funciona e para o interesse que ela atende.', 'dif')
b += scrolly('Relação e função', [('p-rel', rel, 'Relacional'), ('p-exi', exi, 'Existencial × lucro')], [
    S('p-rel', 'Relacionais', 'Troca pontual × relação contínua', '<p>O contrato descontínuo é uma troca pontual. O relacional se desenvolve numa interação contínua, deixa aspectos para definir durante a execução e exige cooperação para acomodar mudanças, como na franquia e no fornecimento de longo prazo.</p><p>Durar muito não basta: uma locação de temporada com tudo definido desde o início não é relacional.</p>', 'dif'),
    S('p-exi', 'Existenciais e de lucro', 'A função econômica', '<p>Ruy Rosado de Aguiar distingue os contratos <strong>existenciais</strong>, que atendem a necessidades ligadas à subsistência e à dignidade (saúde, moradia, alimentação), dos contratos <strong>de lucro</strong>, celebrados por empresas no exercício da atividade ou por investidores em busca de ganho. Nos existenciais, a intervenção protetiva tende a ser mais intensa.</p><p>O critério é a função do contrato, não a intenção de quem contrata, e os critérios se cruzam: a empresa lucra com o plano de saúde, mas, para o paciente, ele é existencial. Nem todo contrato de consumo é existencial, porque o objeto pode ser supérfluo.</p>', 'conc'),
])
b += chapter('06', 'c6', 'Teste')
b += quiz([
    ('As partes concordaram hoje, mas a entrega da coisa ficou para o mês que vem. Como classificar?', 'Execução diferida. Continua consensual: a entrega é cumprimento de um contrato que já se formou com o acordo.'),
    ('O formulário de financiamento foi elaborado pelo banco e assinado por uma empresa. É contrato de adesão?', 'Pode ser, mesmo com uma empresa como aderente. Se é de consumo, é outra pergunta.'),
    ('Uma locação residencial dura doze meses e tem objeto, preço e deveres definidos na assinatura. É relacional?', 'Não. Tudo foi definido na assinatura; falta a interação contínua e a necessidade de ajustes ao longo do tempo.'),
    ('Venda, crédito e seguro aparecem na aquisição de um veículo. Que tipo de relação há entre eles?', 'São contratos distintos, provavelmente coligados, porque servem à mesma operação. Isso não os funde num contrato só, nem os torna acessórios uns dos outros.'),
    ('Por que a classificação por tempo de execução importa para o art. 478?', 'A onerosidade excessiva só se aplica à execução continuada ou diferida, em que o tempo pode desequilibrar as prestações.'),
])
page('aula-08.html', '08', 'Classificação dos contratos II',
     'Consensuais, reais e formais; execução imediata, diferida e continuada; paritários e de adesão; principais, acessórios, mistos e coligados; relacionais, existenciais e de lucro.',
     ['Unidade 5 · Classificação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Classificação', 'dos contratos II',
     'Mais cinco critérios: como o contrato se forma, quando é cumprido, quem define as cláusulas, como se liga a outros contratos e que interesse atende. Cada um é uma <strong class="conc">lente</strong>; o mesmo contrato passa por todas.',
     hero, [('Unidade', '5 · Classificação II'), ('Leitura', '≈ 14 min'), ('Antes', 'Aula 07 · Classificação I'), ('Depois', 'Aula 09 · Interpretação')], b,
     ('aula-07.html', '← Aula 07', 'Classificação dos contratos I'), ('aula-09.html', 'Aula 09 →', 'Interpretação'), unit='5')
