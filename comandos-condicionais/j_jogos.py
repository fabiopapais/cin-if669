points = 0
doorString = ""
anyWrong = False
anyRight = False

# primeira porta
direction, number = input(), int(input())
if number % 2 != 0 and direction == "direita":
    points += 150
    doorString += "CERTA"
    anyRight = True
elif number % 2 == 0 and direction == "esquerda":
    points += 150
    doorString += "CERTA"
    anyRight = True
else:
    doorString += "ERRADA"
    anyWrong = True
    points -= 150

# segunda porta
direction, color, plant, handle = input(), input(), input(), input() 
if (
    ((color == "dourada" or color == "prateada") 
    or ((plant == "avenca" or plant == "espadinha") and handle == "redonda"))
    and direction == "direita"
):
    points += 200
    doorString += " CERTA"
    anyRight = True
elif direction == "esquerda":
    points += 200
    doorString += " CERTA"
    anyRight = True
else:
    doorString += " ERRADA"
    anyWrong = True
    points -= 200

# terceira porta
direction, color, number, plant, handle = input(), input(), int(input()), input(), input()
if (
    ((number % 5 == 0 and plant == "espadinha" and handle == "quadrada")
    or (color == "perolada"))
    and direction == "esquerda"
):
    points += 250
    doorString += " CERTA"
    anyRight = True
elif number % 5 != 0 and direction == "direita":
    points += 250
    doorString += " CERTA"
    anyRight = True
else:
    doorString += " ERRADA"
    anyWrong = True
    points -= 250

# quarta porta
direction, number = input(), int(input())
if (
    (number % 3 == 0
    and number % 2 != 0
    and number % 5 != 0)
    and direction == "direita"
):
    points += 300
    doorString += " CERTA"
    anyRight = True
elif direction == "esquerda":
    points += 300
    doorString += " CERTA"
    anyRight = True
else:
    doorString += " ERRADA"
    anyWrong = True
    points -= 300

# quinta porta
color, number, plant, flower, handle = input(), int(input()), input(), input(), input()
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
    anyRight = True
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
    anyRight = True
elif (
    color == "dourada"
    and (
        flower == "lirio"
        or flower == "ixora"
    ) and handle == "hexagonal"
):
    points += 400
    doorString += " CERTA"
    anyRight = True
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
    if anyRight:
        print(f"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {points} pontos")
    else:
        print(f"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {points} pontos.")
