a1 = int(input('1ste dobbelsteen: '))
a2 = int(input('2de dobbelsteen: '))
a3 = int(input('3de dobbelsteen: '))

v1 = int(input('1ste dobbelsteen: '))
v2 = int(input('2de dobbelsteen: '))

#berekening
legers_a = 2
legers_v = 2
tweede_a = (a1 + a2 + a3 ) - min(a1, a2, a3 ) - max(a1, a2, a3 )

if max(v1, v2) >= max(a1,a2,a3):
    legers_v -= 1
else:
    legers_a -= 1

if min(v2,v1) >= tweede_a:
    legers_v -= 1
else:
    legers_a -= 1

if legers_v == 1:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')
else:
    print('aanvaller verliest', legers_a,' legers, verdediger verliest', legers_v,'legers')

print(tweede_a)
