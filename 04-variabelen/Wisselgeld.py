# invoer
eurocent =int(input('geef aantal eurocent = '))

#berekening
aantal_mundstukken = eurocent // 100
eurocent = eurocent % 100

aantal_mundstukken += (eurocent// 50)
eurocent = eurocent % 50

aantal_mundstukken += (eurocent// 20)
eurocent = eurocent % 20

aantal_mundstukken += (eurocent// 10)
eurocent = eurocent % 10

aantal_mundstukken += (eurocent// 5)
eurocent = eurocent % 5

aantal_mundstukken += (eurocent// 2)
eurocent = eurocent % 2

aantal_mundstukken += (eurocent// 1)
eurocent = eurocent % 1



print(aantal_mundstukken, eurocent)
# uitvoer
