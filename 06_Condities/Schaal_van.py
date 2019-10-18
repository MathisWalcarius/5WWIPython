snelh = int(input('de snelheid: '))

#berekening

if snelh < 119:
    uitvoer ='geen orkaan'
elif snelh <= 153:
    uitvoer ='categorie 1'
elif snelh <= 177:
    uitvoer ='categorie 2'
elif snelh <= 209:
    uitvoer ='categorie 3'
elif snelh <= 249:
    uitvoer ='categorie 4'
else:
    uitvoer ='categorie 5'

#uitvoer

print(uitvoer)
