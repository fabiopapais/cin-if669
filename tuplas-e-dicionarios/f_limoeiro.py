# Calcula os pontos com base na lógica dada pela questão
def calculatePoints(string):
    alphabet = tuple(map(chr, range(97, 123)))
    vowels = ('a', 'e', 'i', 'o', 'u') 
    
    positionsMultiplication = 0
    consonantsCount = 0
    for char in string:
        if char.lower() not in vowels and char != ' ':
            consonantsCount += 1
            if positionsMultiplication == 0:
                positionsMultiplication = alphabet.index(char.lower()) + 1
            else:
                positionsMultiplication *= alphabet.index(char.lower()) + 1

    if consonantsCount == 0 or positionsMultiplication**(1/consonantsCount) == 0: 
        return -1
    return (len(string)**2) / (positionsMultiplication**(1/consonantsCount))

# Checa se alguém está utilizando a fantasia dada e retorna o nome de quem está utilizando
def isSomeoneUsingFantasy(unorderedDict, fantasy):
    for name in unorderedDict.keys():
        if unorderedDict[name]['fantasy'] == fantasy:
            return name
    return ''

# Atualiza o dicionário e retorna uma lista com os nomes em ordem
def judge(unorderedDict):
    # Calcula todos os pontos
    namesToRemove = []
    for name in unorderedDict.keys():
        points = calculatePoints(unorderedDict[name]['fantasy'])
        if points != -1:
            unorderedDict[name]['points'] = points
        else:
            namesToRemove.append(name)
    
    # Remove os nomes com divisão por 0
    for name in namesToRemove:
        del unorderedDict[name]
    
    def sortingFunction(name):
        # Primeira condição de ordenação:
        #   quantidade de pontos (multiplicamos por -1 assim a ordenação será em ordem decrescente)
        # Segunda condição de ordenação:
        #   nome do candidato
        return (-1 * unorderedDict[name]['points'], name)

    sortedNames = sorted(unorderedDict.keys(), key=sortingFunction)
    return sortedNames


fantasiesDict = {}
continueLoop = True
while continueLoop:
    command = input()
    if command == 'Adicionar': # ADICIONAR
        name, fantasy = input().split(' - ')
        if name not in fantasiesDict.keys(): # Adiciona candidato
            if isSomeoneUsingFantasy(fantasiesDict, fantasy) != '': # Caso alguém já esteja usando a fantasia
                print(f"Eita, parece que {name} tentou usar a fantasia {fantasy} que ja está sendo utilizada por {isSomeoneUsingFantasy(fantasiesDict, fantasy)}, ele deverá ser desqualificado por plágio")
            else:
                fantasiesDict[name] = {'fantasy': fantasy, 'points': 0}
                print(f"{name} é o novo participante do desfile!")
        else:
            print(f'Opa, parece que {name} ja consta aqui, voce quis dizer "Atualizar"?')
    elif command == 'Atualizar': # ATUALIZAR
        name, fantasy = input().split(' - ')
        if name in fantasiesDict.keys(): # Atualiza candidato
            if isSomeoneUsingFantasy(fantasiesDict, fantasy) != '': # Caso alguém já esteja usando a fantasia
                del fantasiesDict[name]
                print(f"Eita, parece que {name} tentou usar a fantasia {fantasy} que ja está sendo utilizada por {isSomeoneUsingFantasy(fantasiesDict, fantasy)}, ele deverá ser desqualificado por plágio")
            else:
                fantasiesDict[name]['fantasy'] = fantasy
                print(f"Fantasia de {name} atualizada")
        else:
            print(f"Hmmm não consegui achar {name} no banco de dados...")
    elif command == 'Remover': # REMOVER
        name = input()
        if name in fantasiesDict.keys(): # Remove candidato
            del fantasiesDict[name] # Remove candidato
            print(f"Parece que {name} desistiu...")
        else:
            print(f"Hmmm não consegui achar {name} no banco de dados...")
    elif command == 'Julgar previamente': # JULGAR PREVIAMENTE
        if fantasiesDict != {}:
            sortedNames = judge(fantasiesDict)
            if sortedNames != []:
                # Calcula diferença de pontos entre primeiro e segundo colocado
                pointsDifference = fantasiesDict[sortedNames[0]]['points'] - fantasiesDict[sortedNames[1]]['points']
                print(f"Até o momento, o primeiro colocado é {sortedNames[0]} com uma diferença de {pointsDifference:.1f} pontos para o segundo colocado")
    elif command == 'Fim do desfile': # FIM DO DESFILE
        sortedNames = judge(fantasiesDict)
        print("=== RESULTADOS DO DESFILE ===")
        if fantasiesDict != {}:
            for index, name in enumerate(sortedNames):
                print(f"{index + 1}. {name} --- {fantasiesDict[name]['points']:.1f}")
                print()
            print(f"PARABÉNS {sortedNames[0].upper()}!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!")
        else:
            print("Parece que não sobrou ninguem na disputa, que pena…")
        continueLoop = False