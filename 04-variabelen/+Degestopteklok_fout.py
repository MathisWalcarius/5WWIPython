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

#rittijd = (((vertrekuur4 - vertrekuur1) * 60 + ( vertrekmin4 - vertrekmin1)) - ((vertrekuur3 - vertrekuur2) * 60 + ( vertrekmin3 - vertrekmin2))) / 2
#bijnacorrectetijdmin = rittijd % 60 + vertrekmin3
#extrauur = bijnacorrectetijdmin // 60
#correctetijduur = rittijd // 60 + vertrekuur3 + extrauur
#correctetijdmin = bijnacorrectetijdmin % 60

#uitvoer

#print(int(correctetijduur))
#print(int(correctetijdmin))
#print('rittijd', rittijd)


totale_tijd = ((vertrekuur4 - vertrekuur1) * 60) + (vertrekmin4 - vertrekmin1)
tijd_vriendin = (vertrekuur3 - vertrekuur2) * 60 + (vertrekmin3 - vertrekmin2)
rittijd = (totale_tijd - tijd_vriendin) / 2

tijd_min_hulp = (rittijd + vertrekmin3) // 60
tijd_min = (rittijd + vertrekmin3) % 60
tijd_uur = vertrekuur3 + (rittijd // 60) + tijd_min_hulp


print(int(tijd_uur))
print(int(tijd_min))














