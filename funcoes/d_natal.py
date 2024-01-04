def euclideanDist(x0: float, y0: float, x: float, y: float) -> float:
    return ((x-x0)**2 + (y-y0)**2)**(1/2)

def decryptCaeserCipher(text: str, shift: int, direction: str) -> str:
    decryptedList = []
    for char in list(text):
        if direction == "R":
            newShift = (shift - (91 - ord(char))) % 26
            decryptedList.append(chr((65 + newShift)))
        elif direction == "L":
            newShift = (shift - (ord(char) - 64)) % 26
            decryptedList.append(chr(90 - newShift))
    return ''.join(decryptedList)

citiesQuantity = int(input())

names = []
decryptedPswds = []
coordinates = []
for i in range(citiesQuantity):
    name, x, y, encryptedPswd, shift, direction = input().split(', ')

    names.append(name)
    decryptedPswds.append(decryptCaeserCipher(encryptedPswd, int(shift), direction))
    coordinates.append([float(x), float(y)])

# Este bloco organiza as visitas do papai noel, olhando para cada coordenada
# Usei a solução força bruta, olhando pra todas as coordenadas várias vezes (dá pra otimizar)
currentCoordinate = [0,0]
shortestCoordinateindex = []
for i in range(citiesQuantity):
    # armazena a [menor distância, índice da coordenada mais próxima]
    shortest = [float('inf'), -1]
    for j in range(len(coordinates)):
        dist = euclideanDist(currentCoordinate[0], currentCoordinate[1], coordinates[j][0], coordinates[j][1])
        if dist < shortest[0] and j not in shortestCoordinateindex:
            shortest = [dist, j]
    
    shortestCoordinateindex.append(shortest[1])
    currentCoordinate = coordinates[shortest[1]]
    coordinates.pop


for index in shortestCoordinateindex:
    print(f"A senha da cidade {names[index]} é: {decryptedPswds[index]}")