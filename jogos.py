import adivinhacao

print("*********************************")
print("Escolha seu jovo!")
print("*********************************")

print("Deseja jovar advinhacao?")

jogo = int(input("(1)Sim / (0) Não ?"))

if(jogo == 1):
    adivinhacao.jogar_advinhacao()
