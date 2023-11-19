continueLoop = True
while continueLoop:
    nameLover = input()
    if nameLover != "vou dormir":
        wordLover = input()
        wordTaylor = input()
        matchesCount = 0
        for loverChar in wordLover:
            found = False
            foundChar = ""
            if loverChar != "0":
                for taylorChar in wordTaylor:
                    if loverChar == taylorChar:
                        found = True
                        foundChar = loverChar
            if found:
                # assuming any word contains "0"
                wordTaylor.replace(foundChar, "0", 1)
                loverChar.replace(foundChar, "0", 1)
                matchesCount += 1
        if matchesCount >= len(wordTaylor):
            print(f"você acertou, estreou na lista! {nameLover}")
        else:
            print("perdeu covarde!")
    else:
        continueLoop = False