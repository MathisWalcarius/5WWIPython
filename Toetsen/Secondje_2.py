#invoer

aantal_sec_begin = int(input(' '))

#berekening

aantal_dagen = aantal_sec_begin // (24 * 60 * 60)
aantal_uren = (aantal_sec_begin % (24 * 60 * 60)) // 60
aantal_min = aantal_sec_begin % (24 * 60 * 60 * 60) // 60
aantal_sec = aantal_sec_begin % (24 * 60 * 60 * 60 *60)

#uitvoer

print( str(aantal_dagen) +'d',str(aantal_uren) + ':' + str(aantal_min) + ':' + str(aantal_sec))
