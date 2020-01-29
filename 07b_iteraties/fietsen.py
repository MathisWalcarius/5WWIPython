stijns = int(input('snelheid stijn : '))
kaats = int(input('snelheid kaat : '))
afstand = int(input('afstand : '))

afstands, afstandk, sec,  = afstand,0,0

#while afstandk != afstands:
 #   afstands -= stijns
  #  afstandk += kaats
   # sec += 1
while afstand > 0:
    afstand = afstand - (stijns + kaats)
    sec += 1





uitvoer = 'Na {:d} s hebben Stijn en Kaat elkaar ontmoet.'

print(uitvoer.format(int(sec)))













