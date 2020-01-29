aantal = int(input(' '))
soorta = ''
soortt = ''
soortg = ''
soortc = ''
a,t,g,c = 0,0,0,0

for i in range (0,aantal):
    x = input('')
    if x == 'A':
        a = 1
        soorta = 'A'
    elif x == 'T':
        t = 1
        soortt= 'T'
    elif x == 'G':
        g = 1
        soortg = 'G'
    else:
        c = 1
        soortc = 'C'
som = a+t+g+c
soort = soorta + soortt + soortg + soortc

uitvoer ='De DNA-keting bevat {} soort base: {} '
uitvoer2='De DNA-keting bevat {} verschillende soorten basen: {} '

if som == 1:
    print('De DNA-keting bevat',som,'soort base:',soort)
else:
    print('De DNA-keting bevat',som,'verschillende soorten basen:', soorta , soortc , soortg , soortt)











