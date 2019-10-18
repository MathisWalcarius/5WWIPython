pthuis = int(input('aantal punten thuisploeg: '))
puit = int(input('aantal punten uitploeg: '))
puntenverschil = abs(pthuis - puit)
a = puit

#berekening


if puntenverschil < 10:
    winnaar =+ 600
    verliezer  =+ 400
elif  puntenverschil < 20:
    winnaar =+ 700
    verliezer =+ 300
elif  puntenverschil >= 20:
    winnaar =+ 800
    verliezer =+ 200


if pthuis - puit > 0:
    winnaar = pthuis
    verliezer = puit
else:
    winnaar = puit
    verliezer = pthuis


