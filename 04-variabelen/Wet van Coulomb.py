#invoer
q_1 = 2.0 * 10**-6
q_2 = 1.0 * 10**-6
r = float(input('afstand= '))
r = r * 10**-2
k =  8.99 * 10**9
#berekening
Fc = ((q_1 * q_2)/r**2) * k

#uitvoer
print(Fc)

