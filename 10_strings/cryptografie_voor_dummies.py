


def versleutel_woord(woord,getal):
    nieuwwoord = ''
    for i in range(len(woord)):
        if woord[i] == '@':
            nieuwwoord += ' '
        else:
            nieuwwoord += chr(ord(woord[i].upper()) + getal)
    return nieuwwoord

def versleutel_zin(woord, getal):
    nieuwwoord = ''
    for i in range(len(woord)):
        b = woord[i]
        if woord[i] == '@':
            nieuwwoord += ' '
        elif woord[i] == ' ':
            nieuwwoord += '@'
        else:
            nieuwwoord += chr(ord(woord[i].upper()) + getal)
    return nieuwwoord
