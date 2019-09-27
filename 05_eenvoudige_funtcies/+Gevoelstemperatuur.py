#invoer

T = int(input(' '))
W = int(input(' '))

#berekening

gevoelstemperatuur= 13.12 + 0.6215 * T + ((0.3965 * T) + int(-11.37)) * (3.6 * W)**0.16


#uitvoer
print(gevoelstemperatuur)
