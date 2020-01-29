aantal = int(input('aantal lifters: '))

hoogst = 0

for i in range(1,((aantal)//2+1)):
    score = float(input('score'))
    if score > hoogst:
        hoogst = score

for i in range(((aantal)//2+1),(aantal+1)):
    score = float(input('score'))
    if score > hoogst:
        lifter = score
        break
    if i == aantal:
        lifter = score

print(lifter)
















