aantal = int(input(' '))
uitvoer ='{} is zichtbaar van {:d} meter tot {:d} meter.'
naam1 = input((''))
hoogte1 = int(input(''))
uitvoer1 = '{} is zichtbaar van het gelijkvloers tot {:d} meter.'
print(uitvoer1.format(naam1, hoogte1))
hoogst = hoogte1
for i in range(0,aantal-1):
    naam = (input(''))
    hoogte = int(input(''))
    if hoogte > hoogst:
        print(uitvoer.format(naam,hoogst,hoogte))
        hoogst = hoogte
