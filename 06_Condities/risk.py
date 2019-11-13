a1 = input(int('1ste dobbelsteen: '))
a2 = input(int('2de dobbelsteen: '))
a3 = input(int('3de dobbelsteen: '))

v1 = input(int('1ste dobbelsteen: '))
v2 = input(int('2de dobbelsteen: '))

#berekening

if v1 > v2:
    grootv = v1
    kleinv = v2
else:
    grootv = v2
    kleinv = v1


if a1 > a2 and a2 > a3:
    groota = a1
    middela = a2
elif a1 > a2 and a2 < a3:

