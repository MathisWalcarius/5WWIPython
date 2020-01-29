
totalep = 0
prijs = float(input('prijs '))
while prijs != 0:
    totalep += prijs
    prijs = float(input('prijs: '))

uitvoer = 'De totale prijs is € {:.2f}'
print(uitvoer.format(totalep))


