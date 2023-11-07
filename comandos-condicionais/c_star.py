testPlace = input()
testTime = int(input())
momAnswer = input()

leaveTime = testTime

if testPlace == "Salão":
    print("Em direção ao salão!")
    leaveTime -= 2
elif testPlace == "Praça":
    print("Para a praça eu vou!")
    leaveTime -= 2
elif testPlace == "Centro da cidade":
    print("Faz tempo que não visito o centro, mal posso esperar!")
    leaveTime -= 1

print(f"Pra chegar na hora, vou ter que sair de {leaveTime} horas.")

if momAnswer == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
elif momAnswer == "Não. Você ficará na fazenda.":
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")

