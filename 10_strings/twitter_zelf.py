zin = input(' ')

#def twitter(zin):
antwoord  =''
a = 0
for i in range(0, len(zin)):

    if a == 1:
        antwoord += zin[i]
    if zin[i] == '#':
        a = 1
    if zin[i] == ' ' and a == 1:
        a = 0
        antwoord += '\n'

print(antwoord)









