informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]

codeStr = input()

for i in range(len(codeStr)):

    name = informacoes_deuses[0][int(codeStr[i])]
    if name == "Atenas" or name == "Afrodite":
        print(f"Deusa:{name}")
    else:
        print(f"Deus:{name}")
    print(f"Poder:{informacoes_deuses[1][int(codeStr[i])]}")
    
    if i != len(codeStr) - 1:
        print(f"Artefato:{informacoes_deuses[2][int(codeStr[i])]}\n")
    else:
        print(f"Artefato:{informacoes_deuses[2][int(codeStr[i])]}")