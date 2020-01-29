getal = input('getal: ')

som = 0

for letter in getal:
    som += int(letter)

if int(getal) % som == 0:
    uitvoer = '{} is een Harshadgetal'
else:
    uitvoer = '{} is geen Harshadgetal'

print(uitvoer.format(getal))

