m, n = int(input()), int(input())

# input + logic
dormsMat = []
biggestDormCount = -1
biggestDorm = -1
for i in range(m):
    currentDormList = []
    currentDormSum = 0
    for j in range(n):
        num = int(input())
        currentDormList.append(num)
        currentDormSum += num

    if currentDormSum > biggestDormCount:
        biggestDormCount = currentDormSum
        biggestDorm = i + 1
    
    dormsMat.append(currentDormList)

# output
for dorm in dormsMat:
    print(*dorm)
print(f"\nO chalé {biggestDorm} foi o que mais recebeu semi-deuses, tendo um acréscimo de {biggestDormCount} novos campistas!")

