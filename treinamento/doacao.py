packs = int(input())

rest = packs % 3
share = int((packs - rest) / 3)

print(share)
print(rest)