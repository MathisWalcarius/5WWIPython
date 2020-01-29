
def is_letter(t):
    return ord(t) <= 122 and ord(t) >= 97 or ord(t) >= 65 and ord(t) <= 90


def roteer_letter(letter,getal):
    if ord(letter) <= ord('Z'):
        if (ord(letter) + getal) > ord('Z'):
            a = chr((ord(letter) + getal)-26)
        else:
            a = chr((ord(letter) + getal))
    else:
        if ord(letter) + getal > ord('z'):
            a = chr(ord(letter) + getal - 26)
        else:
            a = chr(ord(letter) + getal)
    return a

def versleutel(zin, getal):
    nieuwe_zin = ''
    a = ''
    for letter in zin:
        if is_letter(letter):
            letter = roteer_letter(letter,getal)
        nieuwe_zin = nieuwe_zin + str(letter)
    return nieuwe_zin




def roteer_letter(letter, plaatsen):

    #volgnummer is het alfabet bepaald van de gegeven letter
    volgnummer_letter = min(ord(letter) % ord('a'), ord(letter)% ord('A'))

    # volgnummer in het alfabet van nieuwe letter
    nieuw_volgnummer = (volgnummer_letter + plaatsen) % 26

    #offset
    offset  = nieuw_volgnummer - volgnummer_letter

    return chr(ord(letter) + offset)








