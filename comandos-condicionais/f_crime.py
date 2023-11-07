life, weaponPower, fightHability, surprisePower = int(input()), int(input()), int(input()), int(input())
villainWeaponPower, villainFightHability, villainSurprisePower, villainDefense = int(input()), int(input()), int(input()), int(input())

if (weaponPower > villainWeaponPower and 
    fightHability > villainFightHability and 
    surprisePower > villainSurprisePower):
    print("Ainda bem que deu tudo certo, está quase em casa")
else:
    life -= villainDefense
    if life > 0:
        print("Rápido, corra antes que ele vá atrás de você!")
        weaponPower -= weaponPower * 0.05
        fightHability -= fightHability * 0.05
        surprisePower += surprisePower * 0.05
    else:
        print("Oh, no! Acabou pra mim")

# vingança
if life > 0:
    villainWeaponPower, villainFightHability, villainSurprisePower = int(input()), int(input()), int(input())
    if (weaponPower >= villainWeaponPower or 
        fightHability >= villainFightHability or 
        surprisePower >= villainSurprisePower):
        print("Casa, aqui vou eu")
    else:
        print("Oh, no! Acabou pra mim")
