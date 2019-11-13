pthuis = int(input('aantal punten thuisploeg: '))
puit = int(input('aantal punten uitploeg: '))
puntenverschil = abs(pthuis - puit)


#berekening


if puntenverschil < 10:
    winnaar = 600
    verliezer  = 400
elif  puntenverschil < 20:
    winnaar = 700
    verliezer = 300
else :
    winnaar = 800
    verliezer = 200


if (pthuis - puit) > 0:
    rankingpthuis = winnaar
    rankingpuit = verliezer
else:
    rankingpuit = winnaar
    rankingpthuis = verliezer

thuisploeg = rankingpthuis - 70
uitploeg = rankingpuit + 70

#uitvoerr
uitvoer = '{:.2f}'
print('thuisploeg:',uitvoer.format(thuisploeg))
print('  uitploeg:',uitvoer.format(uitploeg))
