e = int(input('# elektronen = '))

# berekening

if e <= 2:
    schil = 'K'
elif 2 < e <= 10:
    schil = 'L'
elif 10 < e <= 28:
    schil = 'M'
elif 28 < e <= 60:
    schil = 'N'
elif 60 < e <= 92:
    schil = 'O'
elif 92 < e <= 124:
    schil = 'P'
else:
    schil = 'Q'

#uitvoer

uitvoer = 'De {}-schil is de buitenste schil van een stabiel atoom met {} elektronen.'
print(uitvoer.format(schil,e))
