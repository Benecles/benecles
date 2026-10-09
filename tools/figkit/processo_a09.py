"""Aula 09 instruments: the 2018 citation record, an objection docket, and scoped acts."""
from figkit import t, line, svg


def citation_record():
    o = t(35, 48, '2018 · Q4 · CITAÇÃO DE FLORINDA', size=14, weight=700)
    o += line(35, 65, 1040, 65, w=1.4)
    o += line(91, 109, 91, 460, w=2)
    entries = [
        (135, '1ª VISITA', 'Florinda não é encontrada', 'oficial suspeita de ocultação e marca hora certa', 'conc'),
        (235, 'DIA SEGUINTE', 'Citação por hora certa', 'mandado cumprido na pessoa da vizinha Valquíria', 'ink'),
        (335, '05 SET.', 'Mandado juntado aos autos', 'citação por hora certa de Florinda', 'ink'),
        (435, '05 SET.', 'Advogado de Florinda comparece', 'constituído após a notícia espalhada por Valquíria', 'dif'),
    ]
    for y, when, title, detail, tone in entries:
        o += line(79, y, 103, y, tone=tone, w=3)
        o += t(125, y-8, when, size=12, fill=f'var(--{tone})', weight=700)
        o += t(310, y-8, title, size=15, weight=700)
        o += t(310, y+18, detail, size=12, fill='var(--ink-2)')
        o += line(125, y+37, 1038, y+37, tone='muted', w=.8)
    o += t(35, 510, 'VERSÃO 1  ·  alternativa d', size=12, fill='var(--dif)', weight=700)
    o += t(540, 510, 'VERSÃO 2  ·  alternativa c', size=12, fill='var(--dif)', weight=700)
    return svg('20 25 1035 510', o, cls='fig', ident='pci-a09-citation-record',
               label='Autos da questão 4 de 2018: primeira diligência sem localizar Florinda, citação por hora certa no dia seguinte, juntada do mandado e comparecimento do advogado em 5 de setembro')


def objection_docket():
    o = t(35, 48, 'AUTOS · ALEGAÇÃO DE NULIDADE', size=14, weight=700)
    o += line(35, 65, 1040, 65, w=1.4)
    o += line(125, 130, 125, 450, w=2)
    o += t(170, 145, 'DEFEITO CONHECIDO', size=12, weight=700)
    o += line(125, 160, 1040, 160, tone='muted', w=1.3)
    o += t(170, 245, 'PRIMEIRA OPORTUNIDADE DE FALAR', size=12, fill='var(--dif)', weight=700)
    o += line(125, 260, 1040, 260, tone='dif', w=3)
    o += t(170, 345, 'ARGUIÇÃO NESTE MOMENTO', size=12, fill='var(--dif)', weight=700)
    o += line(125, 360, 1040, 360, tone='dif', w=3)
    o += t(170, 445, 'ARGUIÇÃO POSTERIOR', size=12, fill='var(--conc)', weight=700)
    o += line(125, 460, 1040, 460, tone='conc', w=3, dash='5 5')
    o += t(1040, 510, 'EXCEÇÕES DO ART. 278 · OFÍCIO / LEGÍTIMO IMPEDIMENTO', size=11, fill='var(--ink-2)', anchor='end', weight=600)
    return svg('20 25 1035 510', o, cls='fig', ident='pci-a09-objection-docket',
               label='Autos em ordem: o art. 278 situa a arguição na primeira oportunidade de manifestação, com as exceções legais')


def dependent_acts():
    o = t(35, 48, 'AUTOS · AgInt no REsp 2.075.558/SP · ORDEM RECORRIDA', size=14, weight=700)
    o += line(35, 65, 1040, 65, w=1.4)
    o += t(45, 105, 'SEQUÊNCIA ESPECIAL · ART. 279', size=12, weight=700)
    o += line(60, 125, 60, 205, tone='ink', w=2)
    o += line(52, 140, 68, 140, tone='dif', w=3)
    o += t(85, 145, '§ 1º · PRIMEIRO LAUDO PERICIAL · fl. 479 (marco indicado)', size=12, fill='var(--dif)', weight=700)
    o += t(85, 169, 'STJ descreve o primeiro laudo à fl. 499', size=11, fill='var(--ink-2)')
    o += line(52, 190, 68, 190, tone='conc', w=3)
    o += t(85, 195, '§ 2º · PGJ ouvida antes da ordem · fls. 1083–1084', size=12, fill='var(--conc)', weight=700)
    o += t(690, 195, 'manifestação não apontou prejuízo concreto', size=11, fill='var(--ink-2)')
    o += line(35, 225, 1040, 225, tone='muted', w=1.2)
    o += t(45, 265, 'DEPOIS · ARTS. 281–283 · ORDEM DO TRIBUNAL DE ORIGEM · fls. 1092–1098', size=12, weight=700)
    o += t(85, 305, 'ATINGIDOS', size=11, fill='var(--conc)', weight=700)
    o += t(235, 305, 'laudo pericial + sentença', size=13, fill='var(--conc)', weight=700)
    o += t(610, 305, 'PRESERVADAS', size=11, fill='var(--dif)', weight=700)
    o += t(780, 305, 'manifestações das partes', size=13, fill='var(--dif)', weight=700)
    o += line(35, 335, 1040, 335, tone='muted', w=1.2)
    o += t(45, 375, 'STJ · ausência do MP, por si só, não demonstrou prejuízo suficiente para nulidade', size=12, weight=700)
    return svg('20 25 1035 400', o, cls='fig', ident='pci-a09-dependent-acts',
               label='Autos do AgInt no REsp 2.075.558 SP: marco da intimação, manifestação da PGJ, atos atingidos pela ordem recorrida e conclusão do STJ')


def panels(): return citation_record(), objection_docket(), dependent_acts()


def specimen_entry():
    figs = panels()
    return ('<section class="ref" id="specimen-pci-a09"><header><span class="g">Autos · citação, alegação, alcance</span><span class="v">verbo · localizar / delimitar</span></header>'
            '<h2>Processo · Aula 09 · nulidades</h2><p>O registro da questão 4 de 2018 localiza o comparecimento; o docket situa a primeira oportunidade; o último instrumento ordena o marco do art. 279, a oitiva e o alcance da ordem no caso julgado pelo STJ.</p>'
            '<div class="wide">' + ''.join(f'<div class="s">{fig}</div>' for fig in figs) + '</div></section>')


if __name__ == '__main__':
    print('\n'.join(panels()))
