percyCoords = [int(input()), int(input())]
clarisseCoords = [int(input()), int(input())]
waterCoords = [int(input()), int(input())]
flagCoords = [int(input()), int(input())]

# invertendo valores apenas para facilitar (y,x) -> (x,y)
for coordList in [percyCoords, clarisseCoords, waterCoords, flagCoords]:
    coordList[0], coordList[1] = coordList[1], coordList[0]

def clarisseMovement(clarisseCoord, percyCoord):
    if clarisseCoord[0] == percyCoord[0]: # mesma coluna
        if clarisseCoord[1] > percyCoord[1]:
            clarisseCoord[1] -= 1
        elif clarisseCoord[1] < percyCoord[1]:
            clarisseCoord[1] += 1 
    else: # coluna diferente
        if clarisseCoord[0] > percyCoord[0]:
            clarisseCoord[0] -= 1
        elif clarisseCoord[0] < percyCoord[0]:
            clarisseCoord[0] += 1
    return clarisseCoord

def percyMovement(percyCoord, direction):
    if direction == "cima" and percyCoord[1] > 0:
        percyCoord[1] -= 1
    elif direction == "baixo" and percyCoord[1] < 8:
        percyCoord[1] += 1
    elif direction == "esquerda" and percyCoord[0] > 0:
        percyCoord[0] -= 1
    elif direction == "direita" and percyCoord[0] < 8:
        percyCoord[0] += 1
    return percyCoord

def printMap(percyCoord, clarisseCoord, waterCoord, flagCoord, printFlag = True):
    for i in range(8):
        line = []
        for j in range(8):
            if [j, i] == clarisseCoord:
                line.append('C')
            elif [j, i] == percyCoord:
                line.append('P')
            elif [j, i] == waterCoord:
                line.append('A')
            elif [j, i] == flagCoord and printFlag:
                line.append('B')
            else:
                line.append('-')
        print(" ".join(line))

percyHasFlag = False
while True:
    clarisseCoords = clarisseMovement(clarisseCoords, percyCoords)

    if clarisseCoords == waterCoords:
        print("Vitória!! Nunca subestime o cabeça de alga!")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        break
    elif percyCoords == clarisseCoords:
        print("Ah não, Annabeth vai me matar...")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        break
    
    percyDirection = input()
    percyCoords = percyMovement(percyCoords, percyDirection)

    if percyCoords == waterCoords:
        percyCoords = percyMovement(percyCoords, percyDirection)
        print("Sinto o poder de Poseidon em minhas veias!")

    if percyCoords == flagCoords:
        percyHasFlag = True

    if percyHasFlag and percyCoords[1] == 0:
        print("Vitória!! Nunca subestime o cabeça de alga!")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        break

    if percyCoords != flagCoords and not percyHasFlag:
        print("Preciso pegar aquela maldita bandeira vermelha.")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        print()
    elif percyCoords == flagCoords:
        print("Isso! Consegui a bandeira!")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        print()
    elif percyHasFlag:
        print("Agora eu só preciso meter o pé daqui!")
        printMap(percyCoords, clarisseCoords, waterCoords, flagCoords, not percyHasFlag)
        print()