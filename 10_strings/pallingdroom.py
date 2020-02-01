
def is_paligdroom(woord):
    ant = True

    for i in range(len(woord)):
        if woord[i] != woord[-(i + 1) ]:
            ant = False

    return ant
