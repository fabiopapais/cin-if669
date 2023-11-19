showName = input()
vipCount = 0
while True:
    code = input()
    if code == "1000":
        vipCount += 1
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
    elif code == "1001":
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    elif code == "1002":
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
    elif code == "1003":
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
    elif code == "1004":
        print("Esse código não existe! O sistema quebrou...")
        print("Vamos aguardar até que o suporte nos ajude.")
        while True:
            if input() == "Ajudou":
                break
            else:
                print("Ainda não...")
        break
    elif code == "0000":
        break
print(f"O show da Taylor Swift será em {showName} e contará com {vipCount} VIPs!")