
def volgend_collatz_getal(getal):

    if getal % 2 == 0:
       return int(getal / 2)
    else:
        return int(getal * 3 + 1)

def collatz(getal):
    aantal = 1
    while getal != 1:
        getal = volgend_collatz_getal(getal)
        aantal += 1
    return aantal
