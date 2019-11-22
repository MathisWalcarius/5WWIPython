#invoer

r = float(input('r : '))
v = float(input('v : '))
u = 398600.4418 * 10**9
# berekening

a = (u * r ) / (2 * u - r * (v ** 2))

from math import sqrt, pi

p = 2 * pi * sqrt((a ** 3) / u)


p_d = p // 86400
p_u = p % 86400 // 3600
p_m = (p % 86400) % 3600 // 60

print('grote as:',a,'meter')
print('periode:',p,'seconden')
print('periode:',round(p_d),'dagen,',round(p_u),'uren en',round(p_m),'minuten')
