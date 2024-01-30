def separateGroups(number, shardsGroups):
    shardsGroups.append(int(number))
    if number % 3 == 0 and number != 0:
        base = number / 3
        complement = number - base
        shardsGroups.append(int(base))
        shardsGroups.append(int(complement))
        separateGroups(base, shardsGroups)
        separateGroups(complement, shardsGroups)
    else:
        shardsGroups.append(int(number))

for case in range(int(input())):
    total, desiredGroup = [int(num) for num in input().split()]

    if total >= desiredGroup:
        shardsGroupsDistribution = []
        separateGroups(total, shardsGroupsDistribution)
        if desiredGroup in shardsGroupsDistribution:
            print("SIM")
        else:
            print("NAO") 
    else:
        print("NAO")