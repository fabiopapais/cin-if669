cypherText = input()
cypherTextSize = len(cypherText)

originalMessage = ""
haveDigit = False
for char in cypherText:
    if char == " ":
        originalMessage += " "
    else:
        originalChar = chr(ord(char) + cypherTextSize)
        if originalChar.isdigit():
            haveDigit = True
        originalMessage += originalChar

if originalMessage == " ":
    print("Ué não tem nada para me decifrar aqui")
elif haveDigit:
    print("Algo de errado não está certo. Será que estou ficando doido?")
else:
    print(f"Descobri o que a mensagem significa: {originalMessage}")