
def verwijder_medeklinkers(woord):
    p = woord[0]
    if woord[0] == 'a' or woord[0] == 'i' or woord[0] == 'u' or woord[0] == 'o' or woord[0] == 'e':
        ant = woord
    else:
        nwoord = woord
        a = 0
        for i in range(len(woord)):
            b = woord[i]
            if woord[i] != 'a' and woord[i] != 'i' and woord[i] != 'u' and woord[i] != 'o' and woord[i] != 'e' and a == 0:

                nwoord = nwoord[i+1:]

            else:
                ant = nwoord
                a = 1

    return ant

def vertaal(zin):
    zin = zin.strip()
    nieuwez = ''
    b = 0
    for i in range(len(zin)):

        if zin[i] == ' ':
            a = i
            nieuwez += zin[b:a]



def varkenslatijn(woord):
    if woord[0] == 'a' or woord[0] == 'i' or woord[0] == 'u' or woord[0] == 'o' or woord[0] == 'e':
        ant = woord + 'ibus'
    elif woord[len(woord)-1] == 'a' or woord[len(woord)-1] == 'i' or woord[len(woord)-1] == 'u' :
        ant = woord + 'nt'
    else:
        woord = verwijder_medeklinkers(woord)
        ant = woord + 'itium'

    ant = ant.replace('j','i')
    ant = ant.replace('y','z')
    return ant





def verwijder_medeklinkers(woord):
    a = woord.find('a')
    aw = woord[a:]

    e = woord.find('e')
    ew = woord[e:]

    i = woord.find('i')
    iw = woord[i:]
    o = woord.find('o')
    ow = woord[o:]
    u = woord.find('u')
    uw = woord[u:]
    z = max(len(aw),len(ew),len(iw),len(ow),len(uw))
    return z
