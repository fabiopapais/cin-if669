keepReading = True
songsCount = 0
minutes = 0
while keepReading and songsCount < 21:
    opinion = input()

    if opinion == "amei":
        songsCount += 1
        minutes += 4
    elif opinion == "não parei de ouvir":
        newOpinion = ""
        timesListened = 0
        while newOpinion != "pulei":
            newOpinion = input()
            timesListened += 1
        songsCount += 1
        minutes += (timesListened - 1) * 4

    elif opinion == "essa não deu":
        songsCount += 1

    elif opinion == "escutei só metade":
        songsCount += 1
        minutes += 2
    elif opinion == "parei":
        keepReading = False


print(f"Você ouviu {minutes} minutos hoje!!!")