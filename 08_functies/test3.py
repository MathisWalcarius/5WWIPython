from math import sqrt

def pythagoras(a, b):
 c = -1
 if a > 0 and b > 0:
    c = sqrt(a*a + b*b)
 return c

print(pythagoras(3,4))
