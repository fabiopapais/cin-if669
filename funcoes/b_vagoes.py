
def organizeBaggages(weightsList: [int]):
    sortedWeights = sorted(weightsList)
    finalList = sortedWeights
    finalList[0], finalList[-1] = sortedWeights[-1], sortedWeights[0]
    finalList[1], finalList[-2] = sortedWeights[-2], sortedWeights[1]
    return finalList

def parameters(coal: int, weight: int, passengers: int):
    velocity = int((coal + 200) / 2)
    cargo = int((weight + 4000) / 1000)
    totalPassengers = passengers + 40

    return velocity, cargo, totalPassengers

def shifts(hour: int, script: int, workers: [str]):
    # using different hour format (10:30 == 1030)
    if hour > 700 and hour < 2100:
        if script == 1:
            choosedWorkers = workers[0:2]
        elif script == 2:
            choosedWorkers = [workers[0], workers[-1]]
    # a questão diz "and", mas o correto seria "ou" (?)
    elif hour >= 2100 or hour <= 700:
        if script == 1:
            choosedWorkers = [workers[2]]
        elif script == 2:
            choosedWorkers = []
    
    return choosedWorkers

# converts XX:XX (str) to XXXX (int)
def convertHourFormat(hour: str):
    convertedHour = []
    for char in hour:
        if char.isdigit():
            convertedHour.append(char)
    
    return int("".join(convertedHour))
    

def startProtocol():
    baggages = organizeBaggages(input().split(', '))
    print(f"A nova organização das malas é a seguinte: {', '.join(baggages)}")

    coal, weight, passengers = [int(i) for i in input().split(', ')]
    velocity, cargo, totalPassengers = parameters(coal, weight, passengers)
    print(f"A velocidade que o trem partirá é de: {velocity}Km/H")
    print(f"A carga do Trem em Toneladas é: {cargo} Ton.")
    print(f"A quantidade de passageiros é de {totalPassengers}")

    workers = input().split(', ')
    hour = convertHourFormat(input())
    script = int(input()[-1])
    choosedWorkers = shifts(hour, script, workers)

    if choosedWorkers == []:
        print("Os funcionários convocados são: Nenhum! O turno da Madrugada vai ser tranquilo para todos")
    else:
        print(f"Os funcionários convocados são: {', '.join(choosedWorkers)}")

startProtocol()


#print(organizeBaggages([12, 34, 65, 11, 80, 23, 32]))
#print(parameters(500, 8000, 250))
#print(shifts(10.30, 1, ["Rogério", "Sabrina", "Sorquito", "Claudinete", "Seabroide"]))