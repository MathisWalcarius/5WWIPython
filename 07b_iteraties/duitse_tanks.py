getal = int(input(''))

grootst, aantal = 0, 0

while getal > 0:
    if getal > grootst:
        grootst = getal
    aantal += 1
    getal = int(input(' '))
schatting = ((aantal +1) * grootst) / aantal
if round(schatting) == ((aantal +1) * grootst) / aantal:
    schatting -= 1
    schatting =int(schatting)
else:
    schatting = int(((aantal +1) * grootst) / aantal)

uitvoer = 'Het aantal geproduceerde tanks wordt geschat op {:d}.'

print(uitvoer.format(schatting))
