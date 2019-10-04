#invoer

a = int(input('a = '))
b = int(input('b = '))

#berekening

c = a + b

a2 = a * 10
b2 = b * 10
c2 = a2 + b2

a3 = a * 100
b3 = b * 100
c3 = a3 + b3

a4 = a * 1000
b4 = b * 1000
c4 = a4 + b4

a5 = a * 10000
b5 = b * 10000
c5 = a5 + b5


#uitvoer

uitvoer = '{0:>7d} + {1:<7d} = {2:d}'
print(uitvoer.format(a, b, c))
print(uitvoer.format(a2, b2, c2))
print(uitvoer.format(a3, b3, c3))
print(uitvoer.format(a4, b4, c4))
print(uitvoer.format(a5, b5, c5))
