
kleur = input(' ')
listkl = [ ]
while kleur != 'STOP' :
    if kleur == '?' and  len(listkl) != 0:
        print(listkl.pop(0))
    if kleur != '?':
        listkl.append(kleur)
    kleur = input(' ')
