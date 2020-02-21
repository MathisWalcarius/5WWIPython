
def hoogtemeters(list):
    ant = []
    for i in range(len(list) - 1):
        ant.append((list[i + 1] - list[i]))
    return ant

def dalen_en_stijgen(list):
    ant1 = 0
    ant2 = 0
    for i in range(len(list)):
        if list[i] > 0:
            ant1 += list[i]
        else:
            ant2 -= list[i]
    return(ant2, ant1)
