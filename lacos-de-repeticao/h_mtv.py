celebrityCount = int(input())
isKanyeWestPresent, isPiquePresent, isChrisMartinPresent = False, False, False
for i in range(celebrityCount):
    celebrityName = input()
    if celebrityName == "Kanye West":
        isKanyeWestPresent = True
    elif celebrityName == "Gerard Piqué":
        isPiquePresent = True
    elif celebrityName == "Chris Martin":
        isChrisMartinPresent = True
    print(f"Apresentador: Contamos com a ilustre presença de {celebrityName}, uma salva de palmas!")

winnerName = ""
isTaylorPresent, isKatyPresent, isArianaPresent, isBeyoncePresent = False, False, False, False
while True:
    candidateName = input()
    if candidateName == "Início da Premiação":
        break
    
    if candidateName == "Taylor Swift":
        winnerName = "Taylor Swift"
        isTaylorPresent = True
    elif candidateName == "Katy Perry": 
        isKatyPresent = True
        if not isTaylorPresent:
            winnerName = "Katy Perry"
    elif candidateName == "Ariana Grande": 
        isArianaPresent = True
        if not isTaylorPresent and not isKatyPresent:
            winnerName = "Ariana Grande"
    elif candidateName == "Beyoncé": 
        isBeyoncePresent = True
        if not isTaylorPresent and not isKatyPresent and not isArianaPresent:
            winnerName = "Beyoncé"
    elif candidateName == "Shakira": 
        if not isTaylorPresent and not isKatyPresent and not isArianaPresent and not isBeyoncePresent:
            winnerName = "Shakira"

print("Apresentador: Vamos deixar de enrolação e ir para a premiação!")
print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")

print(winnerName.upper())

if winnerName == "Taylor Swift" and isKanyeWestPresent:
    print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")
elif winnerName == "Shakira" and isPiquePresent:
    print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")
elif winnerName == "Beyoncé" and isChrisMartinPresent:
    print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")