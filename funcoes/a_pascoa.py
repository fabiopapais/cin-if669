daysQuantity = int(input())

def maxBetween(a, b):
    if a > b:
        result = a
    else: 
        result = b
    return result

totalHiddenEggs = 0
totalFoundEggs = 0
for day in range(1, daysQuantity + 1):
    hiddenEggs = int(input())
    foundEggs = 0
    phrase = input()

    if phrase == "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte.":
        foundEggs = hiddenEggs
    elif phrase == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra.":
        foundEggs = hiddenEggs * 0.7
    elif phrase == "As estrelas estão neutras hoje. O dia está em suas mãos.":
        foundEggs = maxBetween(hiddenEggs * 0.7, hiddenEggs / ((hiddenEggs % day) + 1))
    elif phrase == "Isso é raro. As estrelas estão absolutamente neutras hoje.":
        foundEggs = (hiddenEggs % day) + 1
    # elif phrase == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino.":
    #    foundEggs = 0
    
    foundEggs = int(foundEggs)

    totalHiddenEggs += hiddenEggs
    totalFoundEggs += foundEggs

    print(f"Dia {day}")
    print(f"Hoje Carlos encontrou {foundEggs} ovos!!")  

print(f"Kiq encontrou {totalFoundEggs} de um total de {totalHiddenEggs}")
successRate = (totalFoundEggs / totalHiddenEggs) * 100

if successRate == 100:
    print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")
elif successRate < 100 and successRate > 66:
    print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")
elif successRate <= 66 and successRate > 33:
    print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")
elif successRate <= 33 and successRate > 0:
    print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")
elif successRate == 0:
    print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")