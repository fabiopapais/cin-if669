# diz se é pangrama e retorna a maior e menor frequência de letra
def pangram(text: str) -> (bool, int, int):
    frequencies = [0]*26
    for char in list(text.lower()):
        if ord(char) >= 97 and ord(char) <= 122:
            frequencies[ord(char) - 97] += 1
    
    isPangram = True
    biggestFrequency = -1
    lowestFrequency = float('inf')
    for frequency in frequencies:
        if frequency == 0:
            isPangram = False
        if frequency > biggestFrequency:
            biggestFrequency = frequency
        if frequency < lowestFrequency  and frequency != 0:
            lowestFrequency = frequency
    
    return isPangram, biggestFrequency, lowestFrequency
            

# retorna n-número de fibonacci
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        numeroAnterior = 1
        numeroAnteAnterior = 1
        for i in range(3, n + 1):
            c = numeroAnterior
            numeroAnterior = numeroAnterior + numeroAnteAnterior
            numeroAnteAnterior = c
        return numeroAnterior

# retorna a diferença de letras maiúsculas e minúsculas
def diffUpperLower(word: str) -> int:
    upper = 0
    lower = 0
    for char in list(word):
        if char.lower() == char and char != ' ':
            lower += 1
        elif char != ' ':
            upper += 1
    return lower - upper


# 1o desafio
phraseX = input()
isPangram, biggestFrequency, lowestFrequency = pangram(phraseX)
if isPangram:
    noelX = biggestFrequency
else:
    noelX = lowestFrequency

# 2o desafio
wordY = input()
hasVowel = False
for char in list(wordY):
    if char in ['a', 'e', 'i', 'o', 'u']:
        hasVowel = True
if hasVowel:
    noelY = fib(len(wordY)) * 4
else:
    noelY = fib(len(wordY)) * 2

# 3o desafio
wordZ = input()
phraseZ = input()
noelZ = int(diffUpperLower(phraseZ)**diffUpperLower(wordZ))

jackX, jackY, jackZ = int(input()), int(input()), int(input())
finalDistance = ((noelX - jackX)**2 + (noelY - jackY)**2 + (noelZ - jackZ)**2)**(1/2)

print(f"A 1ª coordenada do Papai Noel é: {noelX}")
print(f"A 2ª coordenada do Papai Noel é: {noelY}")
print(f"A 3ª coordenada do Papai Noel é: {noelZ}")
print(f"A distância entre Jack Esqueleto e Papai Noel é: {finalDistance:.2f}")