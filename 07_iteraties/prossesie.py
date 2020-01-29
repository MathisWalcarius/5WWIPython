sec = int(input('geef aantal sec: '))
stappenv = 0
verplaatsingv = 0
stappena= 0
verplaatsinga = 0
for i in range(0, sec,2):
    verplaatsingv += 2
    stappenv += verplaatsingv
for i in range(1,sec,2):
    verplaatsinga += 1
    stappena += verplaatsinga



verschil = stappenv - stappena
print(verschil)
