getal = 0
getal = (input(' '))
hitdag = 0
gwndag = 0
while getal != 'stop':
    getal = input((' '))
    if int(getal) <= 30:
        hitdag += 1
    else:
        gwndag += 1
        getal = int(input(''))
        if getal < 30:
            hitdag = 0
    if hitdag == 3:
        uitvoer = 'hittegolf'
    if gwndag ==2:










