points = 0
stopRead = False
songsCount = 0
while not stopRead:
    text = input()
    if text == "os fãs estão formando uma ciranda":
        points -= 3
    elif ( 
        text == "os fãs estão ligando os flashes e atrapalhando a visão" or 
        text == "os fãs estão dançando na frente da tela" or
        text == "os fãs estão gritando o nome da Taylor e atrapalhando a música"
    ):
        points -= 2
    elif (  
        text == "os fãs estão cantando as músicas em coro" or
        text == "houve um pedido de casamento na sessão"
    ): 
        points += 2
    elif text == "long live":
        stopRead = True
        songsCount +=1
        print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {songsCount} músicas.")
    else:
        points += 1
        songsCount +=1
    
    if points < 0:
        print(f"A Taylor só conseguiu cantar {songsCount} músicas e a sessão foi interrompida.")
        stopRead = True

    