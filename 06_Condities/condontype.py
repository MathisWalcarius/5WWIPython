rna = input('soort type: ')

#berekening

if rna == 'AUG':
    typecondon = 'start'
elif len(rna) != 3:
    typecondon = 'ongeldig'
elif rna == 'UAG' or rna == 'UGA' or rna == 'UAA':
    typecondon = 'stop'
else:
    typecondon = 'gewoon'

#uitvoer

uitvoer = 'Het codon {} is een {} codon.'

print(uitvoer.format(rna,typecondon))

