corrAnswer1, corrAnswer2, corrAnswer3 = input(), input(), input() 

wrongAnswer = False

question1, answer1 = input(), input()
if answer1 == corrAnswer1:
    print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")
else:
    print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
    wrongAnswer = True

if not wrongAnswer:
    question2, answer2 = input(), input()
    if answer2 == corrAnswer2 and not wrongAnswer:
        print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")
    else:
        wrongAnswer = True
        print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")

if not wrongAnswer:
    question3, answer3 = input(), input()
    if answer3 == corrAnswer3 and not wrongAnswer:
        print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")
    else:
        print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")