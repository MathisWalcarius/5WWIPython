#invoer

t = float(input(' '))
w = float(input(' '))

#berekening

gevoelstemperatuur= 13.12 + 0.6215 * t + ((0.3965 * t) + (-11.37)) * (3.6 * w * 0.277777778)**0.16
#gevoelstemperatuur = 13.12 + 0.6215 * t + 0.3965 * t * pow(3.6 * w, 0.16) - 11.37 * pow(3.6 * w, 0.16)

#uitvoer
print(gevoelstemperatuur)
#13,12+0,6215T+(0,3965T−11,37)(3,6W)0,16
