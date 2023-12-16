desiredItems = input().split(", ")
availableItems = input().split(", ")

foundItems = [item for item in desiredItems if (item in availableItems)]

if len(foundItems) == 0:
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(desiredItems)} itens aqui no Acampamento Meio-Sangue.")
else:
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")
    for i in range(len(foundItems)):
        print(f"{i+1}º item: {foundItems[i]}")
    
    if (len(desiredItems) - len(foundItems) > 0):
        print(f"Vou precisar adquirir {len(desiredItems) - len(foundItems)} itens antes da batalha!")
    else:
        print(f"Perfeito, encontrei todos os {len(desiredItems)} itens aqui no Acampamento Meio-Sangue!")

print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")