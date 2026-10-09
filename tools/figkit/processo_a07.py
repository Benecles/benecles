"""Aula 07: read the dated notice and compare the two periods in the 2017 exam."""
from figkit import t, line, svg


def certificate():
    """A source-ordered transcription of the date-bearing lines in the certificate."""
    o = ''
    o += t(40, 38, 'PODER JUDICIÁRIO', size=15, weight=700)
    o += t(40, 62, 'CERTIDÃO', size=18, weight=700, fill='var(--ink)')
    o += line(40, 77, 560, 77, tone='ink', w=1.3)
    o += t(40, 112, 'NOTA Nº 1690/2015 · EDIÇÃO Nº 5561', size=12, weight=700)
    o += t(40, 142, 'DISPONIBILIZADA NO DJE', size=11, fill='var(--ink-2)', weight=600)
    o += t(560, 142, '21/05/2015', size=17, anchor='end', weight=700, fill='var(--conc)')
    o += line(40, 154, 560, 154, tone='muted', w=1)
    o += t(40, 190, 'PUBLICAÇÃO', size=11, fill='var(--ink-2)', weight=600)
    o += t(40, 217, 'no primeiro dia útil que se seguir', size=15, weight=600)
    o += line(40, 231, 560, 231, tone='muted', w=1)
    o += t(40, 269, 'CERTIFICAÇÃO', size=11, fill='var(--ink-2)', weight=600)
    o += t(560, 269, 'PORTO ALEGRE · 22/05/2015', size=15, anchor='end', weight=700, fill='var(--ink)')
    o += line(40, 282, 560, 282, tone='ink', w=1.3)
    return svg('24 15 552 286', o, cls='fig', ident='pci-a07-certificate',
               label='Transcrição em ordem da certidão da Nota 1690/2015: disponibilização no DJE em 21 de maio de 2015, fórmula de publicação no primeiro dia útil seguinte e certificação em Porto Alegre em 22 de maio.')


def doubled_periods():
    """A proportional comparison of the two periods stated in 2017 P1 Q1."""
    x0, scale = 190, 12
    o = t(20, 32, 'P1 · QUESTÃO 1 · 2017', size=13, weight=700)
    o += t(20, 61, 'PRAZOS EM DIAS ÚTEIS', size=11, fill='var(--ink-2)', weight=600)
    o += line(x0, 116, x0 + 30 * scale, 116, tone='muted', w=1.2)
    for i in range(0, 31, 5):
        x = x0 + i * scale
        o += line(x, 108, x, 124, tone='ink', w=1.1)
        o += t(x, 145, str(i), size=10.5, anchor='middle', weight=600)
    o += t(20, 190, 'ODRAUDE', size=13, weight=700, fill='var(--ink)')
    o += line(x0, 185, x0 + 15 * scale, 185, tone='ink', w=9)
    o += line(x0 + 15 * scale, 173, x0 + 15 * scale, 197, tone='ink', w=2)
    o += t(x0 + 15 * scale, 215, '15', size=15, anchor='middle', weight=700)
    o += t(20, 272, 'UFRGS', size=13, weight=700, fill='var(--conc)')
    o += line(x0, 267, x0 + 30 * scale, 267, tone='conc', w=9)
    o += line(x0 + 30 * scale, 255, x0 + 30 * scale, 279, tone='conc', w=2)
    o += t(x0 + 30 * scale, 298, '30', size=15, anchor='middle', weight=700, fill='var(--conc)')
    return svg('12 12 566 300', o, cls='fig', ident='pci-a07-periods',
               label='Escala proporcional de dias úteis na questão 1 da P1 de 2017: 15 para ODRAUDE e 30 para a UFRGS.')


def panels():
    return certificate(), doubled_periods()


def specimen_sections():
    a, b = panels()
    return f'''<section class="ref"><header><span class="g">Documento · ler</span><span class="v">verbo · identificar</span></header>
<h2>Processo · Aula 07 · Certidão de Nota de Expediente</h2>
<p>A transcrição mantém a ordem das inscrições do documento: disponibilização, fórmula de publicação e data da certificação. As marcas tipográficas localizam o que o aluno deve ler.</p>
<p class="r">PCI-A07 · certidão Moodle, p. 1 · fonte no compêndio da aula</p><div class="grid"><div class="s">{a}</div></div></section>
<section class="ref"><header><span class="g">Escala · faixa proporcional</span><span class="v">verbo · comparar</span></header>
<h2>Processo · Aula 07 · P1 de 2017, questão 1</h2>
<p>As extensões levam os próprios prazos à mesma escala; a proporção mostra a duplicação sem converter as datas finais em linhas de texto.</p>
<p class="r">PCI-A07 · exam-2017-2-p1, p. 1, Q1 · CPC arts. 183, 219, 224 e 335</p><div class="grid"><div class="s">{b}</div></div></section>'''
