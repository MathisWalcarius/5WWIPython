bj_salaris = round(float(input(' ')),2)


#berekening

rsz = round(bj_salaris - bj_salaris * 0.1307, 2)
schijf1 = 0
schijf2 =0
schijf3 = 0
schijf4 = 0

if rsz <=  13250.00:
    schijf1 = (rsz - 8860) * 0.75
elif rsz > 13250.00 and rsz <=  23390.00:
    schijf1 = 3292.50
    schijf2 = (rsz - 13250) * 0.60
elif rsz > 23390.00 and rsz <=  40480.00:
    schijf1 = 3292.50
    schijf2 = 10140 * 0.75
    schijf3 = (rsz - 23390.00) * 0.55
else:
    schijf1 = 3292.50
    schijf2 = 10140 * 0.75
    schijf3 = 17090 * 0.55
    schijf4 = (rsz - 40480.00) * 50

verheffing = schijf1 + schijf2 + schijf3 + schijf4
netto_jaarsalaris =  rsz - verheffing
netto_maandsalaris = netto_jaarsalaris / 12

#uitvoer

uitvoer1 ='+ bruto jaarsalaris   {:f}'
uitvoer2 = '- rsz                {:f}'
uitvoer3 ='- voorheffing         {:f}'
uitvoer4 = '=============================='
uitvoer5 ='+ netto jaarsalaris   {:f}'
uitvoer6 ='+ netto maandsalaris   {:f}'

print(uitvoer1.format(bj_salaris))
print(uitvoer2.format(rsz))
print(uitvoer3.format(verheffing))
print(uitvoer4)
print(uitvoer1.format(netto_jaarsalaris))
print(uitvoer1.format(netto_maandsalaris))



