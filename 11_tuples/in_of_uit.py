from math import sqrt


def binnen_of_buiten(mid, p1, p2):

    str = sqrt((mid[0] - p1[0]) ** 2 + (mid[1] - p1[1]) ** 2)
    afsm = sqrt((mid[0] - p2[0]) ** 2 + (mid[1] - p2[1]) ** 2)

    if str == afsm:
        ant = ('op', afsm)
    elif str > afsm:
        ant = ('binnen', afsm)
    else:
        ant = ('buiten', afsm)

    return ant

