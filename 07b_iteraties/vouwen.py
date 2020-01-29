dikte = int(input(' dikte: '))

afstand = int(input(' afstand: '))

aantal = 0

while afstand > dikte:
    dikte *= 2
    aantal += 1

uitvoer = 'Na {:d} keer vouwen bedraagt de dikte van het papier {:d} mm.'

print(uitvoer.format(aantal,dikte))


















