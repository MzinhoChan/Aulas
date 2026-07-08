import random

escolha_jogador = int(input("1- Pedra, 2- Papel, 3- Tesoura "))
escolha_computrador = random.randint(1,3)
print("Escolha do Jogador: ", escolha_jogador)
print("Escolha do Computador: ", escolha_computrador)

if escolha_jogador == escolha_computrador:
    print("Empate.")
elif (escolha_jogador == 1 and escolha_computrador == 3) or \
    (escolha_jogador == 2 and escolha_computrador== 1) or \
    (escolha_jogador == 3 and escolha_computrador == 2):
    print("Vitória.")
else:
    print("Derrota.")
