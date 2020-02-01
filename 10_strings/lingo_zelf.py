
def hint(gok, woord):
    hint = ''
    for i in range(0, 5):

        if woord[i] == gok[i]:
            hint = hint[:i] + gok[i].upper()
        elif woord.find(gok[i]) != -1:
            hint = hint[:i] + gok[i]
        else:
            hint = hint[:i] + '.'

    return hint







