allowedTeams = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
teamsAval = {}

continueTeamsAval = True
while continueTeamsAval:
    entry = input()
    if entry == "Fim":
        continueTeamsAval = False
    else:
        name, aval = entry.split(": ")
        if name not in allowedTeams:
            print("Epa, o que essa escola está fazendo aqui?!")
        elif name in teamsAval.keys():
            print(f"{name} teve sua nota atualizada!")
            teamsAval[name] = float(aval)
        else:
            print(f"{name} teve sua nota apurada!")
            teamsAval[name] = float(aval)
print()

sortedAvals = sorted(teamsAval.items(), key=lambda aval: aval[1], reverse=True)
count = 1
print("CLASSIFICAÇÃO DO CARNAVAL 2024:")
for team in sortedAvals:
    print(f"{count}. {team[0]}: {team[1]}")
    count += 1

print()
print(f"É CAMPEÃ! A ESCOLA {sortedAvals[0][0]} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {sortedAvals[0][1]} PONTOS!!")
print(f"Infelizmente, a escola {sortedAvals[-1][0]} não alcançou as expectativas, fazendo apenas {sortedAvals[-1][1]} pontos, e foi rebaixada.")
