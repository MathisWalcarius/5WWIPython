# invoer

aantal_sol = float(input(' '))

# berekening

#in iedere sol zitten er 88775.244 seconden
aantal_seconden = aantal_sol * 88775.244
aantal_dagen = aantal_seconden // ( 24 * 60 * 60 )
aantal_uren = (aantal_seconden - (aantal_dagen * ( 24 * 60 * 60 ))) // (60 * 60)
aantal_min = ( aantal_seconden - (aantal_dagen * ( 24 * 60 * 60 )) - (aantal_uren * (60 *60))) // 60
aantal_sec = ( aantal_seconden - (aantal_dagen * ( 24 * 60 * 60 )) - (aantal_uren * (60 *60)) - aantal_min * 60)

#uitvoer

print(int(aantal_sol),'sol =', int(aantal_dagen), 'dagen,', int(aantal_uren), 'uren,', int(aantal_min), 'minuten en', int(aantal_sec), 'seconden')

