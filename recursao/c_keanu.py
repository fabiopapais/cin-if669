# Preenche uma lista de inteiros com '0' à sua esquerda
def fill32(firewallList):
    newFirewall = []
    if len(firewallList) == 32:
        newFirewall = firewallList
    else:
        newFirewall = fill32([0] + firewallList)
    return newFirewall


# Retira o primeiro número de firewallList até encontrar targetByte no seu início
def iterateList(firewallList, targetByte):
    if firewallList[:8] == targetByte:
        return firewallList[:8]
    elif len(firewallList) == 8:
        return firewallList
    return iterateList(firewallList[1:], targetByte)


firewallWord = fill32([int(number) for number in list(input())])
guesses = int(input())
continueGuesses = True

while guesses != 0 and continueGuesses:
    desiredByte = [int(number) for number in list(input())]

    # Como iterateList() retorna apenas a lista completa,
    # precisamos fazer a comparação ao receber o retorno
    if desiredByte == iterateList(firewallWord, desiredByte):
        print("Muito bem! Estamos dentro! Vamos queimar essa cidade!!")
        continueGuesses = False
    else:
        print("Não é essa a senha, estamos ficando sem tempo.")
    
    guesses -= 1

if continueGuesses:
    print("Corre Keanu! Eles nos descobriram!!")