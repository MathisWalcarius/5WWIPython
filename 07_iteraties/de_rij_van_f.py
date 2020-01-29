som, voorgaande = 1,0
getal = int(input(' '))
for i in range(1, getal):
   som += voorgaande
   voorgaande = som - voorgaande
print(som)

