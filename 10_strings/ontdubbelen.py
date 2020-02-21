
def ontdubbelen(woord):
    antwoord = woord[0]
    for i in range(1, len(woord)):
        if woord[i] != woord[i - 1]:
            antwoord += woord[i]
    return antwoord
