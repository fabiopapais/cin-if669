presentationCount = int(input())
tay_wins, bey_wins = 0, 0

print("Vai começar! Vamos ver quem é a verdadeira diva!")

round = 1
while round <= presentationCount:
    print(f"Vai começar a {round}º rodada!")
    tay_coreography, tay_costume = int(input()), int(input())
    bey_coreography, bey_costume = int(input()), int(input())

    tay_points = tay_coreography * 4 + tay_costume * 3
    bey_points = bey_coreography * 4 + bey_costume * 3

    if tay_points > bey_points:
        tay_wins += 1
        print(f"Fim da apresentação! O placar da rodada {round} foi {tay_points}x{bey_points} para os representantes da Tay.")
    else:
        bey_wins += 1
        print(f"Fim da apresentação! O placar da rodada {round} foi {bey_points}x{tay_points} para os representantes da Bey.")

    if abs(tay_points - bey_points) > 20:
        print(f"A diferença na pontuação foi de {abs(tay_points - bey_points)} pontos.")
    else:
        print(f"A diferença de pontos foi de apenas {abs(tay_points - bey_points)}.")
    
    if tay_wins == 3 or bey_wins == 3:
        round = presentationCount + 1
    
    round += 1

if tay_wins > bey_wins:
    print(f"Uuuh! Por um placar de {tay_wins} a {bey_wins}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
else:
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {bey_wins} a {tay_wins}. A Bey é a verdadeira rainha do pop!")