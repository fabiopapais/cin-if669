sergioCollection = input().split(", ")
editionCount = int(input())

sagaBooks = ["O Ladrão de Raios", "O Mar de Monstros", "A Maldição do Titã", "A Batalha do Labirinto", "O Último Olimpiano"]

booksToBuy = []
for sagaBook in sagaBooks:
    if sagaBook not in sergioCollection:
        booksToBuy.append(sagaBook)
wrongBooks = []
for sergioBook in sergioCollection:
    if sergioBook not in sagaBooks and sergioBook != "":
        wrongBooks.append(sergioBook)

if len(booksToBuy) == 0:
    print("Sua coleção está completa! Você pode ler à vontade.")
elif len(booksToBuy) == 5:
    print("Caramba, você não tem nenhum livro. Compre todos imediatamente.")
else:
    print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {', '.join(booksToBuy)}.")

if len(wrongBooks) > 0:
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {", ".join(wrongBooks)}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')