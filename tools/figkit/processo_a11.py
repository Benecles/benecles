"""Aula 11: the 2015 P2 party relation and co-litigant answer.

Both panels use the same verified 2015/1 Avaliação 2, question 4 thread.
The first draws the exam's conditional remaining-party relationship; the
second draws its keyed classification. The native HTML docket remains the
reader's general reach instrument.
"""

from figkit import line, svg, t


EXAM_THREAD = "exam-2015-1-avaliacao-2-q4"
SOURCE = "EX, Avaliação 2 2015, questão 4; CPC, Lei 13.105/2015."


def _dot(x, y, tone="ink", r=7, open_=False):
    fill = "var(--paper)" if open_ else f"var(--{tone})"
    return (f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" '
            f'style="fill:{fill};stroke:var(--{tone});stroke-width:2"/>')


def reach_panel():
    """The Q4 collection relation after the hypothesized Dalvo ruling."""
    o = ""
    o += t(24, 37, "2015 · P2 · Q4", size=14, weight=700)
    o += t(376, 37, "R$ 100.000,00", size=11,
           fill="var(--ink-2)", weight=700, anchor="end")
    o += line(24, 54, 376, 54, w=1.4)
    # The collection has one claimant and two solidary defendants. The
    # conditional ruling ends only Dalvo's branch; Serotonina's branch stays
    # open. This is the particular relationship, not the docket's generic test.
    o += t(200, 90, "JESSE VALADÃO", size=13, weight=700,
           anchor="middle")
    o += t(200, 111, "COBRANÇA SOLIDÁRIA", size=11,
           fill="var(--ink-2)", weight=600, anchor="middle")
    o += line(200, 124, 200, 147, w=2)
    o += line(88, 147, 312, 147, w=2)
    o += _dot(88, 147, "conc") + _dot(312, 147, "dif")
    o += t(88, 180, "DALVO", size=12, fill="var(--conc)",
           weight=700, anchor="middle")
    o += t(88, 197, "FRITZ", size=12, fill="var(--conc)",
           weight=700, anchor="middle")
    o += t(312, 180, "SEROTONINA", size=12, fill="var(--dif)",
           weight=700, anchor="middle")
    o += t(312, 197, "DA SILVA", size=12, fill="var(--dif)",
           weight=700, anchor="middle")
    o += line(88, 211, 88, 266, tone="conc", w=3)
    o += line(312, 211, 312, 310, tone="dif", w=3)
    o += line(79, 258, 97, 276, tone="conc", w=2.5)
    o += line(79, 276, 97, 258, tone="conc", w=2.5)
    o += _dot(312, 310, "dif", open_=True)
    o += t(88, 301, "SE ILEGÍTIMO", size=11, fill="var(--conc)",
           weight=700, anchor="middle")
    o += t(312, 340, "DEMANDA SEGUE", size=11, fill="var(--dif)",
           weight=700, anchor="middle")
    return svg("10 10 380 345", o, cls="fig", ident="pci-a11-reach",
               label="Na questão 4 da P2 de 2015, Jesse Valadão cobra solidariamente cem mil reais de Dalvo Fritz e Serotonina da Silva. Se Dalvo for declarado parte ilegítima, a demanda segue contra Serotonina")


def co_litigants_panel():
    """Two separate procedural tracks for the exam's solidary debtors."""
    o = ""
    o += t(24, 37, "2015 · P2 · Q4", size=14, weight=700)
    o += t(376, 37, "DOIS RÉUS", size=11,
           fill="var(--ink-2)", weight=700, anchor="end")
    o += line(24, 54, 376, 54, w=1.4)
    o += t(200, 92, "COBRANÇA SOLIDÁRIA", size=13,
           weight=700, anchor="middle")
    o += line(200, 105, 200, 130, w=2)
    o += line(105, 130, 295, 130, w=2)
    o += _dot(105, 130, "conc") + _dot(295, 130, "dif")
    # Two tracks retain their own baselines and open ends. Deleting the labels
    # still leaves one shared demand with two independent positions.
    for x, name, tone in [(105, "DALVO", "conc"),
                          (295, "SEROTONINA", "dif")]:
        o += line(x, 137, x, 272, tone=tone, w=3)
        o += _dot(x, 272, tone, open_=True)
        label_x = x + 15 if x < 200 else x - 15
        o += t(label_x, 174, name, size=12, fill=f"var(--{tone})",
               weight=700, anchor="start" if x < 200 else "end")
        o += t(x, 300, "posição própria", size=11,
               fill=f"var(--{tone})", anchor="middle", weight=600)
    o += line(24, 330, 376, 330, tone="ink", w=1)
    o += t(200, 356, "SIMPLES · FACULTATIVO", size=12,
           weight=700, anchor="middle")
    o += t(200, 376, "POSIÇÕES AUTÔNOMAS", size=12,
           weight=700, anchor="middle")
    return svg("10 10 380 380", o, cls="fig", ident="pci-a11-collitigants",
               label="Na questão 4 da P2 de 2015, a cobrança solidária envolve Dalvo e Serotonina; o gabarito classifica o litisconsórcio como simples e facultativo, com posições processuais autônomas")


def panels():
    return reach_panel(), co_litigants_panel()


def specimen_sections():
    a, b = panels()
    return f'''<section class="ref" data-exam-thread="{EXAM_THREAD}"><header><span class="g">Autos · relação remanescente</span><span class="v">verbo · localizar</span></header>
<h2>Processo · Aula 11 · cobrança e partes</h2><p>Na hipótese de ilegitimidade de Dalvo, a cobrança proposta por Jesse segue quanto a Serotonina.</p><p class="r">thread · {EXAM_THREAD}</p><div class="grid"><div class="s">{a}</div></div></section>
<section class="ref" data-exam-thread="{EXAM_THREAD}"><header><span class="g">Autos · posições</span><span class="v">verbo · comparar</span></header>
<h2>Processo · Aula 11 · dois devedores</h2><p>A resposta da P2 de 2015 classifica os dois devedores solidários como litisconsortes simples e facultativos, com posições processuais autônomas.</p><p class="r">thread · {EXAM_THREAD}</p><div class="grid"><div class="s">{b}</div></div></section>'''
