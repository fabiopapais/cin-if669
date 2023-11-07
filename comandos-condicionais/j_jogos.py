points = 0
doorString = ""
anyWrong = False

direction, number = input(), int(input())
# primeira porta
if number % 2 != 0 and direction == "direita":
    points += 150
    doorString += "CERTA"
elif direction == "esquerda":
    points += 150
    doorString += "CERTA"
else:
    doorString += "ERRADA"
    anyWrong = True

direction, color, plant, handle = input(), input(), input(), input() 
# segunda porta
if (
    (color == "dourada" or color == "prateada") 
    or ((plant == "avenca" or plant == "espadinha") and handle == "redonda")
) and direction == "direita":
    points += 200
    doorString += " CERTA"
elif direction == "esquerda":
    points += 200
    doorString += " CERTA"
else:
    doorString += " ERRADA"
    anyWrong = True

direction, color, number, plant, handle = input(), input(), int(input()), input(), input()
# terceira porta
if (
    (number % 5 == 0 and plant == "espadinha" and handle == "quadrada")
    or (color == "perolada")
    and direction == "esquerda"
):
    points += 250
    doorString += " CERTA"
elif direction == "direita":
    points += 250
    doorString += " CERTA"
else:
    doorString += " ERRADA"
    anyWrong = True

direction, number = input(), int(input())
# quarta porta
if (
    (number % 3 == 0
    and number % 2 != 0
    and number % 5 != 0)
    and direction == "direita"
):
    points += 300
    doorString += " CERTA"
elif direction == "esquerda":
    points += 300
    doorString += " CERTA"
else:
    doorString += " ERRADA"
    anyWrong = True

color, number, plant, flower, handle = input(), int(input()), input(), input(), input()
# quinta porta
if (
    color == "acobreada"
    and (
        number % 2 != 0
        or handle == "triangular" 
        or handle == "quadrada" 
    )
    and plant == "jiboia"
):
    points += 500
    doorString += " CERTA"
elif (
    color == "prateada"
    and (
        flower != "margarida"
        or flower != "papoula"
        or flower != "cosmos"
    )
    and (
        handle == "hexagonal"
        or handle == "redonda"
    )
):
    points += 450
    doorString += " CERTA"
elif (
    color == "dourada"
    and (
        flower == "lirio"
        or flower == "ixora"
    ) and handle == "hexagonal"
):
    points += 400
    doorString += " CERTA"
else:
    points -= 500
    doorString += " ERRADA"
    anyWrong = True

print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")

print(doorString)

if points > 0:
    if anyWrong:
        print(f"Você passou com {points} pontos, mas faça melhores escolhas da próxima vez.")
    else:
        print(f"Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {points} pontos!")
else:
    if not anyWrong:
        print(f"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {points} pontos")
    else:
        print(f"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {points} pontos.")
