
getal = int(input('getal: '))
deler = 2
uitkomst= 0
uitvoer = ' '

if getal ==  2 or getal == 3:
    uitvoer = '{:d} is een priemgetal'
elif getal==1:
    uitvoer ='{:d} is geen priemgetal'
else:
    while deler != getal:
        if getal % deler == 0:
            uitvoer = '{:d} is geen priemgetal'
            break
        else:
            deler += 1

if uitvoer == ' ':
    uitvoer = '{:d} is een priemgetal'

print(uitvoer.format(getal))
