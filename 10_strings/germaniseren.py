
def germaniseer(zin):
    nieuwezin = ''
    a = 0
    nummer = 0
    for letter in zin:

        if a ==  1:
            nieuwezin = nieuwezin[:nummer] + letter.upper()
            a = 0
        else:
            nieuwezin += letter
        if letter == ' ':
            a = 1
        nummer += 1
    return nieuwezin


