from kit import *

# hero: a seat changes hands; the other party signs off
hero = ('<path class="draw" d="M300 85H780" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:.3s"><circle cx="820" cy="85" r="32" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:2"/><text x="820" y="92" text-anchor="middle" style="font:600 18px var(--sans);fill:var(--dif)">C</text></g>'
        '<g class="pop" style="--d:.5s;opacity:.45"><circle cx="160" cy="45" r="26" style="fill:var(--paper);stroke:var(--ink);stroke-width:2;stroke-dasharray:5 4"/><text x="160" y="51" text-anchor="middle" style="font:600 16px var(--sans);fill:var(--ink)">A</text></g>'
        '<path class="draw" style="--d:.9s;stroke:var(--conc);stroke-width:2.5;fill:none" d="M150 140C200 140 230 100 262 90"/>'
        '<g class="pop" style="--d:1.2s"><circle cx="264" cy="85" r="32" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/><text x="264" y="92" text-anchor="middle" style="font:600 18px var(--sans);fill:var(--conc)">B</text></g>'
        '<g class="pop" style="--d:1.6s"><path d="M860 60l8 9l14 -18" style="stroke:var(--dif);stroke-width:3.5;fill:none;stroke-linecap:round"/></g>'
        '<g class="pop" style="--d:1.7s;font:12px var(--mono);letter-spacing:1px"><text x="200" y="30" style="fill:var(--ink)">CEDENTE SAI</text>'
        '<text x="264" y="148" text-anchor="middle" style="fill:var(--conc)">CESSIONÁRIO ENTRA</text><text x="820" y="148" text-anchor="middle" style="fill:var(--dif)">CEDIDO CONSENTE</text></g>')

def node(cx, cy, l, tone='conc', label=None, r=32, ghost=False):
    if ghost:
        o = C(cx, cy, r, 'f-paper ink', style='stroke-dasharray:5 4;opacity:.5') + T(cx, cy + 8, l, 't-mid', anchor='middle', style='opacity:.5')
    else:
        o = C(cx, cy, r, f'w-{tone} ' + ('ink' if tone == 'grey' else f'c-{tone}'), extra=' stroke-width="2"') + T(cx, cy + 8, l, f't-mid tc-{tone}', anchor='middle')
    if label: o += T(cx, cy + r + 22, label, 't-small', anchor='middle', style='opacity:.5' if ghost else '')
    return o

# ---- Fig 1: the three-party swap
def swap(k):
    o = T(40, 60, 'LOCAÇÃO COMERCIAL EM ANDAMENTO', 't-small', style='letter-spacing:.1em')
    A, B, Cc = (130, 170), (130, 400), (470, 170)
    if k == 0:
        o += P('M166 170H434', 'ink', style='stroke-width:3') + T(300, 156, 'CONTRATO-BASE', 't-small', anchor='middle')
        o += G(node(*A, 'A', 'conc', 'ANA · LOCATÁRIA'), 'pop', d=.1) + G(node(*Cc, 'C', 'dif', 'CAIO · LOCADOR'), 'pop', d=.3)
        o += G(node(*B, 'B', 'grey', 'BRUNO · QUER ENTRAR'), 'pop', d=.6)
    elif k == 1:
        o += P('M166 170H434', 'ink', style='stroke-width:3')
        o += node(*A, 'A', 'conc', 'CEDENTE') + node(*Cc, 'C', 'dif', 'CEDIDO') + node(*B, 'B', 'conc', 'CESSIONÁRIO')
        o += P('M130 206V364', 'c-conc grow', style='stroke-width:3') + G(R(150, 260, 170, 50, 'w-conc ink') + T(235, 290, 'ACORDO DE CESSÃO', 't-small tc-conc', anchor='middle'), 'pop', d=.5)
        o += G(T(470, 300, 'Caio ainda', 't-hand', anchor='middle') + T(470, 330, 'não disse nada', 't-hand', anchor='middle'), 'fade', d=.9)
    else:
        o += node(*A, 'A', label='ANA SAI', ghost=True) + node(*Cc, 'C', 'dif', 'CEDIDO')
        o += P('M162 390L438 186', 'ink grow', style='stroke-width:3') + G(node(*B, 'B', 'conc', 'NOVO LOCATÁRIO'), 'pop', d=0)
        o += G(C(520, 120, 18, 'w-dif ink') + check(520, 120), 'pop', d=.6)
        o += G(T(560, 90, 'CONSENTE', 't-small tc-dif', anchor='end'), 'pop', d=.7)
        o += G(box(40, 480, 520, 80, 'A POSIÇÃO INTEIRA MUDOU DE MÃOS', 'direitos, deveres, poderes e encargos do lado de Ana', 'conc', ctx='swap'), 'pop', d=1.0)
    return o
def release(k):
    o = T(40, 60, 'E ANA? LIBERADA OU NÃO?', 't-small', style='letter-spacing:.1em')
    o += node(470, 150, 'C', 'dif', 'CEDIDO') + node(130, 150, 'B', 'conc', 'CESSIONÁRIO') + P('M166 150H434', 'ink', style='stroke-width:3')
    if k == 0:
        o += G(node(300, 330, 'A', label='ANA LIBERADA', ghost=True), 'pop', d=.3)
        o += G(box(40, 440, 520, 100, 'SE CAIO ACEITOU LIBERAR', 'Ana não responde pelo que vier depois', 'dif', ctx='rel'), 'pop', d=.7)
    else:
        o += G(node(300, 330, 'A', 'grey', 'ANA · SUBSIDIÁRIA'), 'pop', d=.3)
        o += P('M300 294V190', 'c-conc grow', style='stroke-dasharray:6 5;--d:.5s') + T(310, 250, 'garante', 't-small tc-conc')
        o += G(box(40, 440, 520, 100, 'SE CAIO CONDICIONOU', 'Ana continua respondendo subsidiariamente;', 'conc', ctx='rel', sub2='solidariedade não nasce da cessão sozinha'), 'pop', d=.7)
    return o

# ---- Fig 2: what exactly was transferred?
def moved(k):
    o = T(40, 60, ['CESSÃO DE CRÉDITO · ARTS. 286–298', 'ASSUNÇÃO DE DÍVIDA · ARTS. 299–303', 'CESSÃO DA POSIÇÃO'][k], 't-small', style='letter-spacing:.1em')
    o += R(60, 100, 220, 260, 'f-paper ink') + T(170, 128, 'POSIÇÃO DE UMA PARTE', 't-small', anchor='middle')
    items = [('CRÉDITOS', 'dif'), ('DÍVIDAS', 'conc'), ('PODERES', 'grey'), ('ENCARGOS', 'grey')]
    moving = {0: [0], 1: [1], 2: [0, 1, 2, 3]}[k]
    for i, (lab, tone) in enumerate(items):
        y = 150 + i * 50
        if i in moving:
            o += R(80, y, 180, 36, 'f-paper ink', style='stroke-dasharray:4 4;opacity:.5')
            o += G(R(340, y, 180, 36, f'w-{tone} ink') + T(430, y + 23, lab, 't-small' + (f' tc-{tone}' if tone != 'grey' else ''), anchor='middle'), 'pop', d=.3 + .12 * i)
            o += P(f'M262 {y+18}H336', 'thin grow', style=f'--d:{.2+.12*i}s')
        else:
            o += R(80, y, 180, 36, f'w-{tone} ink') + T(170, y + 23, lab, 't-small', anchor='middle')
    o += R(320, 100, 220, 260, 'f-paper ink', style='fill:none;stroke-dasharray:6 5') + T(430, 128, 'QUEM RECEBE', 't-small', anchor='middle')
    notes = [('notificar o devedor', 'para valer contra ele (art. 290)', 'dif'),
             ('consentimento expresso do credor', 'silêncio após prazo = recusa (art. 299)', 'conc'),
             ('consentimento do cedido', 'o cedente só sai se isso for acertado', 'mix')][k]
    o += G(box(40, 400, 520, 100, notes[0].upper(), notes[1], notes[2], ctx='mv'), 'pop', d=.9)
    o += T(300, 550, ['o credor original continua parte', 'o lado ativo não se move', 'o lado inteiro se move'][k], 't-hand', anchor='middle')
    return o

# ---- Fig 3: scope of the leasing transfer
lease = (T(40, 60, 'REsp 356.383/SP · LEASING', 't-small', style='letter-spacing:.1em')
         + P('M60 250H540', 'ink', style='stroke-width:2')
         + ''.join(C(80 + i * 40, 250, 7, 'f-ink' if i < 7 else 'f-paper ink') for i in range(12))
         + G(C(360, 250, 12, 'f-ink', style='fill:var(--conc)') + T(360, 290, 'CESSÃO', 't-small tc-conc', anchor='middle'), 'pop', d=.2)
         + T(200, 230, 'parcelas já pagas', 't-small', anchor='middle') + T(460, 230, 'futuras', 't-small', anchor='middle')
         + P('M360 200C300 140 150 140 80 200', 'c-dif grow', m='p-lease-d', style='--d:.6s')
         + G(T(220, 130, 'o instrumento alcançava', 't-hand', anchor='middle') + T(220, 105, 'direitos anteriores, atuais e futuros', 't-small tc-dif', anchor='middle'), 'fade', d=1)
         + G(box(40, 360, 520, 110, 'LEGITIMIDADE RECONHECIDA', 'a sucessora pôde discutir as parcelas', 'dif', ctx='lease', sub2='pagas pela empresa anterior'), 'pop', d=1.3)
         + T(300, 530, 'decidiu o alcance daquela cessão, não de toda cessão', 't-hand', anchor='middle'))

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo">{corpo}</div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'A troca envolve três pessoas', 'Quem sai combina com quem entra. Mas o contrato tem um outro lado, e ele também precisa aceitar a troca.', 'conc')
b += scrolly('A posição muda de mãos', [('p-sw0', swap(0), 'Contrato-base'), ('p-sw1', swap(1), 'Acordo'), ('p-sw2', swap(2), 'Consentimento'), ('p-rl0', release(0), 'Liberação'), ('p-rl1', release(1), 'Subsidiária')], [
    S('p-sw0', 'O cenário', 'Ana quer sair, Bruno quer entrar', '<p>Numa locação comercial em andamento, Ana é a locatária. Ela quer transferir a Bruno o seu lugar no contrato. Caio, o locador, vai continuar na relação e passará a tratar com Bruno.</p>'),
    S('p-sw1', 'Cedente e cessionário', 'O acordo de cessão', '<p>Ana (<strong>cedente</strong>) e Bruno (<strong>cessionário</strong>) assinam o acordo que põe Bruno no lugar de Ana. O contrato original continua servindo de base.</p><p>Mas Caio não é um espectador que só precisa ser avisado: ele vai passar a exigir de Bruno os deveres do contrato e a reconhecer a Bruno os direitos correspondentes.</p>', 'conc'),
    S('p-sw2', 'O cedido', 'O consentimento completa a substituição', '<p>A anuência de Caio (<strong>cedido</strong>) completa a troca. Pode vir antes (numa cláusula que autoriza a transferência sob condições), junto com o acordo, ou depois, inclusive por conduta que mostre sem dúvida que ele passou a tratar com Bruno.</p><p>O que se transfere é a <strong>posição contratual</strong>: o conjunto de direitos, deveres, poderes e encargos do lado de Ana. Não um crédito isolado, nem uma dívida isolada.</p>', 'dif'),
    S('p-rl0', 'Liberação', 'Ana pode ficar livre', '<p>Se Caio aceitou a substituição liberando Ana, ela não responde pelo que vier depois.</p>'),
    S('p-rl1', 'Ou não', 'Substituir não é o mesmo que liberar', '<p>Caio pode aceitar Bruno com a condição de que Ana continue respondendo subsidiariamente. A substituição e a liberação do cedente são perguntas relacionadas, mas separadas. E solidariedade não nasce automaticamente da cessão.</p><p>Garantias também pedem análise à parte. Na assunção de dívida, as garantias especiais dadas pelo devedor original se extinguem, salvo assentimento expresso dele (art. 300); garantias de terceiros dependem do consentimento de quem as prestou. A cessão não basta para presumir que continuam.</p>', 'conc'),
])
b += chapter('02', 'c2', 'Descubra o que foi transferido', 'O nome “cessão” não resolve tudo. Mudou um crédito, uma dívida ou a posição inteira?', 'dif')
b += scrolly('Crédito, dívida ou posição', [(f'p-mv{k}', moved(k), l) for k, l in enumerate(['Crédito', 'Dívida', 'Posição'])], [
    S('p-mv0', 'Arts. 286 a 298', 'Cessão de crédito', '<p>O credor transfere um crédito, com seus acessórios, salvo ajuste diferente. Para valer contra o devedor, a cessão precisa ser notificada a ele (art. 290). O credor original continua sendo parte do contrato de origem.</p><p>Se Caio cede a uma empresa apenas os aluguéis que tem a receber, continua locador; Ana continua locatária, e só precisa ser notificada.</p>', 'dif'),
    S('p-mv1', 'Arts. 299 a 303', 'Assunção de dívida', '<p>Um terceiro assume a obrigação do devedor, com consentimento <strong>expresso</strong> do credor (art. 299). Se o credor for chamado a consentir num prazo e ficar calado, o silêncio vale como recusa.</p><p>Só o lado passivo se move. Assumir uma dívida de Ana não torna Bruno titular dos direitos dela.</p>', 'conc'),
    S('p-mv2', 'Cessão da posição', 'O lado inteiro se move', '<p>Na cessão da posição contratual, o contratante transfere todo o seu lado do vínculo. Não há no Código Civil um artigo geral que a regule; o STJ exige a anuência do cedido e destaca que ele pode avaliar o risco de inadimplência do novo contratante.</p><p>Não há regra geral que transforme silêncio em consentimento. Saber da negociação não é aceitar a troca.</p>'),
])
b += chapter('03', 'c3', 'O que o acordo alcança', 'O instrumento de cessão diz até onde a nova posição vai: créditos, deveres, garantias, pretensões sobre o passado.')
b += scrolly('O alcance da cessão', [('p-lease', lease, 'Leasing')], [
    S('p-lease', 'REsp 356.383/SP · 3ª Turma · 2002', 'A sucessora pode discutir o passado?', '<p>Uma empresa sucedeu outra como arrendatária num contrato de leasing, com participação da arrendadora. A sucessora quis revisar também parcelas que a antecessora já tinha pago.</p><p>O STJ reconheceu a legitimidade: naquele acordo, a transferência incluía créditos e débitos e abrangia direitos e obrigações anteriores, atuais e futuros. O que decidiu foi o <strong>alcance do instrumento</strong>. Não disse que toda cessão transfere automaticamente as pretensões passadas do cedente.</p>', 'dif'),
])
b += wide('<div class="julgados">'
          + jul('', 'Arrendamento residencial', 'REsp 1.950.000/SP · 2022',
                '<p>A transferência de um imóvel do Programa de Arrendamento Residencial dependia dos requisitos de ingresso no programa e da anuência da CEF. Os sucessores não preenchiam os requisitos.</p>',
                'O STJ não permitiu que a CEF dispensasse requisitos do programa. O regime especial do contrato pesou tanto quanto a anuência: o resultado não substitui a análise de cada contrato.')
          + '</div>')
b += chapter('04', 'c4', 'É mesmo cessão?', 'Três figuras parecidas, três estruturas diferentes.')
b += wide(table(['', 'Quando', 'O que acontece'], [
    ['Pessoa a declarar', 'Na formação do contrato.', 'Uma parte reserva o direito de indicar quem ocupará a posição prevista no próprio acordo (Aula 06). Não é troca posterior de contratante.'],
    ['Subcontrato', 'Durante a execução.', 'Uma parte contrata um terceiro para executar algo ligado ao contrato principal. Em regra, continua responsável perante a outra parte.'],
    ['Cessão da posição', 'Durante a execução.', 'O novo contratante entra no vínculo existente e ocupa a posição transferida, com o consentimento do cedido.'],
]) + '<p class="note">Pergunta de controle: quem continua sendo a contraparte, e quais direitos e deveres entraram de fato na transferência?</p>')
b += chapter('05', 'c5', 'Teste')
b += quiz([
    ('O locador Caio cede a uma empresa só os aluguéis que tem a receber de Ana. A cessionária precisa do consentimento de Ana?', 'Não. É cessão de crédito, não substituição contratual. Ana precisa ser notificada para que a cessão valha contra ela (art. 290). Caio continua locador.'),
    ('Ana e Bruno assinam a transferência e avisam Caio. Caio não responde. A cessão está completa?', 'Não dá para concluir isso pelo aviso e pelo silêncio. A substituição exige o consentimento do cedido, e não há regra geral que faça o silêncio valer como consentimento.'),
    ('O instrumento diz que Bruno assume a posição e inclui os créditos sobre parcelas pagas por Ana. O que ensina o REsp 356.383/SP?', 'Que o alcance expressamente pactuado pode dar ao cessionário legitimidade para discutir parcelas anteriores. Não é regra automática para cessões com escopo diferente.'),
    ('Caio aceitou Bruno como locatário. Ana está livre de toda responsabilidade futura?', 'Não necessariamente. Substituir e liberar são coisas distintas; Caio pode ter condicionado a aceitação à responsabilidade subsidiária de Ana.'),
    ('Uma empresa terceiriza parte da obra que contratou. A contratante da obra passou a ter um novo contratante?', 'Não. Isso é subcontrato: a empresa original continua responsável perante a contratante.'),
])
page('aula-14.html', '14', 'Cessão da posição contratual',
     'Cessão da posição contratual: cedente, cessionário e cedido; consentimento; cessão de crédito e assunção de dívida; alcance da transferência.',
     ['Unidade 8 · Cessão da posição contratual', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Quem entra', 'no contrato?',
     'Numa locação em andamento, a locatária quer sair e outra pessoa quer assumir seu lugar. O que precisa acontecer para o <strong class="dif">locador</strong> tratar com o <strong class="conc">novo locatário</strong>, e a antiga deixar de responder?',
     hero, [('Unidade', '8 · Cessão'), ('Leitura', '≈ 15 min'), ('Antes', 'Aula 13 · Base do negócio'), ('Depois', 'Aula 15 · Extinção')], b,
     ('aula-13.html', '← Aula 13', 'A base comum do negócio'), ('aula-15.html', 'Aula 15 →', 'Qual evento extingue a obrigação?'), unit='8')
