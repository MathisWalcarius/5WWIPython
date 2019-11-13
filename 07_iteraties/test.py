naam = input('geef naam: ')
aantal_klinkers = 0
for letter in naam:
    if letter in 'aeuoi' :
        aantal_klinkers += 1
print( aantal_klinkers, len(naam)-aantal_klinkers)



