ndegetal = int(input('getal: '))


som = 1
voorgaande = 0
#berekening

for i in range(1, ndegetal):
   som += voorgaande
   voorgaande = som - voorgaande


print(som)






