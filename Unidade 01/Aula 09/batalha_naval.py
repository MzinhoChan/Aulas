import random

mapa_jogador = [
    ["~","~","~"],
    ["~","~","~"],
    ["~","~","~"]
]

mapa_computador = [
    ["~","~","~"],
    ["~","~","~"],
    ["~","~","~"]
]

# Jogador escolhe onde posicionar o barquinho!
print("Onde colocar o barquinho?")
LINHA_INICIAL_JOGADOR = int(input("Escolha uma linha: "))
COLUNA_INICIAL_JOGADOR = int(input("Escolha uma coluna: "))

mapa_jogador[LINHA_INICIAL_JOGADOR][COLUNA_INICIAL_JOGADOR] = "O"

# Computador escolhe onde posicionar o barquinho!
LINHA_INICIAL_COMPUTADOR = random.randint(0,2)
COLUNA_INICIAL_COMPUTADOR = random.randint(0,2)

# Inicia o  loop das escolhas
while True:
    print("Sua vez de Atacar!")
    escolha_linha_jogador = int(input("Escolha uma linha: "))
    escolha_coluna_jogador = int(input("Escolha uma coluna: "))
    
    if (escolha_linha_jogador == LINHA_INICIAL_COMPUTADOR) and \
    (escolha_coluna_jogador == COLUNA_INICIAL_COMPUTADOR):
        print("Você Ganhou!")
        break
    else:
        print("Você Errou!")
        mapa_computador[escolha_linha_jogador][escolha_coluna_jogador] = "X"

        for linha in mapa_computador:
            print(" ".join(linha))

    print("É a vez do Computador!")

    while True:
        escolha_linha_computador = random.randint(0,2)
        escolha_coluna_computador = random.randint(0,2)
        if mapa_jogador[escolha_linha_computador][escolha_coluna_computador] == "X":
            continue
        else:
            break


    if escolha_linha_computador == LINHA_INICIAL_JOGADOR and \
    escolha_coluna_computador == COLUNA_INICIAL_JOGADOR:
        print("Você Perdeu!")
        break
    else:
        mapa_jogador[escolha_linha_computador][escolha_coluna_computador] = "X"
        for linha in mapa_jogador:
            print(" ".join(linha))

    
