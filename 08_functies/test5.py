from random import randint


def gooi_muntstuk():
    print(a)
    rg = randint(0, 2)
    if rg == 0:
        muntstuk = 'kop'
    else:
        muntstuk = 'munt'
    return muntstuk
a = 4
for i in range(10):
    print(gooi_muntstuk())
#print(rg, muntstuk)
