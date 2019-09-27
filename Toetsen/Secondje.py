#invoer

aantal_sec_begin = int(input(' '))

#berekening

aantal_dagen = aantal_sec_begin // (24 * 60 * 60)
aantal_uren = (aantal_sec_begin - aantal_dagen * (24 * 60 * 60)) // (60 * 60)
aantal_min =(aantal_sec_begin - aantal_dagen * (24 * 60 * 60) - aantal_uren * (60 * 60)) // 60
aantal_sec = (aantal_sec_begin - aantal_dagen * (24 * 60 * 60) - aantal_uren * (60 * 60) - aantal_min * 60)

#uitvoer

#print(aantal_dagen,str('d'), aantal_uren, str(':'), aantal_min, str(':'), aantal_sec)
print(str(int(aantal_dagen))+str('d'),str(int(aantal_uren))+str(':')+str(int(aantal_min))+str(':')+str(int(aantal_sec)))
