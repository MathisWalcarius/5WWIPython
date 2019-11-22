kleur1 = input('kleur hoed1: ')
kleur2 = input('kleur hoed2: ')
po = int(input('persoon die liegt: '))

#berekening

if 'z' in kleur1 and 'z' in kleur2 and po == 1 or 'w' in kleur1 and 'z' in kleur2 and po == 2:
    p1 = 'wit'
    p2 = 'zwart'
elif 'w' in kleur1 and 'w' in kleur2 and po == 1 or 'z' in kleur1 and 'z' in kleur2 and po == 2:
    p1 = 'zwart'
    P2 = 'wit'
elif 'w' in kleur1 and 'z' in kleur2 and po == 1 or 'z' in kleur1 and 'w' in kleur2 and po == 2:
    p1 = 'wit'
    p2 = 'wit'
else:
    p1 = 'zwart'
    p2 = 'zwart'

#if 1 == po :
  #  if kleur1 != kleur2:
     #    p1 = 'wit'
     #    p2 = 'wit'
   # elif 'z' in kleur1 and 'z' in kleur2:
   #      p1 = 'wit'
   #      p2 = 'zwart'
  #  elif 'z' in kleur1 and 'w' in kleur2:
     #    p1 = 'zwart'
    #     p2 = 'zwart'
 #   else:
  #       p1 = 'zwart'
  #       P2 = 'wit'
#else:
   #  if kleur1 == kleur2:
    #     p1 = 'zwart'
     #    P2 = 'wit'
  #   elif 'w' in kleur1 and 'w' in kleur2:
     #    p1 = 'wit'
     #    p2 = 'zwart'
   #  elif 'w' in kleur1 and 'z' in kleur2:
   #      p1 = 'zwart'
   #      p2 = 'zwart'
   #  else:
     #    p1 = 'wit'
      #   P2 = 'wit'




#uitvoer

print(p1)
print(p2)
