name1, points1, critic1 = input(), int(input()), input()
name2, points2, critic2 = input(), int(input()), input()
name3, points3, critic3 = input(), int(input()), input()

worstFilm = ""

if critic1 == "boa":
    points1 *= 1.25
elif critic1 == "media":
    points1 *= 1.00
elif critic1 == "ruim":
    points1 *= 0.75
elif critic1 == "pessima":
    points1 = 0
    worstFilm = name1

if critic2 == "boa":
    points2 *= 1.25
elif critic2 == "media":
    points2 *= 1.00
elif critic2 == "ruim":
    points2 *= 0.75
elif critic2 == "pessima":
    points2 = 0
    worstFilm = name2

if critic3 == "boa":
    points3 *= 1.25
elif critic3 == "media":
    points3 *= 1.00
elif critic3 == "ruim":
    points3 *= 0.75
elif critic3 == "pessima":
    points3 = 0
    worstFilm = name3

film1, film2, film3 = "", "", ""

# Cálculo rápido da maior pontuação, sem usar max
maxHalf1 = (points1 + points2 + abs(points1 - points2)) / 2
maxHalf2 = (points2 + points3 + abs(points2 - points3)) / 2
filmPoints1 = (maxHalf1 + maxHalf2 + abs(maxHalf1 - maxHalf2)) / 2

# Cálculo rápido da menor pontuação, sem usar min
minHalf1 = (points1 + points2 - abs(points1 - points2)) / 2
minHalf2 = (points2 + points3 - abs(points2 - points3)) / 2
filmPoints3 = (minHalf1 + minHalf2 - abs(minHalf1 - minHalf2)) / 2

# pegar nome do filme max
if filmPoints1 == points1:
    film1 = name1
elif filmPoints1 == points2:
    film1 = name2
elif filmPoints1 == points3:
    film1 = name3

# pegar nome do filme min
if filmPoints3 == points1:
    film3 = name1
elif filmPoints3 == points2:
    film3 = name2
elif filmPoints3 == points3:
    film3 = name3

# pegar nome do filme intermediario
if (film1 == name1 and film3 == name3) or (film1 == name3 and film3 == name1):
    film2 = name2
elif (film1 == name1 and film3 == name2) or (film1 == name2 and film3 == name1):
    film2 = name3
elif (film1 == name2 and film3 == name3) or (film1 == name3 and film3 == name2):
    film2 = name1

print("**** TOP 3 FILMES ****")
print(f"{film1} está em 1° lugar")
print(f"{film2} está em 2° lugar")
print(f"{film3} está em 3° lugar")

if worstFilm != "":
    print(f"{worstFilm} teve uma crítica péssima")
