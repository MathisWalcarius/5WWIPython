dag = int(input('dag: '))
maand = int(input('maand: '))
jaar = int(input('jaar: '))

#berekening

if jaar % 400 == 0:
    schrikkeljaar = 'ja'
elif jaar % 4 == 0 and jaar % 100 != 0:
    schrikkeljaar = 'ja'
else: schrikkeljaar = 'nee'



if maand == 12 and dag == 31:
    jaar += 1
    dag = 1
    maand = 1
elif maand == 4 or maand == 6 or maand ==  9 or maand ==  11 and dag == 30:
    maand += 1
    dag = 1
elif maand == 2 and schrikkeljaar== 'ja' and dag == 29:
    maand += 1
    dag = 1
elif maand == 2 and schrikkeljaar== 'nee' and dag == 28:
    maand += 1
    dag = 1
elif maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10  and dag == 31:
    maand += 1
    dag = 1
else:
    dag += 1
    maand = maand
#uitvoer

uitvoer = '{:d}/{:d}/{:d}'

print(uitvoer.format(dag,maand,jaar))
