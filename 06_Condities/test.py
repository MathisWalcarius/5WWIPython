getal = int(input('geef getal: '))

if getal < 0:
    if getal % 2 == 0:
        print('een negatief even getal')
    else:
        print('een negatief onvenen getal')
elif getal > 0: #else if
    if getal % 2 == 0:
        print('een positief even getal')
    else:
        print('een positief onvenen getal')
else:
    print('getal is 0')

print('tot ziens')
