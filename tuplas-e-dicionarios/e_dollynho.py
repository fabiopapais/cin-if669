dollyLife, dollyAttack, dollyDefense = int(input()), int(input()), int(input())
enemiesQuantity = int(input())
enemies = {}

if enemiesQuantity > 0:
    print("Oh não! Eles querem acabar com o meu Dollynho!")
else:
    print("Oba! Sem intercorrências pelo caminho! Podemos ir para o carnaval em paz!")


eliminatedEnemies = 0
# loop dos inimigos
for i in range(enemiesQuantity):
    enemyName = input()
    enemies[enemyName] = {'life': int(input()), 'attack': int(input()), 'defense': int(input())}

    # lógica de batalha
    isDollyAttacking = True
    while dollyLife > 0 and enemies[enemyName]['life'] > 0:
        if isDollyAttacking:
            enemies[enemyName]['life'] -= dollyAttack - enemies[enemyName]['defense']
        else:
            dollyLife -= enemies[enemyName]['attack'] - dollyDefense
        isDollyAttacking = not isDollyAttacking
    
    # Caso dolly morra
    if dollyLife <= 0:
        print("Que tristeza! Dollynho se foi!")
        break
    # Caso o inimigo morra
    elif enemies[enemyName]['life'] <= 0:
        eliminatedEnemies += 1
        print(f"O {enemyName} foi derrotado!")
        print("STATUS DOLLY")
        print(f"Vida: {dollyLife}")

if enemiesQuantity > 0:
    if enemiesQuantity == eliminatedEnemies:
        print("OBA! Dolly venceu todos os inimigos!")
    else:
        print("Infelizmente Dollynho não conseguiu vencer todos os Barriguinhas Moles…")
        print(f"Pelo menos levou {eliminatedEnemies} baderneiros com ele!")