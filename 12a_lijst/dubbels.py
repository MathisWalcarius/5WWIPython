

def dubbels(list):
    ant = []
    for i in range(len(list)):
        a = list[i]
        if list.count(list[i]) > 1 and list[i] not in ant:
            ant.append(list[i])

    return ant
