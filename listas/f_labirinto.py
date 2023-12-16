relicCoords = []

i = 0
while True:
    line = input()
    if line == "Fim do labirinto":
        break
    line = line.split(" ")
    
    for j in range(len(line)):
        if line[j] == "1":
            relicCoords.append([i, j])

    i += 1

if len(relicCoords) > 0:
    print("Relíquias encontradas nos seguintes locais:")
    for coord in relicCoords:
        print(f"linha: {coord[0]}, coluna: {coord[1]}")
else:
    print("Nenhuma relíquia encontrada no labirinto.")