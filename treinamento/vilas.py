x_steve, z_steve = abs(int(input())), abs(int(input()))

x_hogsmade, z_hogsmade = 34, 220
x_kakariko, z_kakariko = 0, 0
x_solitude, z_solitude = 140, 456

def dist(xz_destination, xz_origin):
    return "%.2f" % (
        (xz_destination[0] - xz_origin[0])**2 +
        (xz_destination[1] - xz_origin[1])**2
    )**(1/2)

print(f"Distancia para Hogsmeade: {dist((x_hogsmade, z_hogsmade), (x_steve, z_steve))}")
print(f"Distancia para Kakariko: {dist((x_kakariko, z_kakariko), (x_steve, z_steve))}")
print(f"Distancia para Solitude: {dist((x_solitude, z_solitude), (x_steve, z_steve))}")