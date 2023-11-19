numVerses = int(input())
numCorrectVerses = 0
for i in range(numVerses):
    inputAudience = input()
    normalizedInputAudience = ""
    for char in inputAudience:
        normalizedInputAudience += char.upper()
    if i == 0:
        print("Cause, baby, now we've got")
        if normalizedInputAudience == "BAD BLOOD":
            numCorrectVerses +=1
            print("BAD BLOOD")
    elif i == 1:
        print("You know it used to be")
        if normalizedInputAudience == "MAD LOVE":
            numCorrectVerses +=1
            print("MAD LOVE")
    elif i == 2:
        print("So take a look what")
        if normalizedInputAudience == "YOU'VE DONE":
            numCorrectVerses +=1
            print("YOU'VE DONE")
    else:
        print("Cause, baby, now we've got")
        if normalizedInputAudience == "BAD BLOOD, HEY":
            numCorrectVerses +=1
            print("BAD BLOOD, HEY")

if numCorrectVerses == numVerses:
    print("A plateia deu um show! Acertou tudo!")
elif numCorrectVerses >= 0.5 * numVerses:
    print("A plateia acertou a maior parte da música")
elif numCorrectVerses < 0.5 * numVerses:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
