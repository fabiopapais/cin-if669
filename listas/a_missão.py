missionName = input()

heroNames = []
while True:
    heroName = input()
    if heroName == "Grupo formado":
        break
    heroNames.append(heroName)

print(f"O grupo formado por {len(heroNames)} heróis para a missão {missionName} foi:")
for heroName in heroNames:
    print(f"- {heroName}")