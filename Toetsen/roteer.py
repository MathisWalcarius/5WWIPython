
#def roteer(woord, getal):
    #nieuwwoord = ''
    #if len(woord) == 1:
   #     nieuwwoord = woord
   # else:

    #    for i in range(len(woord)):
    #       nieuwwoord += woord[(getal -1 + i)]
    #return nieuwwoord

def roteer(woord, getal):

    tussenstap = woord * (getal+ 1)
    nieuwwoord = ''
    if len(woord) == 1:
        nieuwwoord = woord
    else:
        for i in range(len(woord)):
            nieuwwoord += tussenstap[getal  + i]
    return nieuwwoord




