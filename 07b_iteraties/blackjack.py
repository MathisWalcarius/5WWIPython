

som = 0
while som < 21 :
    kaart = int(input('kaart: '))
    som += kaart
    if kaart == 0:
        break

if som < 21:
    uitvoer= 'Voorzichtig gespeeld ({:d})'
    print(uitvoer.format(som))
elif som == 21:
    uitvoer='gewonnen!'
    print(uitvoer)
else:
    uitvoer= 'Verbrand ({:d})'
    print(uitvoer.format(som))










