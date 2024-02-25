import decimal

teamsDict = {}
continueTeamsReading = True
while continueTeamsReading:
    name = input()
    if name == "Não há mais escolas":
        continueTeamsReading = False
    else:
        theme, time = input(), int(input())
        if time > 75:
            penalty = time - 75
        elif time < 65:
            penalty = 65 - time
        else:
            penalty = 0
        teamsDict[name] = {'score': 0, 'theme': theme, 'penalty': penalty}

# armazenando as avaliações para o print
avalsDict = {}
continueAvaliation = True
while continueAvaliation:
    avaliationName = input()
    if avaliationName == "Não há mais quesitos":
        continueAvaliation = False
    else:
        avalsDict[avaliationName] = {}
        for team in teamsDict.keys():
            team, score = input().split(' - ')
            avalsDict[avaliationName][team] = score
            teamsDict[team]['score'] += float(score)

# printando as avaliações
print('Desfile de samba do Rio de janeiro 2024')
for avaliation in avalsDict.keys():
    print(f'Vamos às notas para o quesito {avaliation}:')
    for team in avalsDict[avaliation].keys():
        print(f"{team}: {avalsDict[avaliation][team]}")

# cálculo da pontuação dos times
biggestScore = 0
biggestScoreTeam = ''
for team in teamsDict.keys():
    # somamos todas as avaliações e dividimos pela quantidade de avaliações no final
    teamsDict[team]['score'] = (teamsDict[team]['score'] / len(avalsDict.keys())) - float(teamsDict[team]['penalty'] * decimal.Decimal('0.1'))
    if teamsDict[team]['score'] > biggestScore:
        biggestScore = teamsDict[team]['score']
        biggestScoreTeam = team

print('E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:')
print(f'{biggestScoreTeam} com uma nota final de {biggestScore:.2f}!')
