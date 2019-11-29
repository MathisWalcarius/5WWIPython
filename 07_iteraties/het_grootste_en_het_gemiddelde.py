aantal = int(input('aantal getallen: '))

#lees het eeste getal voor de lus
getal_0 = int(input('geef getal : '))
som, grootste = getal_0, getal_0

# het eerste getal is onmiddelijk de som en het grootste getal
for i in range(aantal-1):
    getal = int(input('geef getal: '))
    som  += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal

#uitvoer

print('Het grootste getal is {1:d} en het gemiddelde is {0:.2f}'.format(gemiddelde, grootste))







