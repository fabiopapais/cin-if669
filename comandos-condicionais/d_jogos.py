victimName = input()
villainName = input()
trapType = input()
escapeTime = int(input())

# -1: doesn't survive
# 0: hardly survives
# 1: easily survives
fate = -1

if villainName == "John Kramer":
    if trapType == "Armadilha de urso reversa":
        if escapeTime >= 300:
            print(f"Com tempo de sobra, {victimName} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.")
        elif escapeTime >= 150 and escapeTime < 300:
            print(f"À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {victimName} remove a armadilha de urso e por pouco escapa de um destino cruel.")
        else:
            print("Game Over...")
    elif trapType == "Tanque de agua":
        if escapeTime >= 240:
            print(f"{victimName} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.")
        elif escapeTime >= 120 and escapeTime < 240:
            print(f"{victimName} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.")
        else:
            print("Game Over...")
elif villainName == "Amanda Young":
    if trapType == "Caixa de laminas":
        if escapeTime >= 600:
            print(f"Apenas com ferimentos leves, {victimName} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.")
        elif escapeTime >= 90 and escapeTime < 600:
            print(f"Por um triz, {victimName} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.")
        else:
            print("Game Over...")
    elif trapType == "Asas de anjo":
        if escapeTime >= 180:
            print(f"Com surpreendente facilidade, {victimName} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.")
        elif escapeTime >= 90 and escapeTime < 180:
            print(f"{victimName} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.")
        else:
            print("Game Over...")