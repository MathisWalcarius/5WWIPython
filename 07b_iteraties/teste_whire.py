#woord = 'start'

#while woord != 'stop':
    #print(woord)
   # woord = input('geef woord: ')


#teste 2

#vorst_periode = 0
#temperatuur = int(input('Dagtemperatuur: '))

#while temperatuur <= 0:
    #vorst_periode += 1
   # #op einde while lus nieuwe invoer vragen
   # temperatuur = int(input('Dagtemperatuur: '))

#print(vorst_periode)


#from random import randint

#munt = 0
#aantal_experimenten = 1000000

#for i in range(aantal_experimenten):
 #   munt += randint(0,1)
#print('munt: ', munt / aantal_experimenten, 'kop ',(aantal_experimenten - munt) / aantal_experimenten)


# bieden met afslag
bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))

akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

while (not akkoord) and (bod >= doorgedraaid + 0.01):
    bod -= 0.01
    akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

if akkoord:
    print('verkocht aan {:.2f}'.format(bod))
else:
    print('doorgedraaid')
