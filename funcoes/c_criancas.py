def sumCodes(listOfCodes: [int]):
    totalSum = 0
    for code in listOfCodes:
        totalSum += code
    return totalSum

def decode(listOfCodes: [int]):
    listOfChar = []
    for code in listOfCodes:
        listOfChar.append(chr(code))
    
    return ''.join(listOfChar)

giftQuantity = int(input())

decodedGifts = []
removedGifts = []
for i in range(giftQuantity):
    inputList = input().split(' ')

    listOfCodes = []
    for str in inputList:
        if str != '':
            listOfCodes.append(int(str))
    decodedGift = decode(listOfCodes)
    
    if sumCodes(listOfCodes) % 2 != 0 and decodedGift not in removedGifts:
        removedGifts.append(decodedGift)

    if decodedGift in decodedGifts:
        print(f"{decodedGift} já está na lista de presentes da Anya!!")
    else:
        print(f"{decodedGift} foi adicionado a lista ultrassecreta de presentes da Anya!!")
        decodedGifts.append(decodedGift)

if len(removedGifts) > 0:
    print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {', '.join(removedGifts)}.")
elif giftQuantity != 0:
    print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")

if len(decodedGifts) == len(removedGifts):
    print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")
else:
    finalGiftsList = []
    for gift in decodedGifts:
        if gift not in removedGifts:
            finalGiftsList.append(gift)
    print(f"Lista final dos melhores presentes da Anya: {', '.join(finalGiftsList)}.")