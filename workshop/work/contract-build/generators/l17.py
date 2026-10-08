from kit import *

# hero: a due date, a late delivery still useful, and a later one that lost its point
hero = ('<path class="draw" d="M30 90H1050" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:.4s"><path d="M300 50V130" style="stroke:var(--ink);stroke-width:2;stroke-dasharray:6 5"/></g>'
        '<g class="pop" style="--d:.9s"><circle cx="440" cy="90" r="11" style="fill:var(--dif)"/></g>'
        '<g class="pop" style="--d:1.2s"><path d="M720 50V130" style="stroke:var(--conc);stroke-width:3"/></g>'
        '<g class="pop" style="--d:1.5s"><circle cx="880" cy="90" r="11" style="fill:var(--conc)"/></g>'
        '<g class="pop" style="--d:1.7s;font:12px var(--mono);letter-spacing:1px"><text x="300" y="36" text-anchor="middle" style="fill:var(--ink)">PRAZO</text>'
        '<text x="440" y="130" text-anchor="middle" style="fill:var(--dif)">AINDA ÚTIL · MORA</text>'
        '<text x="720" y="36" text-anchor="middle" style="fill:var(--conc)">A CERIMÔNIA</text>'
        '<text x="880" y="130" text-anchor="middle" style="fill:var(--conc)">INÚTIL · DEFINITIVO</text></g>')

# ---- Fig 1: useful interest
def util(k):
    o = T(40, 60, 'O INTERESSE ÚTIL DO CREDOR', 't-small', style='letter-spacing:.1em')
    o += P('M50 200H550', 'ink', style='stroke-width:2')
    o += G(P('M150 150V250', 'ink', style='stroke-dasharray:6 5') + T(150, 140, 'PRAZO', 't-small', anchor='middle'), 'pop', d=0)
    if k == 0:
        o += G(R(250, 170, 60, 50, 'w-grey ink') + P('M256 170v-14h48v14', 'ink') + T(280, 250, 'MÓVEL', 't-small', anchor='middle') + T(280, 268, '2 dias depois', 't-small', anchor='middle'), 'pop', d=.3)
        o += G(box(40, 320, 520, 120, 'MORA', 'atraso imputável, prestação ainda possível', 'dif', ctx='u', sub2='e útil: o credor pode exigir o cumprimento') + T(54, 424, 'e perdas e danos do atraso (arts. 394 a 396)', 't-small'), 'pop', d=.7)
    elif k == 1:
        o += G(P('M380 150V250', 'c-conc', style='stroke-width:3') + T(380, 140, 'CERIMÔNIA', 't-small tc-conc', anchor='middle'), 'pop', d=.2)
        o += G(C(470, 190, 30, 'w-conc ink') + P('M446 184h48M452 184c0-18 36-18 36 0', 'ink') + T(470, 250, 'BOLO', 't-small tc-conc', anchor='middle') + T(470, 268, 'no dia seguinte', 't-small', anchor='middle'), 'pop', d=.5)
        o += G(box(40, 320, 520, 120, 'INADIMPLEMENTO DEFINITIVO', 'ainda possível fisicamente, mas sem', 'conc', ctx='u', sub2='a utilidade que dava sentido ao prazo') + T(54, 424, 'o credor pode enjeitar e pedir perdas e danos (art. 395, p. ú.)', 't-small'), 'pop', d=.8)
    else:
        o += G(R(250, 170, 60, 50, 'w-grey ink') + T(280, 250, 'ENTREGUE', 't-small', anchor='middle') + T(280, 268, 'mas errado', 't-small', anchor='middle') + P('M262 182l36 26M298 182l-36 26', 'c-conc'), 'pop', d=.3)
        o += G(box(40, 320, 520, 120, 'CUMPRIMENTO DEFEITUOSO', 'algo foi feito, fora do modo, quantidade', 'grey', ctx='u', sub2='ou qualidade devidos') + T(54, 424, 'pese a relevância da falha para o interesse do credor', 't-small'), 'pop', d=.7)
    o += T(300, 500, ['a pergunta é se ainda serve', 'o prazo era essencial', 'nem toda falha resolve'][k], 't-hand', anchor='middle')
    return o

# ---- Fig 2: express vs tacit clause
def clause(k):
    o = T(40, 60, ['CLÁUSULA RESOLUTIVA EXPRESSA', 'CLÁUSULA RESOLUTIVA TÁCITA'][k] + ' · ART. 474', 't-small', style='letter-spacing:.1em')
    if k == 0:
        steps = [('GATILHO', 'o fato previsto ocorre', 'grey'), ('ESCOLHA', 'o lesado decide resolver', 'conc'), ('COMUNICAÇÃO', 'avisa a outra parte', 'conc'), ('JUIZ, SE PRECISO', 'restituição, resistência', 'grey')]
    else:
        steps = [('INADIMPLEMENTO', 'não há cláusula', 'grey'), ('INTERPELAÇÃO', 'judicial', 'dif'), ('JUIZ AVALIA', 'requisitos do art. 475', 'dif'), ('RESOLUÇÃO', 'pela sentença', 'dif')]
    for i, (a, s, tone) in enumerate(steps):
        y = 90 + i * 100
        dashed = (k == 0 and i == 3)
        o += G(R(120, y, 360, 74, f'w-{tone} ink' if not dashed else 'f-paper ink', style='stroke-dasharray:6 5' if dashed else '')
               + T(140, y + 32, a, 't-small' + (f' tc-{tone}' if tone != 'grey' else '')) + T(140, y + 54, s, 't-small'), 'pop', d=.2 + .3 * i)
        o += C(90, y + 37, 14, 'f-ink') + T(90, y + 42, str(i + 1), 't-small t-light', anchor='middle')
        if i < 3: o += P(f'M300 {y+74}V{y+100}', 'ink')
    o += T(300, 520, ['de pleno direito: sem sentença prévia, mas com manifestação', 'o contrato não tinha previsto o gatilho'][k], 't-hand', anchor='middle')
    return o

# ---- Fig 3: art. 475 choice
fork = (G(box(200, 60, 200, 80, 'PARTE LESADA', 'escolhe', 'grey', ctx='fork'), 'pop', d=0)
        + P('M300 140C300 190 150 180 150 230', 'c-conc grow', m='p-fork-c', style='--d:.3s') + P('M300 140C300 190 450 180 450 230', 'c-dif grow', m='p-fork-d', style='--d:.3s')
        + G(box(40, 236, 230, 100, 'RESOLUÇÃO', 'desfaz o vínculo', 'conc', ctx='fork'), 'pop', d=.7)
        + G(box(330, 236, 230, 100, 'CUMPRIMENTO', 'exige a prestação', 'dif', ctx='fork'), 'pop', d=.8)
        + P('M155 336V380H445V336', 'ink', style='stroke-dasharray:5 4') + P('M300 380V404', 'ink')
        + G(box(150, 406, 300, 90, '+ PERDAS E DANOS', 'em qualquer dos casos', 'ink', ctx='fork'), 'pop', d=1.1)
        + T(300, 552, 'se o essencial foi prestado, resolver pode ser excessivo', 't-hand', anchor='middle'))

# ---- Fig 4: effects in time
def effect(k):
    o = T(40, 60, ['VENDA DE UM BEM · VOLTAR AO INÍCIO', 'PRESTAÇÕES CONTÍNUAS · O USADO FICOU'][k], 't-small', style='letter-spacing:.1em')
    if k == 0:
        o += node(120, 180, 'A', 'conc', 'VENDEDOR') + node(480, 180, 'B', 'dif', 'COMPRADOR')
        o += P('M156 160H444', 'thin') + P('M444 200H156', 'thin')
        o += P('M444 160H156', 'c-dif grow', m='p-ef0-d', style='--d:.4s') + T(300, 148, 'devolve o bem', 't-small tc-dif', anchor='middle')
        o += P('M156 200H444', 'c-conc grow', m='p-ef0-c', style='--d:.7s') + T(300, 226, 'devolve o preço', 't-small tc-conc', anchor='middle')
        o += G(box(40, 320, 520, 110, 'RESTITUIÇÃO RECÍPROCA', 'se devolver a própria coisa não der,', 'grey', ctx='ef', sub2='acerta-se o equivalente'), 'pop', d=1.0)
    else:
        for i in range(10):
            x = 80 + i * 46
            used = i < 6
            o += G(R(x - 16, 150, 32, 32, 'w-grey ink' if used else 'f-paper ink', style='' if used else 'stroke-dasharray:4 3'), 'pop' if used else '', d=.05 * i)
        o += P('M354 130V200', 'c-conc', style='stroke-width:3') + T(354, 120, 'RESOLUÇÃO', 't-small tc-conc', anchor='middle')
        o += T(190, 216, 'já usado e consumido', 't-small', anchor='middle') + T(450, 216, 'não será prestado', 't-small', anchor='middle')
        o += G(box(40, 320, 520, 110, 'NÃO SE DEVOLVE O TEMPO', 'o que foi usado não volta fisicamente;', 'grey', ctx='ef', sub2='acerta-se o que resta e o que é restituível'), 'pop', d=.8)
    o += T(300, 500, 'o nome do contrato não decide o acerto', 't-hand', anchor='middle')
    return o
def node(cx, cy, l, tone='conc', label=None, r=30):
    o = C(cx, cy, r, f'w-{tone} c-{tone}', extra=' stroke-width="2"') + T(cx, cy + 8, l, f't-mid tc-{tone}', anchor='middle')
    if label: o += T(cx, cy + r + 22, label, 't-small', anchor='middle')
    return o

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Nem todo atraso encerra o vínculo', 'A encomenda chega depois do prazo, mas ainda serve: é mora. Se chega tão tarde que perdeu a finalidade, o atraso virou definitivo.', 'conc')
b += scrolly('Mora ou inadimplemento definitivo', [('p-u0', util(0), 'Mora'), ('p-u1', util(1), 'Definitivo'), ('p-u2', util(2), 'Defeituoso')], [
    S('p-u0', 'Mora', 'O móvel que chegou dois dias depois', '<p>A mora supõe atraso imputável ao devedor e prestação ainda possível e útil (arts. 394 a 396). Sem fato ou omissão imputável ao devedor, não há mora. Um móvel entregue dois dias depois ainda serve: o comprador pode exigir e receber, com as perdas e danos do atraso.</p><p>Se o evento foi caso fortuito ou força maior, olhe primeiro para a distribuição do risco (art. 393) antes de falar em inadimplemento culposo.</p>', 'dif'),
    S('p-u1', 'Inadimplemento definitivo', 'O bolo que chegou depois da cerimônia', '<p>A confeiteira prometeu entregar antes de uma cerimônia e apareceu no dia seguinte. Fazer o bolo ainda é possível; o que se perdeu foi a utilidade que dava sentido ao prazo.</p><p>Quando a prestação, por causa da mora, se torna inútil ao credor, ele pode enjeitá-la e exigir perdas e danos (art. 395, parágrafo único). É o inadimplemento definitivo, que abre a porta da resolução.</p>', 'conc'),
    S('p-u2', 'Cumprimento defeituoso', 'Algo foi entregue, mas não o devido', '<p>Há também o cumprimento defeituoso: a prestação veio fora do modo, da quantidade ou da qualidade combinados. Um defeito parcial não resolve o contrato automaticamente; mede-se a sua relevância para o interesse do credor, à luz da boa-fé.</p><p>E quem pede resolução num contrato bilateral não pode ignorar o próprio inadimplemento: a outra parte pode opor a exceção do contrato não cumprido (Aula 07).</p>'),
])
b += chapter('02', 'c2', 'Cláusula expressa ou tácita', 'A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial (art. 474).', 'dif')
b += scrolly('Duas rotas para resolver', [('p-ce0', clause(0), 'Expressa'), ('p-ce1', clause(1), 'Tácita')], [
    S('p-ce0', 'Expressa', '“De pleno direito” não quer dizer em silêncio', '<p>A cláusula expressa descreve, antes do conflito, quais fatos permitem encerrar o vínculo. Quando o fato previsto ocorre, a parte lesada verifica o gatilho, <strong>decide</strong> se quer resolver e <strong>comunica</strong> essa decisão. Não precisa de sentença prévia para a resolução se aperfeiçoar; se houver resistência, pode ir ao Judiciário para obter a restituição e os demais efeitos.</p><p>Essa comunicação não se confunde com o aviso que constitui o devedor em mora quando não há prazo certo (art. 397). E a cláusula não resolve em abstrato se uma falha mínima basta: texto, função do dever e boa-fé pesam.</p>', 'conc'),
    S('p-ce1', 'Tácita', 'Sem cláusula, o juiz decide', '<p>Todo contrato bilateral traz implícita a possibilidade de resolver pelo inadimplemento. Sem cláusula expressa, a resolução depende de interpelação judicial: é na ação que o juiz avalia se o inadimplemento justifica o fim do vínculo.</p>', 'dif'),
])
b += chapter('03', 'c3', 'Resolver ou exigir o cumprimento?', 'A parte lesada pode pedir a resolução, se não preferir exigir o cumprimento, cabendo em qualquer caso indenização por perdas e danos (art. 475).')
b += scrolly('A escolha do art. 475', [('p-fork', fork, 'Art. 475')], [
    S('p-fork', 'Art. 475', 'Uma escolha, não um castigo', '<p>O credor escolhe: resolver ou exigir a prestação. Nos dois caminhos pode pedir perdas e danos, desde que prove o prejuízo e o nexo com o inadimplemento. Indenização não é multa automática.</p><p>Uma gráfica atrasa dois dias a impressão de convites, mas o evento ainda está longe: a cliente pode exigir a entrega e cobrar os custos comprovados. Se os convites chegam depois da festa, a inutilidade pode sustentar a resolução. E se a prestação parcial satisfez o essencial, resolver pode ser desproporcional; exigir complemento ou indenização pode bastar.</p>'),
])
b += chapter('04', 'c4', 'O fim no tempo', 'Resolver pode exigir que as prestações voltem. Isso não é o mesmo que indenizar, e depende do que já foi executado.', 'conc')
b += scrolly('Efeitos da resolução', [('p-ef0', effect(0), 'Restituição'), ('p-ef1', effect(1), 'Contínuos')], [
    S('p-ef0', 'Restituição', 'Voltar ao estado anterior', '<p>Numa venda desfeita, cada parte devolve o que recebeu. Se devolver a própria coisa não for possível, acerta-se o equivalente.</p>', 'conc'),
    S('p-ef1', 'Prestações contínuas', 'O que foi usado não volta', '<p>Numa locação ou num fornecimento contínuo, o que já foi usado ou consumido não pode ser devolvido fisicamente. Identifique o fundamento da extinção, o que foi executado, o que resta e os direitos de terceiros antes de falar em efeito retroativo ou só para o futuro.</p><p>Vale o aviso de nomenclatura da Aula 15: autores diferentes dão nomes diferentes. A duração ajuda a ver o que é restituível, mas não escolhe sozinha o nome nem o efeito.</p>'),
])
b += chapter('05', 'c5', 'Quando a prestação dependia daquela pessoa', 'A morte extingue o vínculo se a identidade ou a habilidade do contratante era essencial à prestação.')
b += wide('<div class="julgados"><article class="julgado conc"><header><b>A cantora</b><span>intuitu personae</span></header><div class="corpo"><p>Uma cantora contratada para uma apresentação em data certa morre antes do show. Seus herdeiros não podem, nem devem, cantar no lugar dela.</p></div><div class="tese">A obrigação era personalíssima, e a morte tornou aquela prestação impossível. Muda tudo se o contrato admitia cumprimento por sucessores, ou se o dever transmitido é patrimonial, como pagar uma quantia.</div></article>'
          '<article class="julgado"><header><b>Caso para resolver</b><span>fornecimento semanal</span></header><div class="corpo"><p>Uma empresa contratou uma fornecedora por dois anos, com entregas semanais. O contrato permite à parte adimplente resolver se três entregas essenciais forem perdidas, mediante comunicação escrita. A fornecedora falha uma semana por problema logístico e propõe reposição antes do uso. Meses depois, perde três entregas seguidas, e os produtos chegam depois da campanha sazonal.</p></div><div class="tese">Na primeira falha, a utilidade continua: cabe exigir a reposição e cobrar prejuízos. Na sequência, confira o gatilho exatamente; a inutilidade para a campanha reforça a perda de interesse. A contratante ainda precisa comunicar por escrito a decisão de resolver. Havendo disputa, o juiz verifica se o gatilho ocorreu e define restituições e danos.</div></article></div>')
b += chapter('06', 'c6', 'Teste')
b += quiz([
    ('Uma máquina chega dois dias atrasada, mas serve para a mesma produção, e o comprador ainda a quer. O próximo passo é pedir resolução?', 'Não. A prestação continua possível e útil: é mora. O comprador pode exigir o cumprimento e, se houver prejuízo provado, perdas e danos.'),
    ('Uma cláusula expressa prevê resolução após três entregas essenciais perdidas. A terceira falha ocorreu. O contrato terminou sozinho?', 'Não. A parte beneficiada confirma o fato previsto, escolhe resolver e comunica a decisão. “De pleno direito” dispensa sentença prévia, não a manifestação.'),
    ('O credor prefere receber a prestação a encerrar o contrato. Perde o direito a perdas e danos?', 'Não. O art. 475 admite perdas e danos em qualquer dos caminhos, provados o prejuízo e o nexo.'),
    ('Um contrato de prestação mensal durou dois anos. Isso basta para dizer que a resolução só terá efeito para o futuro?', 'Não. Verifique o fundamento, o que foi executado e consumido, o que é restituível e o que as partes acertaram.'),
    ('Não há cláusula resolutiva no contrato, e a outra parte descumpriu. Como resolver?', 'Pela cláusula resolutiva tácita, que depende de interpelação judicial (art. 474): o juiz avalia o inadimplemento na ação.'),
])
page('aula-17.html', '17', 'Extinção: inadimplemento e resolução',
     'Extinção dos contratos III: mora e inadimplemento definitivo, interesse útil, cláusula resolutiva expressa e tácita (art. 474), a escolha do art. 475 e os efeitos da resolução.',
     ['Unidade 9 · Extinção', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Mora ou', 'ruptura?',
     'Uma entrega falha. A pergunta decisiva é se o credor ainda pode tirar <strong class="dif">utilidade</strong> do contrato, e qual caminho escolhe para protegê-la: <strong class="conc">resolver</strong> ou exigir.',
     hero, [('Unidade', '9 · Extinção III'), ('Leitura', '≈ 15 min'), ('Antes', 'Aula 16 · Saída por vontade'), ('Depois', 'Revisão da P2')], b,
     ('aula-16.html', '← Aula 16', 'Quando as partes decidem sair'), ('revisao-p2.html', 'Revisão →', 'Revisão para a P2'), unit='9')
