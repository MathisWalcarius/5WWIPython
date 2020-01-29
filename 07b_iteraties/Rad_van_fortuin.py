
woord = input('woord: ')
geld = int(input('geld: '))
letter = input('letter: ')
totalegeld = 0
geprobeert = ' '
while letter in woord and letter not in geprobeert:
    totalegeld += geld
    geprobeert += letter
    letter = input('letter: ')

print(totalegeld)















