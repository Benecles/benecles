"""Aula 08: real exam docket and contestation selector instruments."""
from figkit import t, line, svg

def docket():
    o=''
    # A real procedural record: dated entries sit on one continuous docket spine.
    o += t(36,32,'AVALIAÇÃO 2 · 31/10/2017 · QUESTÃO 1',size=13,weight=700)
    o += t(36,57,'ARIOVALDO × ODRAUDE E UFRGS',size=18,weight=700)
    o += line(66,95,66,520,w=3)
    entries=[(126,'01/02/2018','Inicial distribuída','Ação de Ariovaldo contra Odraude e UFRGS','ink'),(246,'01/03/2018','Audiência preliminar','Todos presentes · sem conciliação','conc'),(366,'ART. 335, I','Prazo para contestar','Quinze dias; aplicar a contagem já estudada','dif')]
    for y,date,head,detail,tone in entries:
        o += f'<circle cx="66" cy="{y-5}" r="9" style="fill:var(--paper);stroke:var(--{tone});stroke-width:3"/>'
        o += t(105,y-8,date,size=13,fill=f'var(--{tone})',weight=700)
        o += t(330,y-8,head,size=17,weight=700)
        o += t(330,y+22,detail,size=13,fill='var(--ink-2)')
        o += line(105,y+48,1000,y+48,tone='muted',w=1)
    o += t(105,465,'ÚLTIMO DIA · ODRAUDE',size=12,fill='var(--ink-2)',weight=700)
    o += t(330,465,'22/03/2018',size=15,fill='var(--dif)',weight=700)
    o += t(105,500,'ÚLTIMO DIA · UFRGS (PRAZO EM DOBRO)',size=12,fill='var(--ink-2)',weight=700)
    o += t(590,500,'13/04/2018',size=15,fill='var(--dif)',weight=700)
    return svg('20 10 1010 530',o,cls='fig figkit',ident='pci-a08-exam-docket',label='Autos do exame de 2017: audiência sem conciliação em 1 de março de 2018 inicia o prazo de contestação')

def order():
    o=''
    o += t(28,34,'PEÇA DE DEFESA · ORDEM DE LEITURA',size=13,weight=700)
    # One continuous spine and three stage markers retain the sequence without labels.
    o += line(112,122,112,422,tone='ink',w=2.5)
    stages=[(145,'PRELIMINARES · ART. 337','incompetência relativa / convenção de arbitragem','conc'),(278,'MÉRITO','razões de fato e de direito','dif'),(411,'PROVAS','especificação do que se pretende produzir','ink')]
    for y,head,detail,tone in stages:
        o += f'<circle cx="112" cy="{y}" r="13" style="fill:var(--paper);stroke:var(--{tone});stroke-width:3"/>'
        o += t(164,y-8,head,size=14,fill=f'var(--{tone})',weight=700)
        o += t(164,y+22,detail,size=13,fill='var(--ink-2)')
    # The final fork tests the two matters whose initiative is reserved to the party.
    o += line(620,475,875,475,tone='muted',w=1.5)
    o += line(620,475,620,520,tone='conc',w=3)
    o += line(875,475,875,520,tone='ink',w=3)
    o += t(620,455,'INICIATIVA',size=11,fill='var(--ink-2)',weight=700,anchor='middle')
    o += t(620,546,'PARTE · INCOMPETÊNCIA RELATIVA / ARBITRAGEM',size=11,fill='var(--conc)',weight=700,anchor='middle')
    o += t(875,546,'JUIZ · DEMAIS',size=11,fill='var(--ink-2)',weight=600,anchor='middle')
    return svg('18 10 1010 555',o,cls='fig figkit',ident='pci-a08-contestation-order',label='Ordem da contestação: preliminares antes do mérito, fundamentos e provas; arbitragem depende de alegação da parte')

if __name__=='__main__':
 print(docket());print('<!--FIG2-->');print(order())
