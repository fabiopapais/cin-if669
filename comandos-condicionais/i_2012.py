instruction = int(input())
string1, string2, string3 = input(), input(), input()
len1, len2, len3 = len(string1), len(string2), len(string3)

mostLetters = ""
lessLetters = ""

# string com mais letras
if instruction == 1:
    if len1 > len2 and len1 > len3:
        mostLetters = string1
    elif len2 > len1 and len2 > len3:
        mostLetters = string2
    elif len3 > len2 and len3 > len1:
        mostLetters = string3
    if mostLetters != "":
        print(mostLetters)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
# string com menos letras
elif instruction == 2:
    if len1 < len2 and len1 < len3:
        lessLetters = string1
    elif len2 < len1 and len2 < len3:
        lessLetters = string2
    elif len3 < len2 and len3 < len1:
        lessLetters = string3
    if lessLetters != "":
        print(lessLetters)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

if mostLetters == "" and lessLetters == "":
    print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
    # maior lexico
    mostLex = "" # assumo que não existe local chamado ""
    if string1 > string2 and string1 > string3:
        mostLex = string1
    elif string2 > string1 and string2 > string3:
        mostLex = string2
    elif string3 > string2 and string3 > string1:
        mostLex = string3

    if mostLex == "":
        print('"AAAAAA! Um fantasma me assustou!"\n(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')
    else:
        print(mostLex)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

print('(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)')