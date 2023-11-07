in1, in2, in3, in5 = int(input()), -1, -1, -1
finalNumber = 0
word = "A"

exit = False

if in1 > 0:
    if in1 % 2 == 0:
        in1 *= 2
    else:
        in1 *= 0.5
    in2 = int(input())
else:
    print(f"{in1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit = True

if in2 > 0:
    if in2 % 2 == 0:
        in2 *= 2
    else:
        in2 *= 0.5
    in3 = int(input())
elif not exit:
    print(f"{in2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit = True

if in3 > 0:
    if in3 % 2 == 0:
        in3 *= 2
    else:
        in3 *= 0.5
    word = input()
elif not exit:
    print(f"{in3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit = True

if word.islower():
    in5 = int(input())
elif not exit:
    print(f"{word} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit = True

if in5 > 0:
    finalNumber = (in5 * in3 * in2 * in1)**(1/2)
    if finalNumber >= 10:
        print(f"O número {finalNumber:.2f} e a palavra {word} eram as respostas. A caixa foi aberta.")
    else:
        print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {10 - finalNumber:.2f} anos.")
elif not exit:
    print(f"{in5:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")

# lembrar de formatar duas casas decimais