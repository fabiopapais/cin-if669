availableEquipment = ["Foice de Hades", "Talismã de Ícaro", "Elmo da Invisibilidade", "Cinto de Hermes", "Espada Anaklusmos", "Escudo Aegis", "Adaga Katoptris"]
herosNames = []
herosEquipments = []
while True:
    entry = input().split("-")
    if entry[0] == "Parar":
        break
    elif len(entry) == 1:
        herosNames.append(entry[0])
        herosEquipments.append(availableEquipment.copy())
    else:
        herosNames.append(entry[0])
        currentHeroEquipment = availableEquipment.copy()
        for i in range(1, len(entry)): # skips 1st element
            currentHeroEquipment.remove(entry[i])
        herosEquipments.append(currentHeroEquipment)

for i in range(len(herosNames)):
    if len(herosEquipments[i]) == 0:
        print(f"{herosNames[i]} irá batalhar na base do murro!")
    elif len(herosEquipments[i]) == 1:
        print(f"{herosNames[i]} irá rumo a batalha com o equipamento: {herosEquipments[i][0]}!")
    else:
        printString = ", ".join(herosEquipments[i][:-1])
        print(f"{herosNames[i]} irá rumo a batalha com os seguintes equipamentos: {printString} e {herosEquipments[i][-1]}!")