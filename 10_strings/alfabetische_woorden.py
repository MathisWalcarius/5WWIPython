
def positie_laagste_ascii(woord):
    a = ord(woord[0])
    for letter in woord:
        if ord(letter) < a:
            a = ord(letter)

    return woord.find(chr(a))

def sorteer(woord):
    b = 0
    antwoord = ''
    rest = woord
    for i in range(len(rest)):
        b = positie_laagste_ascii(rest)
        antwoord += rest[b]
        rest = rest[:b]+ rest[(b+1):]
    return antwoord

def is_alfabetisch(woord):
    if sorteer(woord) == woord:
        ant = True
    else:
        ant = False
    return ant
