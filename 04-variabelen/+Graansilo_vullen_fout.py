#invoer

breedte = float(input(' '))
lengte = float(input(' '))
cubiek = float(input(' '))
straal = float(input(' '))
hoogte = float(input(' '))

#berekening


aantal_graan = breedte * lengte * cubiek / 10000
cubiek_silo = straal**2 * 3.141592 * hoogte
aantal_silo = round(aantal_graan / cubiek_silo)
if(aantal_graan / cubiek_silo - int(aantal_graan / cubiek_silo)) < 0.5:
    aantal_silo + 1
    aantal_silo + 0
restsilo = aantal_graan % cubiek_silo
hoogte_restsilo = restsilo / (3.141592 * straal**2)



#uitvoer

print(aantal_silo)
print(hoogte_restsilo)

