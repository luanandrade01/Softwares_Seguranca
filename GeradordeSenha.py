import random, string, time

while True:
    tamanho = int(input("Digite o tamanho de senha que você deseja ou '0' para SAIR: "))
    if tamanho == 0:
        print("Obrigado por utilizar nosso programa. Saindo..")
        time.sleep(2)
        break
    elif tamanho < 16:
        print("Digite um tamanho maior, por exemplo 16")
    else:
        print("OK! Senha sendo gerada...")
        time.sleep(5)
        chars = string.ascii_letters + string.digits + '!@#$%*(){}Ç~-=+'

        rnd = random.SystemRandom()

        print(''.join(rnd.choice(chars) for i in range(tamanho)))
