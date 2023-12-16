truthLists = [
    ['Zeus', 'trovão', 'deus'],
    ['Afrodite', 'amor', 'deusa'],
    ['Poseidon', 'oceanos', 'deus'],
    ['Hércules', 'força', 'semideus'],
    ['Aquiles', 'resistência', 'semideus'],
    ['Orfeu', 'música', 'semideus']
]
questionNumber = int(input())
if questionNumber == 0:
    print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")
else:
    correctAnswers = 0
    for i in range(1, questionNumber + 1):
        answer1, answer2, answer3 = input().split(', ')

        found = False
        for list in truthLists:
            if (answer1 in list and 
                answer2 in list and 
                answer3 in list):
                found = True
                correctAnswers += 1
                break

        print(f"A resposta da {i}ª questão está... CORRETA!") if found else print(f"A resposta da {i}ª questão está... ERRADA!")
                
    percentage = int((correctAnswers / questionNumber) * 100)
    print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {percentage}%")
    
    if (percentage == 100):
        print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")
    elif (percentage >= 60 and percentage < 100):
        print("Muito bem, você quase pode começar a desfilar entre os semideuses!")
    elif(percentage >= 20 and percentage < 60):
        print("Você pode melhorar um pouco mais!")
    else:
        print("Bem... te vejo ano que vem")
