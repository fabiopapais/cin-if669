availableObjects = input().split(' - ')
movementsCount = int(input())

visibleObjectIndex = int(len(availableObjects) / 2 
                 if len(availableObjects) % 2 == 0 
                 else (len(availableObjects) - 1) / 2)

backpackObjects = []

for i in range(movementsCount):
    directions = input()
    rotationQuantity, rotationDirection = int(directions[:-1]), str(directions[-1])
    if rotationDirection == ">":
        visibleObjectIndex = (int(rotationQuantity) + visibleObjectIndex) % len(availableObjects)
    else:
        visibleObjectIndex = (-1*int(rotationQuantity) + visibleObjectIndex) % len(availableObjects)
    currentObject = availableObjects[visibleObjectIndex]

    decision = input()

    if currentObject in backpackObjects:
        print(f"{currentObject} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
    elif decision == "Adicionar":
        backpackObjects.append(currentObject)
        print(f"{currentObject} adicionado a mochila!")
    elif decision == "Ignorar":
        print(f"{currentObject} não vai ser tão útil assim!")

if len(backpackObjects) == 0:
    print("Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…") 
else:
    print(f"Com {', '.join(backpackObjects)}, seremos imbatíveis na caça à bandeira!")