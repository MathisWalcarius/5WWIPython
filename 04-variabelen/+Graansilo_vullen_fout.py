#invoer

breedte = float(input(' '))
lengte = float(input(' '))
cubiek = float(input(' '))
straal = float(input(' '))
hoogte = float(input(' '))

#berekening


aantal_graan = breedte * lengte * cubiek / 10000
cubiek_silo = straal**2 * 3.14159265358979323846264338327950288419716939937510 * hoogte
aantal_silo = int(aantal_graan / cubiek_silo) + 1

restsilo = aantal_graan % cubiek_silo
hoogte_restsilo = restsilo / (3.14159265358979323846264338327950288419716939937510 * straal**2)



#uitvoer

print(aantal_silo)
print(hoogte_restsilo)

