#invoer
keuze = input('keuze: ')
keuze2= input('keuze: ')

#berekening

if keuze == keuze2:
    einde = 'onbeslist'
elif keuze == 'steen' and keuze2 == 'schaar':
    einde = 'speler 1 wint'
elif keuze == 'schaar' and keuze2 == 'blad':
    einde = 'speler 1 wint'
elif keuze == 'blad' and keuze2 == 'steen':
    einde = 'speler 1 wint'
else:
    einde  = 'speler 2 wint'

print(einde)

