print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_tentativas = 3

while (total_tentativas > 0):
    print("Rodada: ", total_tentativas)
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    
    # converter string para int
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você erro! o seu chute foi maior do que o número secreto")
        elif(menor):
            print("Você erro! o seu chute foi menor do que o número secreto")
    total_tentativas = total_tentativas - 1
