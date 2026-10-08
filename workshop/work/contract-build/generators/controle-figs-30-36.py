"""Scroll-driven figures for Controle Aulas 30–36, inserted after chapter 01."""
import re, sys
import kit
from kit import T, R, P, C, G, box, check, doc, person, lens, coin, scrolly, WARN
D = "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/controle-de-constitucionalidade/"
S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
def node(cx, cy, l, tone='conc', label=None, r=30):
    o = C(cx, cy, r, f'w-{tone} ' + ('ink' if tone == 'grey' else f'c-{tone}'), extra=' stroke-width="2"') + T(cx, cy + 7, l, 't-small' + (f' tc-{tone}' if tone != 'grey' else ''), anchor='middle')
    if label: o += T(cx, cy + r + 20, label, 't-small', anchor='middle')
    return o
def seats(n_on, n_hi, y=150):
    o = ''
    for i in range(11):
        x = 90 + i * 42
        cls = 'f-ink' if i < n_hi else ('w-grey ink' if i < n_on else 'f-paper ink')
        st = 'fill:var(--dif)' if i < n_hi else ('' if i < n_on else 'stroke-dasharray:3 3')
        o += G(C(x, y, 15, cls, style=st), 'pop', d=.05 * i)
    return o

FIG = {}

# ---------------- 30 · ADC
a = (G(box(200, 50, 200, 70, 'LEI FEDERAL', 'presumida válida', 'grey', ctx='30'), 'pop', d=0)
     + P('M260 120L150 190M340 120L450 190', 'ink grow', style='--d:.2s')
     + G(box(40, 196, 220, 90, 'TRIBUNAL A', 'aplica a lei', 'dif', ctx='30') + check(232, 241), 'pop', d=.4)
     + G(box(340, 196, 220, 90, 'TRIBUNAL B', 'afasta a lei', 'conc', ctx='30') + check(532, 241, False), 'pop', d=.6)
     + P('M150 286C150 350 300 330 300 380M450 286C450 350 300 330 300 380', 'c-conc grow', style='--d:.9s')
     + G(R(200, 384, 200, 70, 'f-ink') + T(300, 426, 'ADC NO STF', 't-small t-light', anchor='middle'), 'pop', d=1.2)
     + G(T(300, 520, 'sem controvérsia judicial, não há ADC', 't-hand', anchor='middle'), 'fade', d=1.4))
b = (G(R(40, 60, 170, 70, 'f-ink') + T(125, 102, 'ADC', 't-small t-light', anchor='middle'), 'pop', d=0)
     + P('M210 95H280', 'c-dif grow', style='--d:.2s')
     + G(box(284, 50, 276, 90, 'CAUTELAR', 'maioria absoluta', 'dif', ctx='30'), 'pop', d=.3)
     + G(''.join(doc(60 + i * 36, 200 + i * 10, 110, 130, None, lines=4) for i in range(3)) + T(150, 378, 'PROCESSOS SOBRE A LEI', 't-small', anchor='middle'), 'pop', d=.6)
     + G(R(214, 230, 18, 60, 'f-ink', style='fill:var(--dif)') + R(240, 230, 18, 60, 'f-ink', style='fill:var(--dif)') + T(236, 312, 'suspensos', 't-small tc-dif', anchor='middle'), 'pop', d=.9)
     + G(box(340, 200, 220, 120, 'A LEI', 'continua vigente', 'grey', ctx='30', sub2='a cautelar não a suspende'), 'pop', d=1.1)
     + G(R(40, 430, 520, 70, 'w-conc ink') + T(300, 472, 'JULGAMENTO EM ATÉ 180 DIAS, OU A CAUTELAR PERDE EFICÁCIA', 't-small tc-conc', anchor='middle'), 'pop', d=1.3))
c = (T(40, 70, 'O PLENÁRIO TEM 11 MINISTROS', 't-small', style='letter-spacing:.1em')
     + seats(8, 6) + T(300, 210, '8 presentes para instalar · 6 votos no mesmo sentido para decidir', 't-small', anchor='middle')
     + G(box(40, 260, 250, 110, 'INSTALAÇÃO', 'pelo menos 8', 'grey', ctx='30', sub2='ministros presentes'), 'pop', d=.7)
     + G(box(310, 260, 250, 110, 'DECISÃO', 'pelo menos 6 votos', 'dif', ctx='30', sub2='num ou noutro sentido'), 'pop', d=.9)
     + G(T(300, 450, 'depois de proposta, não há desistência;', 't-hand', anchor='middle') + T(300, 480, 'da decisão, só embargos de declaração', 't-hand', anchor='middle'), 'fade', d=1.2))
d_ = (G(R(220, 50, 160, 70, 'f-ink') + T(300, 92, 'ADC', 't-small t-light', anchor='middle'), 'pop', d=0)
      + P('M260 120C260 180 150 170 150 220', 'c-dif grow', style='--d:.3s') + P('M340 120C340 180 450 170 450 220', 'c-conc grow', style='--d:.3s')
      + G(box(40, 226, 230, 110, 'PROCEDENTE', 'a lei é', 'dif', ctx='30', sub2='constitucional'), 'pop', d=.6)
      + G(box(330, 226, 230, 110, 'IMPROCEDENTE', 'a lei é', 'conc', ctx='30', sub2='inconstitucional'), 'pop', d=.8)
      + G(R(40, 380, 520, 90, 'w-grey ink') + T(300, 418, 'NOS DOIS CASOS', 't-small', anchor='middle') + T(300, 444, 'eficácia contra todos e efeito vinculante', 't-small', anchor='middle'), 'pop', d=1.1)
      + G(T(300, 530, 'ADC e ADI são a mesma pergunta com o sinal trocado', 't-hand', anchor='middle'), 'fade', d=1.3))
FIG['30'] = ('A ADC em quatro tempos', [('q30a', a, 'Controvérsia'), ('q30b', b, 'Cautelar'), ('q30c', c, 'Quórum'), ('q30d', d_, 'Ambivalência')], [
    S('q30a', 'Cabimento', 'A controvérsia é o gatilho', '<p>A ADC só cabe quando decisões judiciais divergem sobre a constitucionalidade de uma lei federal. É a divergência que cria a insegurança que a ação resolve.</p>', 'conc'),
    S('q30b', 'Cautelar', 'Suspende os processos, não a lei', '<p>Por maioria absoluta, o STF pode mandar suspender o julgamento dos processos que envolvem a norma. A lei continua em vigor. O mérito deve ser julgado em até 180 dias.</p>', 'dif'),
    S('q30c', 'Quórum', 'Oito para instalar, seis para decidir', '<p>A sessão exige ao menos oito ministros presentes, e a declaração, seis votos no mesmo sentido.</p>'),
    S('q30d', 'Ambivalência', 'O resultado segue a resposta', '<p>Procedente, a lei é constitucional; improcedente, é inconstitucional. Nos dois casos, a decisão tem eficácia contra todos e efeito vinculante.</p>', 'dif'),
])

# ---------------- 31 · ADO × MI
a = (G(R(200, 50, 200, 110, 'f-paper ink', style='stroke-dasharray:7 5') + T(300, 100, 'A NORMA', 't-small', anchor='middle') + T(300, 122, 'QUE FALTA', 't-small', anchor='middle'), 'pulse')
     + P('M260 160C260 230 140 220 140 280', 'c-dif grow', style='--d:.3s') + P('M340 160C340 230 460 220 460 280', 'c-conc grow', style='--d:.3s')
     + G(box(30, 286, 230, 120, 'ADO', 'a Constituição', 'dif', ctx='31', sub2='deixou de ser cumprida'), 'pop', d=.6)
     + G(box(340, 286, 230, 120, 'MANDADO DE INJUNÇÃO', 'um direito', 'conc', ctx='31', sub2='não pode ser exercido'), 'pop', d=.8)
     + G(T(145, 450, 'processo objetivo', 't-hand', anchor='middle') + T(455, 450, 'quem é titular pede', 't-hand', anchor='middle'), 'fade', d=1.1))
b = (G(box(30, 60, 240, 90, 'LEGITIMADO', 'do art. 103', 'dif', ctx='31'), 'pop', d=0)
     + P('M270 105H330', 'c-dif grow', style='--d:.2s')
     + G(R(334, 60, 236, 90, 'f-ink') + T(452, 110, 'STF RECONHECE A MORA', 't-small t-light', anchor='middle'), 'pop', d=.4)
     + P('M452 150V200', 'c-dif grow', style='--d:.6s')
     + G(box(40, 204, 250, 120, 'PODER LEGISLATIVO', 'recebe ciência', 'grey', ctx='31', sub2='sem prazo automático'), 'pop', d=.8)
     + G(box(310, 204, 250, 120, 'ÓRGÃO ADMINISTRATIVO', 'deve agir em 30 dias', 'dif', ctx='31', sub2='ou prazo razoável'), 'pop', d=1.0)
     + G(T(300, 400, 'a cautelar exige urgência e maioria absoluta', 't-hand', anchor='middle'), 'fade', d=1.2))
c = (person(110, 110, None, 'c-conc')
     + T(110, 250, 'TITULAR', 't-small tc-conc', anchor='middle')
     + P('M150 150H250', 'c-conc grow', style='--d:.2s')
     + G(R(254, 90, 180, 110, 'f-ink') + T(344, 140, 'TRIBUNAL', 't-small t-light', anchor='middle') + T(344, 162, 'reconhece a mora', 't-small t-light', anchor='middle'), 'pop', d=.4)
     + G(box(40, 290, 250, 130, 'FIXA PRAZO', 'e condições para', 'conc', ctx='31', sub2='exercer o direito') + T(54, 402, 'até vir a norma', 't-small'), 'pop', d=.7)
     + G(box(310, 290, 250, 130, 'EFEITO', 'em regra, entre as partes', 'grey', ctx='31', sub2='pode ser estendido') + T(324, 402, 'se for indispensável', 't-small'), 'pop', d=.9)
     + G(T(300, 500, 'não autoriza escrever qualquer política pública', 't-hand', anchor='middle'), 'fade', d=1.2))
d_ = (T(40, 64, 'DIREITO DE GREVE DOS SERVIDORES', 't-small', style='letter-spacing:.1em')
      + G(box(40, 90, 250, 100, 'CF, ART. 37, VII', 'o direito existe; o exercício', 'grey', ctx='31', sub2='depende de lei específica'), 'pop', d=0)
      + G(R(310, 90, 250, 100, 'f-paper ink', style='stroke-dasharray:7 5') + T(435, 146, 'A LEI NÃO VEIO', 't-small', anchor='middle'), 'pop', d=.3)
      + P('M300 190V240', 'c-conc grow', style='--d:.5s')
      + G(box(100, 244, 400, 100, 'MIs 670, 708 E 712', 'o STF reconhece a omissão', 'conc', ctx='31'), 'pop', d=.7)
      + P('M300 344V394', 'c-dif grow', style='--d:.9s')
      + G(box(100, 398, 400, 100, 'LEI 7.783/1989', 'aplicada ao serviço público,', 'dif', ctx='31', sub2='com adaptações'), 'pop', d=1.1))
FIG['31'] = ('Uma omissão, dois caminhos', [('q31a', a, 'Escolha'), ('q31b', b, 'ADO'), ('q31c', c, 'MI'), ('q31d', d_, 'Greve')], [
    S('q31a', 'A escolha', 'O mesmo vazio, perguntas diferentes', '<p>Os dois instrumentos partem da falta de uma norma. A ADO protege a Constituição em si; o mandado de injunção protege quem não consegue exercer um direito por causa da falta.</p>'),
    S('q31b', 'ADO', 'O STF declara a mora', '<p>Um legitimado do art. 103 aponta o comando frustrado. Declarada a omissão, o Poder competente recebe ciência; se a omissão é administrativa, a lei dá 30 dias, salvo prazo razoável maior em situação excepcional.</p>', 'dif'),
    S('q31c', 'Mandado de injunção', 'O tribunal viabiliza o direito', '<p>O titular do direito, ou um legitimado coletivo, impetra contra quem deveria regulamentar. O tribunal reconhece a mora, pode fixar prazo e estabelece as condições para o exercício do direito até que a norma venha.</p>', 'conc'),
    S('q31d', 'Exemplo', 'A greve no serviço público', '<p>Sem a lei prevista no art. 37, VII, o STF reconheceu a omissão nos MIs 670, 708 e 712 e mandou aplicar, com adaptações, a lei de greve do setor privado.</p>'),
])

# ---------------- 32 · ADPF
GATES = [('ATO DO PODER PÚBLICO', 'normativo ou concreto'), ('PRECEITO FUNDAMENTAL', 'lesão ou ameaça direta'), ('SUBSIDIARIEDADE', 'nenhum outro meio eficaz')]
def gates(k):
    o = T(40, 64, 'TRÊS TESTES, TODOS NECESSÁRIOS', 't-small', style='letter-spacing:.1em')
    for i, (g, s) in enumerate(GATES):
        y = 100 + i * 120
        on = i <= k
        o += G(box(120, y, 440, 90, g, s, 'dif' if on else 'grey', ctx='32'), 'pop' if i == k else '', d=.1, extra='' if on else ' opacity=".35"')
        o += R(50, y + 28, 36, 36, 'f-paper ink') + (check(68, y + 46) if on else '')
    if k == 2:
        o += G(R(120, 470, 440, 60, 'f-ink') + T(340, 506, 'CABE ADPF', 't-small t-light', anchor='middle'), 'pop', d=.6)
    return o
f = (T(40, 64, 'O FUNIL', 't-small', style='letter-spacing:.1em')
     + P('M80 90H520L380 300H220Z', 'f-paper ink')
     + G(T(300, 130, 'ADI · ADC · ADO', 't-small', anchor='middle') + T(300, 154, 'resolvem de modo amplo?', 't-small', anchor='middle'), 'pop', d=.2)
     + G(T(300, 250, 'não', 't-hand', anchor='middle'), 'fade', d=.5)
     + P('M300 300V350', 'c-dif grow', style='--d:.6s')
     + G(R(200, 354, 200, 60, 'f-ink', style='fill:var(--dif)') + T(300, 390, 'ADPF', 't-small t-light', anchor='middle'), 'pop', d=.8)
     + G(T(60, 470, 'alcança o que as outras não alcançam:', 't-small') + T(60, 496, '· lei municipal diante da CF', 't-small') + T(60, 520, '· norma anterior a 1988', 't-small') + T(60, 544, '· atos concretos do poder público', 't-small'), 'fade', d=1.0))
dec = (T(40, 64, 'O JULGAMENTO', 't-small', style='letter-spacing:.1em')
       + seats(8, 8)
       + T(300, 210, 'presença de pelo menos dois terços dos ministros', 't-small', anchor='middle')
       + G(box(40, 250, 250, 120, 'CAUTELAR', 'maioria absoluta;', 'grey', ctx='32', sub2='relator, na urgência') + T(54, 352, 'ad referendum do Plenário', 't-small'), 'pop', d=.6)
       + G(box(310, 250, 250, 120, 'MÉRITO', 'eficácia contra todos', 'dif', ctx='32', sub2='e efeito vinculante'), 'pop', d=.8)
       + G(R(40, 410, 520, 70, 'w-conc ink') + T(300, 452, 'MODULAÇÃO: DOIS TERÇOS', 't-small tc-conc', anchor='middle'), 'pop', d=1.0)
       + G(T(300, 540, 'irrecorrível, salvo embargos; sem rescisória', 't-hand', anchor='middle'), 'fade', d=1.2))
FIG['32'] = ('Quando a ADPF cabe', [(f'q32g{k}', gates(k), GATES[k][0]) for k in range(3)] + [('q32f', f, 'Funil'), ('q32d', dec, 'Decisão')], [
    S('q32g0', 'Teste 1', 'Há um ato do poder público?', '<p>A ADPF alcança atos normativos e também atos concretos, administrativos ou judiciais, desde que a controvérsia constitucional se ajuste à sua função.</p>'),
    S('q32g1', 'Teste 2', 'O ato atinge um preceito fundamental?', '<p>Não há lista fechada: princípios fundamentais, direitos e garantias, repartição federativa, organização dos Poderes. É preciso mostrar por que o parâmetro tem essa estatura e como o ato o atinge diretamente.</p>', 'dif'),
    S('q32g2', 'Teste 3', 'Há outro meio eficaz?', '<p>A pergunta não é se existe algum processo, e sim se outro instrumento resolve a controvérsia com alcance e tempo adequados. Se existir, a ADPF não cabe.</p>', 'dif'),
    S('q32f', 'Subsidiariedade', 'O que sobra para a ADPF', '<p>Lei municipal diante da Constituição Federal e norma anterior a 1988 não cabem em ADI no STF. É aí que a ADPF costuma funcionar como rota residual.</p>'),
    S('q32d', 'Julgamento', 'Alcance geral', '<p>O julgamento exige dois terços dos ministros presentes. A decisão de mérito vale contra todos e vincula o poder público; por dois terços, o Tribunal pode modular os efeitos.</p>', 'dif'),
])

# ---------------- 33 · Intervenção
PRIN = ['forma republicana, sistema representativo, regime democrático', 'direitos da pessoa humana', 'autonomia municipal', 'prestação de contas da administração', 'mínimos em educação e saúde']
a = (T(40, 64, 'PRINCÍPIOS SENSÍVEIS · ART. 34, VII', 't-small', style='letter-spacing:.1em')
     + ''.join(G(R(40, 90 + i * 70, 520, 54, 'w-conc ink') + T(60, 123 + i * 70, p, 't-serif'), 'pop', d=.12 * i) for i, p in enumerate(PRIN))
     + G(T(300, 470, 'violado um deles, a União pode intervir', 't-hand', anchor='middle') + T(300, 500, 'no Estado ou no Distrito Federal', 't-hand', anchor='middle'), 'fade', d=.9))
STEPS33 = [('PGR', 'propõe a representação', 'grey'), ('STF', 'julga a violação', 'dif'), ('PRESIDENTE', 'decreta em até 15 dias', 'conc'), ('CONGRESSO', 'aprecia em 24 horas', 'grey')]
def steps33(k):
    o = T(40, 64, 'DUAS ETAPAS: DECIDIR E EXECUTAR', 't-small', style='letter-spacing:.1em')
    for i, (a_, s, tone) in enumerate(STEPS33):
        y = 90 + i * 110
        on = i <= k
        o += G(box(120, y, 440, 84, a_, s, tone if on else 'grey', ctx='33'), 'pop' if i == k else '', d=.1, extra='' if on else ' opacity=".35"')
        o += C(70, y + 42, 18, 'f-ink' if on else 'f-paper ink') + T(70, y + 47, str(i + 1), 't-small' + (' t-light' if on else ''), anchor='middle')
        if i < 3: o += P(f'M70 {y+60}V{y+132}', 'ink' if i < k else 'thin')
    if k == 3:
        o += G(T(340, 560, 'se basta suspender o ato, dispensa o Congresso', 't-small', anchor='middle'), 'fade', d=.4)
    return o
fed = (G(R(200, 60, 200, 70, 'f-ink') + T(300, 102, 'UNIÃO', 't-small t-light', anchor='middle'), 'pop', d=0)
       + P('M300 130V200', 'c-conc grow', style='--d:.2s') + T(314, 172, 'art. 34', 't-small tc-conc')
       + G(R(200, 204, 200, 70, 'w-conc ink') + T(300, 246, 'ESTADO · DF', 't-small tc-conc', anchor='middle'), 'pop', d=.4)
       + P('M300 274V344', 'c-dif grow', style='--d:.6s') + T(314, 316, 'art. 35', 't-small tc-dif')
       + G(R(200, 348, 200, 70, 'w-dif ink') + T(300, 390, 'MUNICÍPIO', 't-small tc-dif', anchor='middle'), 'pop', d=.8)
       + P('M150 95C60 200 60 300 196 383', 'thin dash') + G(T(40, 250, 'a União não', 't-small') + T(40, 270, 'pula o Estado', 't-small') + check(60, 300, False), 'pop', d=1.0)
       + G(T(300, 500, 'medida temporária, limitada ao necessário', 't-hand', anchor='middle'), 'fade', d=1.2))
FIG['33'] = ('A representação interventiva', [('q33a', a, 'Princípios')] + [(f'q33s{k}', steps33(k), STEPS33[k][0]) for k in range(4)] + [('q33f', fed, 'Esferas')], [
    S('q33a', 'Art. 34, VII', 'O que a representação protege', '<p>Os princípios sensíveis: forma republicana, sistema representativo e regime democrático; direitos da pessoa humana; autonomia municipal; prestação de contas; e aplicação dos mínimos constitucionais em educação e saúde. A representação também serve para assegurar a execução de lei federal.</p>', 'conc'),
    S('q33s0', 'Etapa 1', 'O PGR provoca', '<p>O Procurador-Geral da República é o único legitimado. A inicial indica o princípio ou a lei, o ato que produz o conflito e as provas.</p>'),
    S('q33s1', 'Etapa 2', 'O STF verifica a violação', '<p>O Tribunal pede informações e pode buscar uma solução para o conflito. O julgamento exige oito ministros presentes e seis votos. A procedência reconhece o pressuposto jurídico da intervenção; não instala interventor.</p>', 'dif'),
    S('q33s2', 'Etapa 3', 'O Presidente executa', '<p>Recebido o acórdão, o Presidente da República tem até 15 dias para expedir o decreto, com amplitude, prazo, condições e, se preciso, o interventor.</p>', 'conc'),
    S('q33s3', 'Etapa 4', 'O Congresso aprecia', '<p>O decreto vai ao Congresso em 24 horas. Se bastar suspender o ato impugnado, o decreto pode se limitar a isso, e essa apreciação fica dispensada.</p>'),
    S('q33f', 'As esferas', 'Quem intervém em quem', '<p>A União intervém em Estado e no Distrito Federal. Intervenção em município situado em Estado segue a competência estadual e o art. 35. A representação interventiva federal não alcança município diretamente.</p>'),
])

# ---------------- 34 · Técnicas
def strip(k):
    o = T(40, 64, ['COM REDUÇÃO DE TEXTO', 'SEM REDUÇÃO DE TEXTO', 'SEM REDUÇÃO DE TEXTO'][k], 't-small', style='letter-spacing:.1em')
    o += R(40, 100, 520, 80, 'f-paper ink') + T(60, 132, 'benefício a', 't-serif') + T(60, 160, '“servidores efetivos e comissionados”', 't-serif')
    if k == 0:
        o += G(P('M300 154H520', 'c-conc', style='stroke-width:3'), 'pop', d=.4)
        o += G(box(40, 230, 520, 110, 'O TEXTO MUDA', 'o segmento inválido sai; o resto', 'conc', ctx='34', sub2='precisa funcionar sozinho'), 'pop', d=.7)
        o += G(T(300, 420, 'cortar sem reescrever a escolha do legislador', 't-hand', anchor='middle'), 'fade', d=1.0)
    else:
        o += G(box(40, 230, 250, 120, 'SENTIDO A', 'compatível', 'dif', ctx='34', sub2='fica') + check(262, 290), 'pop', d=.4)
        o += G(box(310, 230, 250, 120, 'SENTIDO B', 'incompatível', 'conc', ctx='34', sub2='sai') + check(532, 290, False), 'pop', d=.6)
        lab = ['INTERPRETAÇÃO CONFORME', 'DECLARAÇÃO SEM REDUÇÃO'][k - 1]
        sub = ['qual sentido continua permitido?', 'qual aplicação fica proibida?'][k - 1]
        o += G(R(40, 390, 520, 90, 'f-ink') + T(300, 428, lab, 't-small t-light', anchor='middle') + T(300, 454, sub, 't-small t-light', anchor='middle'), 'pop', d=.9)
    return o
tm = (T(40, 64, 'O TEMPO DOS EFEITOS', 't-small', style='letter-spacing:.1em')
      + P('M50 200H550', 'ink', style='stroke-width:2')
      + G(C(120, 200, 9, 'f-ink') + T(120, 236, 'NORMA', 't-small', anchor='middle'), 'pop', d=.1)
      + G(C(330, 200, 11, 'f-ink', style='fill:var(--conc)') + T(330, 236, 'DECISÃO', 't-small tc-conc', anchor='middle'), 'pop', d=.3)
      + P('M330 180C300 120 160 120 128 180', 'c-conc grow', style='--d:.5s') + T(225, 118, 'regra: retroage', 't-small tc-conc', anchor='middle')
      + G(P('M340 180C380 130 460 130 500 180', 'c-dif', style='stroke-width:3') + T(430, 118, 'modulação', 't-small tc-dif', anchor='middle'), 'pop', d=.8)
      + G(box(40, 290, 250, 130, 'MODULAR', 'dois terços, segurança', 'dif', ctx='34', sub2='jurídica ou interesse social') + T(54, 402, 'precisa ser justificada', 't-small'), 'pop', d=1.0)
      + G(box(310, 290, 250, 130, 'SEM PRONÚNCIA', 'reconhece o vício,', 'mix', ctx='34', sub2='adia a nulidade') + T(324, 402, 'prazo ou apelo ao legislador', 't-small'), 'pop', d=1.2))
FIG['34'] = ('O que a decisão muda', [('q34a', strip(0), 'Texto'), ('q34b', strip(1), 'Sentido'), ('q34c', strip(2), 'Aplicação'), ('q34d', tm, 'Tempo')], [
    S('q34a', 'Com redução de texto', 'Muda o texto', '<p>Se só “e comissionados” viola a Constituição, o tribunal pode retirar esse segmento, desde que o restante continue aplicável sem virar uma regra que o legislador não aprovou.</p>', 'conc'),
    S('q34b', 'Interpretação conforme', 'Muda o sentido', '<p>As palavras ficam. Entre os sentidos plausíveis, o tribunal fica com o compatível com a Constituição. Não pode fabricar um significado que o texto não comporta.</p>', 'dif'),
    S('q34c', 'Sem redução', 'Proíbe uma aplicação', '<p>Na declaração parcial sem redução, o texto também fica, mas certas aplicações ou hipóteses são afastadas. As duas técnicas se aproximam; o dispositivo da decisão deve dizer com precisão o que foi decidido.</p>'),
    S('q34d', 'O tempo', 'Muda quando valem os efeitos', '<p>A regra é a retroatividade. Por dois terços e com justificativa, o STF pode modular. Na declaração sem pronúncia de nulidade, reconhece a incompatibilidade e preserva a norma por um tempo, para evitar um dano maior.</p>'),
])

# ---------------- 35 · Controle estadual
def ladders(k):
    o = ''
    for i, (top, court, objs, tone) in enumerate([('CONSTITUIÇÃO FEDERAL', 'STF · ADI', 'lei federal ou estadual', 'dif'), ('CONSTITUIÇÃO ESTADUAL', 'TJ · ADI ESTADUAL', 'lei estadual ou municipal', 'conc')]):
        x = 40 + i * 290
        on = k == 2 or k == i
        o += G(box(x, 70, 230, 80, top, 'parâmetro', tone if on else 'grey', ctx='35'), 'pop' if on else '', d=.1, extra='' if on else ' opacity=".4"')
        o += P(f'M{x+115} 150V200', 'ink' if on else 'thin')
        o += G(R(x, 204, 230, 70, 'f-ink' if on else 'f-paper ink', style='' if on else 'opacity:.4') + T(x + 115, 246, court, 't-small' + (' t-light' if on else ''), anchor='middle'), 'pop' if on else '', d=.3)
        o += P(f'M{x+115} 274V324', 'ink' if on else 'thin')
        o += G(box(x, 328, 230, 80, 'OBJETO', objs, tone if on else 'grey', ctx='35'), 'pop' if on else '', d=.5, extra='' if on else ' opacity=".4"')
    if k == 2:
        o += G(T(300, 480, 'lei estadual pode enfrentar as duas vias,', 't-hand', anchor='middle') + T(300, 510, 'cada uma com seu parâmetro', 't-hand', anchor='middle'), 'fade', d=.8)
    return o
re_ = (G(R(40, 60, 230, 80, 'f-ink', style='fill:var(--conc)') + T(155, 106, 'TJ DECIDE', 't-small t-light', anchor='middle'), 'pop', d=0)
       + G(box(310, 50, 250, 100, 'NORMA DE', 'reprodução obrigatória', 'conc', ctx='35', sub2='da CF na CE'), 'pop', d=.2)
       + P('M155 140V210', 'c-dif grow', style='--d:.4s') + T(170, 182, 'RE', 't-small tc-dif')
       + G(R(40, 214, 230, 80, 'f-ink', style='fill:var(--dif)') + T(155, 260, 'STF', 't-small t-light', anchor='middle'), 'pop', d=.6)
       + G(box(310, 200, 250, 110, 'REQUISITOS', 'questão federal,', 'grey', ctx='35', sub2='prequestionamento, RG'), 'pop', d=.8)
       + G(box(40, 360, 520, 100, 'TEMA 484', 'TJ pode usar norma federal de reprodução obrigatória', 'dif', ctx='35', sub2='como parâmetro; a decisão pode chegar ao STF por RE'), 'pop', d=1.0)
       + G(T(300, 530, 'o STF examina a questão federal, não refaz a ação', 't-hand', anchor='middle'), 'fade', d=1.2))
FIG['35'] = ('Dois andares de controle abstrato', [('q35a', ladders(0), 'Federal'), ('q35b', ladders(1), 'Estadual'), ('q35c', ladders(2), 'Lado a lado'), ('q35d', re_, 'Recurso')], [
    S('q35a', 'No STF', 'Parâmetro: a Constituição Federal', '<p>A ADI no STF confronta lei ou ato normativo federal ou estadual com a Constituição Federal. Lei municipal diante da Constituição Federal não cabe aqui; pode caber ADPF, com subsidiariedade.</p>', 'dif'),
    S('q35b', 'No TJ', 'Parâmetro: a Constituição estadual', '<p>O art. 125, § 2º, manda os Estados instituírem a ação contra leis ou atos estaduais ou municipais em face da Constituição estadual, julgada pelo Tribunal de Justiça. A Constituição estadual define os legitimados, sem concentrá-los num único órgão.</p>', 'conc'),
    S('q35c', 'Lado a lado', 'A mesma lei, duas perguntas', '<p>Uma lei estadual pode ser atacada no STF diante da Constituição Federal e no TJ diante da estadual. Fixe o parâmetro antes de escolher a ação.</p>'),
    S('q35d', 'O recurso', 'Quando a ação estadual chega ao STF', '<p>Se o TJ decidiu com base em norma da Constituição estadual que reproduz regra federal de observância obrigatória, cabe recurso extraordinário, com os requisitos do RE. A exceção depende da reprodução obrigatória, não de uma cópia qualquer.</p>', 'dif'),
])

# ---------------- 36 · Reserva de plenário
def flow36(k):
    o = G(box(170, 50, 260, 80, 'ÓRGÃO FRACIONÁRIO', 'surge a questão', 'grey', ctx='36'), 'pop', d=0)
    o += P('M300 130V160', 'ink') + P('M150 160H450', 'ink') + P('M150 160V200M450 160V200', 'ink')
    o += G(box(40, 204, 220, 100, 'REJEITA', 'a alegação:', 'dif', ctx='36', sub2='segue julgando'), 'pop' if k == 0 else '', d=.2, extra='' if k in (0, 2) else ' opacity=".35"')
    o += G(box(340, 204, 220, 100, 'ACOLHE', 'a relevância:', 'conc', ctx='36', sub2='remete o incidente'), 'pop' if k == 1 else '', d=.2, extra='' if k in (1, 2) else ' opacity=".35"')
    if k >= 1:
        o += P('M450 304V344', 'c-conc grow', style='--d:.4s')
        o += G(R(300, 348, 260, 90, 'f-ink') + T(430, 386, 'PLENÁRIO OU ÓRGÃO', 't-small t-light', anchor='middle') + T(430, 408, 'ESPECIAL · ART. 97', 't-small t-light', anchor='middle'), 'pop', d=.6)
        o += P('M300 393C200 393 150 360 150 308', 'c-dif grow', style='--d:.9s') + T(150, 440, 'o caso volta', 't-small tc-dif', anchor='middle')
    if k == 2:
        o += G(R(40, 480, 520, 70, 'w-conc ink') + T(300, 512, 'MAIORIA ABSOLUTA DOS MEMBROS', 't-small tc-conc', anchor='middle') + T(300, 534, 'para declarar a inconstitucionalidade', 't-small', anchor='middle'), 'pop', d=1.1)
    return o
exc = (G(box(40, 60, 520, 100, 'JÁ HÁ PRONUNCIAMENTO?', 'do plenário do próprio tribunal ou do STF', 'dif', ctx='36', sub2='sobre a mesma questão'), 'pop', d=0)
       + P('M300 160V200', 'c-dif grow', style='--d:.3s')
       + G(R(160, 204, 280, 60, 'f-ink', style='fill:var(--dif)') + T(300, 240, 'NÃO SE INSTAURA INCIDENTE', 't-small t-light', anchor='middle'), 'pop', d=.5)
       + G(box(40, 320, 520, 130, 'SÚMULA VINCULANTE 10', 'afastar a lei por fundamento constitucional,', 'conc', ctx='36', sub2='sem declarar, também viola o art. 97') + check(530, 360, False), 'pop', d=.8)
       + G(T(300, 520, 'não dá para contornar a reserva pelo nome', 't-hand', anchor='middle'), 'fade', d=1.1))
rg = (T(40, 64, 'REPERCUSSÃO GERAL', 't-small', style='letter-spacing:.1em')
      + seats(11, 8, 130) + T(300, 186, 'recusar exige dois terços dos membros', 't-small', anchor='middle')
      + G(box(40, 230, 250, 110, 'SEM ESSE QUÓRUM', 'a repercussão', 'dif', ctx='36', sub2='é reconhecida'), 'pop', d=.6)
      + G(box(310, 230, 250, 110, 'TESE FIXADA', 'tribunais aplicam', 'grey', ctx='36', sub2='ou se retratam'), 'pop', d=.8)
      + G(R(40, 380, 520, 90, 'w-conc ink') + T(300, 416, 'RECLAMAÇÃO', 't-small tc-conc', anchor='middle') + T(300, 442, 'só após esgotar as instâncias ordinárias', 't-small', anchor='middle'), 'pop', d=1.0)
      + G(T(300, 530, 'o STF não vira terceira instância', 't-hand', anchor='middle'), 'fade', d=1.2))
FIG['36'] = ('A reserva de plenário', [('q36a', flow36(0), 'Rejeita'), ('q36b', flow36(1), 'Acolhe'), ('q36c', flow36(2), 'Art. 97'), ('q36d', exc, 'Exceções'), ('q36e', rg, 'Repercussão geral')], [
    S('q36a', 'Rejeitar', 'A câmara pode rejeitar sozinha', '<p>Se o órgão fracionário rejeita a alegação de inconstitucionalidade, segue julgando. A reserva do art. 97 alcança a declaração, não a simples discussão.</p>', 'dif'),
    S('q36b', 'Acolher', 'Para declarar, remete ao plenário', '<p>Se pretende acolher, o órgão fracionário instaura o incidente (CPC, arts. 948 a 950) e remete a questão ao plenário ou ao órgão especial. Resolvida a questão, o caso volta e é decidido no restante.</p>', 'conc'),
    S('q36c', 'Art. 97', 'O quórum da declaração', '<p>Nos tribunais, só pelo voto da maioria absoluta dos membros do plenário ou do órgão especial se declara a inconstitucionalidade de lei ou ato normativo.</p>'),
    S('q36d', 'Exceções e limites', 'Quando não há incidente, e o que não se pode fazer', '<p>Não se instaura novo incidente se o plenário do tribunal ou o do STF já se pronunciou sobre a mesma questão. E a Súmula Vinculante 10 impede o atalho: afastar a lei por fundamento constitucional, sem declarar, também viola a reserva.</p>', 'conc'),
    S('q36e', 'Repercussão geral', 'O filtro do recurso extraordinário', '<p>Para recusar a repercussão geral, o STF precisa de dois terços dos membros. Fixada a tese, os tribunais aplicam ou se retratam; a reclamação só cabe depois de esgotadas as instâncias ordinárias.</p>', 'dif'),
])

def insert(n):
    title, panels, steps = FIG[n]
    kit.FIGN[0] = 0
    html = scrolly(title, panels, steps)
    if WARN:
        print('\n'.join('  WARN ' + w for w in WARN)); WARN.clear()
    f = D + f'aula-{n}.html'
    s = open(f).read()
    s = re.sub(r'\n<!-- cfig -->.*?<!-- /cfig -->\n', '\n', s, flags=re.S)
    anchor = '<section class="chapter" aria-labelledby="c2">'
    assert anchor in s, n
    s = s.replace(anchor, '<!-- cfig -->\n' + html + '<!-- /cfig -->\n' + anchor, 1)
    open(f, 'w').write(s)
    print('aula', n, 'figure inserted', len(html))

for n in (sys.argv[1:] or FIG.keys()):
    insert(n)
