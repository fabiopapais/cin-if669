# Converte uma lista de 0s e 1s para sua forma decimal
def binaryToDecimal(bitString, currentSum=0, currentIndex=0):
    if len(bitString) == 0:
        return currentSum
    else:
        if bitString[-1] == '1':
            currentSum += 2**currentIndex
        return binaryToDecimal(bitString[:-1], currentSum, currentIndex + 1)     


# Converte uma lista de decimais para uma lista de caracteres ASCII
def decimalToAscii(decimalList, asciiList=[]):
    if len(decimalList) == 0:
        return asciiList
    else:
        return decimalToAscii(decimalList[1:], asciiList + [chr(decimalList[0])])


# Executa binaryToDecimal e decimalToAscii na lista de strings binárias
# e retorna a string decodificada
def loop(binaryStringsList, decimalList=[]):
    if len(binaryStringsList) == 0:
        return ''.join(decimalToAscii(decimalList))
    else:
        return loop(binaryStringsList[1:], decimalList + [binaryToDecimal(binaryStringsList[0])])


code = [list(char) for char in input().split(' ')]
print(f"Os códigos da Matrix indicam que {loop(code)} está perto.")