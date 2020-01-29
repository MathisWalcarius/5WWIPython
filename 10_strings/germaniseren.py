
def germaniseer(zin):
    nieuwezin = ''
    a = 0
    nummer = 0
    for letter in zin:

        if a ==  1:
            nieuwezin = zin[:mummer] + i.upper() + zin[i:]
            a = 0

        if letter == ' ':
            a = 1
        nummer += 1
    return nieuwezin


