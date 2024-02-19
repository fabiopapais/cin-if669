bagInput = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
            ['O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O'], 
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

def bagLookup(bag, desiredSize, found=False, coordsStart=[0,0], coordsEnd=[0,0], foundCountI=0, foundCountJ=0, i=0, j=0):
    print(f"Coluna {i} / Linha {j} / Elemento {bag[j][i]} / {foundCountI} {foundCountJ}")
    if not found:
        if bag[j][i] == 'O':
                print(i, j, coordsStart, foundCountI, foundCountJ)
                if foundCountI == 0 and foundCountJ == 0:
                    coordsStart = [i,j]
                foundCountI += 1
        else:
                if i >= desiredSize[0] and j + 1 >= desiredSize[1]:
                    coordsEnd = [i - 1, j]
                    foundCountI = -1
                    foundCountJ = -1
                    found=True
                else:
                    print(i, j + 1)
                    foundCountI = 0
                    foundCountJ = 0
    if i == len(bag[0]) - 1 and j == len(bag) - 1: # Finaliza iteração
        return foundCountI, foundCountJ, coordsStart, coordsEnd
    if i == len(bag[0]) - 1:
        if not found:
            if foundCountI >= desiredSize[0]:
                foundCountJ += 1
            foundCountI = 0
        return bagLookup(bag, desiredSize, coordsStart=coordsStart, coordsEnd=coordsEnd, foundCountI=foundCountI, foundCountJ=foundCountJ, i=0, j=j+1) # Anda linha
    return bagLookup(bag, desiredSize, coordsStart=coordsStart, coordsEnd=coordsEnd, foundCountI=foundCountI, foundCountJ=foundCountJ, i=i+1, j=j) # Anda coluna
    

print(bagLookup(bagInput, desiredSize=[4,3]))


# Apenas para iterar pela matriz:
def iterateMatrix(bag, desiredSize, found=False, i=0, j=0):
    print(f"Coluna {i} / Linha {j} / Elemento {bag[j][i]}")
    if i == len(bag[0]) - 1 and j == len(bag) - 1:
        return found
    if i == len(bag[0]) - 1:
        return iterateMatrix(bag, desiredSize, i=0, j=j+1)
    return iterateMatrix(bag, desiredSize, i=i+1, j=j)