"""Aula 08: two exam-bank instruments, built with figkit primitives."""
from figkit import t, line, svg

def figures():
    # Q3's real money claim and named co-defendants; the full bar is shared, not divided.
    a=''
    a += t(30,35,'AVALIAÇÃO 2 · 2015 · Q3',size=13,weight=700)
    a += t(30,112,'JESSE VALADÃO',size=12,weight=700)
    a += f'<circle cx="60" cy="160" r="8" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
    a += line(68,160,112,160,w=2)
    a += line(68,160,470,160,w=3,tone='ink')
    a += t(145,125,'R$ 100.000',size=15,weight=700,fill='var(--conc)')
    a += t(130,188,'cobrança solidária',size=11,fill='var(--ink-2)')
    a += line(470,160,520,110,w=2,tone='ink')
    a += line(470,160,520,210,w=2,tone='ink')
    for y,label in [(110,'DALVO FRITZ'),(210,'SEROTONINA DA SILVA')]:
        a += f'<circle cx="520" cy="{y}" r="7" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
        a += t(540,y+5,label,size=11,weight=600)
    a += t(30,250,'UM PEDIDO · DOIS RÉUS',size=12,weight=700,fill='var(--ink-2)')
    claim=svg('20 10 675 260',a,cls='fig',ident='pci-a08-solidary',label='A cobrança solidária de Jesse por cem mil reais contra Dalvo e Serotonina, conforme a questão 3 da Avaliação 2 de 2015')

    # The matched exam's exact date and ordinal sequencing; no invented date for Dalvo's filing.
    b=''
    b += t(34,42,'AVALIAÇÃO 2 · 2015 · Q1',size=13,weight=700)
    b += line(90,157,630,157,w=2)
    xs=[130,335,560]
    for i,x in enumerate(xs):
        tone='var(--ink)' if i<2 else 'var(--dif)'
        b += f'<circle cx="{x}" cy="157" r="9" style="fill:var(--paper);stroke:{tone};stroke-width:3"/>'
    b += t(130,112,'01/04/2015',size=12,weight=700,anchor='middle')
    b += t(130,193,'audiência preliminar',size=12,anchor='middle')
    b += line(335,130,535,130,w=5,tone='conc')
    b += t(435,112,'1ª SEMANA DO PRAZO',size=11,weight=700,anchor='middle',fill='var(--conc)')
    b += t(435,193,'Dalvo contesta',size=12,anchor='middle')
    b += t(560,112,'13/04/2015',size=12,weight=700,anchor='middle',fill='var(--dif)')
    b += t(560,193,'complementa a defesa',size=12,anchor='middle')
    b += t(34,252,'SEROTONINA · SEM DEFESA · SEM ADVOGADO',size=12,weight=700,fill='var(--ink-2)')
    b += t(34,279,'Data da contestação não informada',size=11,fill='var(--ink-2)')
    timeline=svg('20 15 660 290',b,cls='fig',ident='pci-a08-timeline',label='Sequência dos atos e datas expressamente indicados no enunciado da Avaliação 2 de 2015')
    return claim,timeline

if __name__=='__main__':
    print('\n'.join(figures()))
