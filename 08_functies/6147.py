
def splits(getal):
    a,b,c,d = '', '', '', ''
    n = 1
    woord = str(getal)
    for letter in woord:
         if n ==1:
             a = letter
         elif n == 2:
             b = letter
         elif n == 3:
             c = letter
         else:
             d = letter
         n += 1
    ant = int(a), int(b), int(c), int(d)
    return ant

def oplopende_cijfers(a,b,c,d):
    a1 = max(a,b,c,d)
    a2 = max(min(a,b),min(b,c),min(c,d),min(d,a),min(a,c),min(b,d))
    a4 = min(a,b,c,d)
    a3 = a+b+c+d - (a1+a2+a4)
    return a4, a3, a2, a1

def op_af_getallen(a,b,c,d):

    return str(a)+str(b)+str(c)+str(d), str(d)+str(c)+str(b)+str(a)

def verschil (getalg, getalk):

    return str(int(getalg) - int(getalk))


def kaprekar(getal):
    uitkomst = ''

    while int(getal) != 6174 :

        a, b, c, d = splits(getal)
        e, f, g, h = oplopende_cijfers(a,b,c,d)

        j, i = op_af_getallen(e, f, g, h)
        getal = (verschil(i,j))
        if int(getal) != 6174:
            uitkomst += str(i) + ' - ' + str(j)  + ' = ' + getal + '\n'
        else:
            uitkomst += str(i) + ' - ' + str(j)  + ' = ' + getal


    return uitkomst








