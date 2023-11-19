songsCount = int(input())

totalPoints = 0
for i in range(songsCount):
    songName = input()
    songPoints = 0
    for letter in songName:
        letter = letter.lower()
        if (letter == 'a' or
            letter == 'e' or
            letter == 'i' or
            letter == 'o' or
            letter == 'u'):
            songPoints += 1
        else:
            songPoints += 2
    
    if totalPoints > 0:
        totalPoints *= songPoints
    else:
        totalPoints += songPoints  

print(f"Parabéns por adquirir o ingresso! Seu assento é o {totalPoints}, estamos ansiosos para vê-lo, vai ser incrível!")