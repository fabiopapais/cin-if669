availableComputers = int(input())
availableMoney = int(input())
timeLimit = int(input()) * 60

friendsCount = 0
while True:
    name = input()
    if name == "end":
        break
    if name != "laura" and name != "carlos" and name != "roberto":
        friendsCount += 1
    
    if friendsCount == availableComputers:
        break

if friendsCount == 0:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")
else:
    print(f"Bom começo! Consegui {friendsCount} amigos que podem me ajudar a comprar o ingresso")
    bestComputerIndex = -1
    bestLinePosition = -1
    validTicketsCount = 0
    for currentComputerIndex in range(1, friendsCount + 1):
        while True:
            ticketCost, showLocation = input(), input()
            if showLocation == "end":
                break
            elif (showLocation == "rio de janeiro" 
                or showLocation == "são paulo"
                or showLocation == "buenos aires"):
                print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
                if int(ticketCost) <= availableMoney:
                    print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
                    linePosition = int(input())
                    # 16 posições == 10min
                    # 1 posição == 0.625min
                    if (linePosition * 0.625) <= timeLimit:
                        print("ISSOOO, conseguimos um ingresso!!!")
                        validTicketsCount += 1
                        if bestComputerIndex == -1:
                            bestComputerIndex = currentComputerIndex
                            bestLinePosition = linePosition
                        elif linePosition < bestLinePosition:
                            bestComputerIndex = currentComputerIndex
                            bestLinePosition = linePosition
                    else:
                        print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {currentComputerIndex}")
                else:
                    print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")      
                break
    if bestComputerIndex != -1:
        print(f"Consegui o ingresso! Com {int((validTicketsCount/friendsCount)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {bestComputerIndex}. Rumo ao show da Taylor!!!")
    else:
        if friendsCount > 0.5 * availableComputers:
            print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")
        elif friendsCount <= 0.5 * availableComputers:
            print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")