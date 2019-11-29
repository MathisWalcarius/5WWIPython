sec = int(input('geef aantal sec: '))


stappenv = 0
verplaatsingv = 2
stappena= 0
verplaatsinga = 1

for i in range(0, sec):
    stappenv += verplaatsingv
    verplaatsingv += 2
    stappena += verplaatsinga
    verplaatsinga += 1


verschil = stappenv - stappena
print(verschil)
