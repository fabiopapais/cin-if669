buyersCount = int(input())
suspectsCount = 0

for i in range(buyersCount):
    suspectPoints = 0
    
    nameBuyer, cpfBuyer = input(), input()
    nameId, cpfId = input(), input()
    ticketsCount, ticketsPrice = int(input()), float(input())
    purchaseCode = input()

    if nameBuyer != nameId: 
        suspectPoints += 1
    if cpfBuyer != cpfId:
        suspectPoints += 1
    if ticketsCount > 12:
        suspectPoints += 1
    if ticketsPrice > 1500: # check logic
        suspectPoints += 1

    oddCount = 0
    for digit in purchaseCode:
        if int(digit) % 2 != 0:
            oddCount += 1
    
    if oddCount >= 7:
        suspectPoints += 1

    if suspectPoints >= 3:
        suspectsCount += 1

print(f"Total de compradores analisados: {buyersCount}")
print(f"Total de suspeitas de cambistas: {suspectsCount}")