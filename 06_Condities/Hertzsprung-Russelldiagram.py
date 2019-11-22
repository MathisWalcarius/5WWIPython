px = float(input('co x-as: '))
py = float(input('co y-as: '))

#berekening

if py > 10000:
    ster = 'superreuzen (a)'
elif py > 1000:
     ster = 'superreuzen (b)'
elif px < 7500 and py > 100:
    ster = 'heldere reuzen'
elif px < 6000 and py > 10:
    ster = 'reuzen'
elif px > 5000 and py < 0.01 or px > 300 and py < 0.0001:
    ster = 'witte dwergen'
else: ster = 'hoofdreeks'

#uitvoer

print(ster)
