#invoer

eerste_getal = float(input('eerste willekeurig getal = '))
tweede_getal = float(input('tweede willekeurig getal = '))

#berekening

linkerlid = abs(abs(eerste_getal) - abs(tweede_getal))
rechterlid = abs(eerste_getal - tweede_getal)

#uitvoer
uitvoer = '{0:.4f} \N{LESS-THAN OR EQUAL TO} {1:.4f}'
print(uitvoer.format(linkerlid, rechterlid))

#42.06826283274985 13.510020196930185
