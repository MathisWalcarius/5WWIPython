#invoer
from math import floor, pi
r_klein = float(input('de straal van de kleine cirkels = '))
r_groot = float(input('de straal van de grote cirkel = '))

#berekening

aantal_kleine_cirkels = floor(0.83 * pow(r_groot, 2) / pow(r_klein, 2) - 1.9)
aantal_procent_bedekt = (pow(r_klein, 2) * pi * aantal_kleine_cirkels / (pow(r_groot, 2) * pi)) * 100

#uitvoer
uitvoer = '{0:d} kleine cirkels bedekken {1:.2f}% van de grote cirkel'
print(uitvoer.format(aantal_kleine_cirkels, aantal_procent_bedekt))

