getal1 = int(input(' '))
getal2 = int(input(' '))
som1, som2 = 0, 0
#berekening

for i in range(1, getal1):
    if getal1 % i == 0:
        som1 += i
for c in range(1, getal2):
    if getal2 % c == 0:
        som2 += c

if som1 == getal2 and som2 == getal1:
    uitvoer = '{:d} en {:d} zijn bevriende getallen'
else:
    uitvoer = '{:d} en {:d} zijn geen bevriende getallen'

print(uitvoer.format(getal1, getal2))

getal1 = int(input(' '))
getal2 = int(input(' '))
som1, som2 = 0, 0
#berekening

for i in range(1, int(getal1/2 + 1)):
    if getal1 % i == 0:
        som1 += i
for c in range(1, int(getal2 / 2 + 1)):
    if getal2 % c == 0:
        som2 += c

if som1 == getal2 and som2 == getal1:
    uitvoer = '{:d} en {:d} zijn bevriende getallen'
else:
    uitvoer = '{:d} en {:d} zijn geen bevriende getallen'

print(uitvoer.format(getal1, getal2))
