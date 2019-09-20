#invoer

vertrekuur1 = int(input(' '))
vertrekmin1 = int(input(' '))

vertrekuur2 = int(input(' '))
vertrekmin2 = int(input(' '))

vertrekuur3 = int(input(' '))
vertrekmin3 = int(input(' '))

vertrekuur4 = int(input(' '))
vertrekmin4 = int(input(' '))


#berekening

rittijd = ((vertrekuur4 - vertrekuur1) * 60 + ( vertrekmin4 - vertrekmin1)) - ((vertrekuur3 - vertrekuur2) * 60 + ( vertrekmin3 - vertrekmin2)) / 2
correctetijdmin = rittijd % 60 + vertrekmin3
correctetijduur = rittijd // 60 + vertrekuur3
#uitvoer

print(correctetijduur)
print(correctetijdmin)
