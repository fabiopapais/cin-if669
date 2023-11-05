phrase, attribute = input(), input()

creature = "humano"

if phrase == "Parou filhotada, assim vocês vão deixar todo mundo maluco.":
    if attribute == "Uivar" or attribute == "Pelos" or attribute == "Caninos":
        creature = "lobisomen"
elif phrase == "Veio de novo pelo correio, deixa de ser pão duro.":
    if attribute == "Desmontável" or attribute == "Parafusos" or attribute == "Morto-vivo":
        creature = "frankenstein"
elif phrase == "Quem me beliscou?":
    if attribute == "Transparente":
        creature = "invisivel"
elif phrase == "Tô na área galera!":
    if attribute == "Enfaixado" or attribute == "Morto-vivo":
        creature = "mumia"

if creature == "humano":
    print("UM HUMANO! Quem é você, e como você achou esse lugar?")
else:
    print("Bem-vindos ao Hotel Transilvânia!")
    if creature == "lobisomen":
        print("Wayne, seu cachorrão.")
    elif creature == "frankenstein":
        print("Frank, assim vai acabar perdendo a cabeça.")
    elif creature == "invisivel":
        print("Griffin, prazer em vê-lo.")
    elif creature == "mumia":
        print("Murray, sempre soltando areia.")

