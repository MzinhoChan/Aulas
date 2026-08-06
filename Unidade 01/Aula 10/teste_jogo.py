import json  # Biblioteca para salvar e carregar o progresso do jogador
import os  # Biblioteca para checar se o arquivo de save existe no computador
import random  # Biblioteca para sortear variação de ouro/XP ganhos


# --- FUNÇÕES DE SALVAMENTO ---


def salvar_jogo(player):
    # Salva o dicionário com todas as informações atuais do jogador
    with open("save_resgate.txt", "w") as arquivo:
        json.dump(player, arquivo)
    print("\n[!] Progresso salvo com sucesso! O resgate pode continuar mais tarde.")


def carregar_jogo():
    # Verifica se existe um arquivo salvo para carregar
    if os.path.exists("save_resgate.txt"):
        with open("save_resgate.txt", "r") as arquivo:
            player = json.load(arquivo)
        print(
            f"\n[!] Save carregado! Você está no {player['andar']}º andar buscando {player['nome_filha']}!"
        )
        return player
    else:
        print("\n[!] Nenhum arquivo de save encontrado.")
        return None


# --- SISTEMA DE LOJA / FERREIRO ---


def visitar_ferreiro(player):
    while True:
        print("\n" + "=" * 35)
        print(f"--- FERREIRO DO CASTELO --- (Seu Ouro: {player['ouro']} G)")
        print(f"1. Melhorar Espada (+5 Atq)  - Custo: {player['custo_espada']} Ouro (Nível {player['lvl_espada']})")
        print(f"2. Melhorar Armadura (+20 HP) - Custo: {player['custo_armadura']} Ouro (Nível {player['lvl_armadura']})")
        print("3. Comprar Poção de Cura (+30 HP) - Custo: 15 Ouro")
        print("4. Voltar para o Corredor")
        print("=" * 35)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Melhora o ataque da espada se tiver ouro suficiente
            if player["ouro"] >= player["custo_espada"]:
                player["ouro"] -= player["custo_espada"]
                player["ataque_base"] += 5
                player["lvl_espada"] += 1
                player["custo_espada"] = int(player["custo_espada"] * 1.5)  # Aumenta o preço da próxima melhoria
                print(f"\n[!] Sua espada foi forjada! Novo ataque base: {player['ataque_base']}")
            else:
                print("\n[!] Ouro insuficiente!")

        elif opcao == "2":
            # Melhora a vida máxima com armadura nova
            if player["ouro"] >= player["custo_armadura"]:
                player["ouro"] -= player["custo_armadura"]
                player["vida_max"] += 20
                player["vida"] += 20  # Aumenta a vida atual também
                player["lvl_armadura"] += 1
                player["custo_armadura"] = int(player["custo_armadura"] * 1.5)
                print(f"\n[!] Sua armadura foi reforçada! Nova Vida Máxima: {player['vida_max']}")
            else:
                print("\n[!] Ouro insuficiente!")

        elif opcao == "3":
            # Compra poção
            if player["ouro"] >= 15:
                player["ouro"] -= 15
                player["pocoes"] += 1
                print("\n[!] Você comprou 1 Poção de Cura!")
            else:
                print("\n[!] Ouro insuficiente!")

        elif opcao == "4":
            break
        else:
            print("Opção inválida!")


# --- SISTEMA DE XP E NÍVEL ---


def checar_subida_de_nivel(player):
    # Enquanto o XP atual for maior ou igual ao XP necessário, o jogador sobe de nível
    while player["xp"] >= player["xp_proximo_nivel"]:
        player["xp"] -= player["xp_proximo_nivel"]  # Desconta o XP consumido
        player["nivel"] += 1
        player["xp_proximo_nivel"] = int(player["xp_proximo_nivel"] * 1.4)  # Próximo nível precisa de mais XP

        # Bônus por subir de nível
        player["ataque_base"] += 3
        player["vida_max"] += 15
        player["vida"] = player["vida_max"]  # Cura totalmente ao subir de nível

        print("\n" + "*" * 40)
        print(f"  *** SUBIU DE NÍVEL! Você agora é Nível {player['nivel']}! ***")
        print(f"  +15 Vida Máxima | +3 Ataque Base (Vida restaurada!)")
        print("*" * 40)


# --- COMBATE E INIMIGOS ---


def criar_inimigo(andar):
    # O andar 11 contém o chefe final
    if andar == 11:
        return {
            "nome": "Rei Sequestrador (CHEFE FINAL)",
            "vida": 250,
            "ataque": 22,
            "xp": 500,
            "ouro": 200,
        }
    else:
        # Status dos guardas escalam de acordo com o andar
        return {
            "nome": f"Guardião do {andar}º Andar",
            "vida": 25 + (andar * 12),
            "ataque": 5 + (andar * 3),
            "xp": 20 + (andar * 15),
            "ouro": 10 + (andar * 8),
        }


def batalhar(player):
    inimigo = criar_inimigo(player["andar"])
    print(f"\n--- {player['andar']}º ANDAR DO CASTELO ---")
    print(f"Um {inimigo['nome']} apareceu no seu caminho!")

    while player["vida"] > 0 and inimigo["vida"] > 0:
        print(f"\nSua Vida: {player['vida']}/{player['vida_max']} | Poções: {player['pocoes']}")
        print(f"Inimigo: {inimigo['nome']} | Vida: {inimigo['vida']}")
        print("1. Atacar com Espada")
        print("2. Usar Poção de Cura (+30 HP)")
        print("3. Recuar para o corredor")

        opcao = input("Escolha: ")

        if opcao == "1":
            # Dano base + pequenas variações
            dano_causado = player["ataque_base"] + random.randint(0, 3)
            inimigo["vida"] -= dano_causado
            print(f"\nVocê atacou o {inimigo['nome']} e causou {dano_causado} de dano!")

            # Inimigo derrotado
            if inimigo["vida"] <= 0:
                print(f"\n[VITÓRIA] Você derrotou o {inimigo['nome']}!")
                
                # Recompensas de Ouro e XP
                player["ouro"] += inimigo["ouro"]
                player["xp"] += inimigo["xp"]
                print(f"Recompensas: +{inimigo['ouro']} Ouro | +{inimigo['xp']} XP")

                # Checa se o jogador subiu de nível com esse XP
                checar_subida_de_nivel(player)

                # Condição de Vitória do Jogo Final
                if player["andar"] == 11:
                    print("\n" + "=" * 50)
                    print(f"PARABÉNS, {player['nome']}!")
                    print(f"Você derrotou o Rei, abriu a gaiola e salvou sua filha {player['nome_filha']}!")
                    print("Vocês escaparam do castelo e voltaram para casa em segurança.")
                    print("=" * 50)
                    if os.path.exists("save_resgate.txt"):
                        os.remove("save_resgate.txt")
                    exit()
                else:
                    player["andar"] += 1
                    print(f"\nA porta para o {player['andar']}º Andar foi destrancada!")
                    break

            # Inimigo contra-ataca
            dano_recebido = inimigo["ataque"]
            player["vida"] -= dano_recebido
            print(f"O {inimigo['nome']} te atingiu e causou {dano_recebido} de dano!")

        elif opcao == "2":
            if player["pocoes"] > 0:
                player["pocoes"] -= 1
                player["vida"] = min(player["vida_max"], player["vida"] + 30)
                print(f"\nVocê tomou uma poção! Vida atual: {player['vida']}/{player['vida_max']}")
                
                # O inimigo ainda ataca na rodada de cura
                player["vida"] -= inimigo["ataque"]
                print(f"O {inimigo['nome']} atacou enquanto você se curava e causou {inimigo['ataque']} de dano!")
            else:
                print("\nVocê não tem poções restantes!")

        elif opcao == "3":
            print("\nVocê recuou em segurança.")
            break
        else:
            print("Opção inválida!")

        # Game Over
        if player["vida"] <= 0:
            print(f"\n[GAME OVER] Você caiu em batalha... {player['nome_filha']} continua presa no topo.")
            break


# --- MENU PRINCIPAL ---


def menu_principal():
    print("=========================================")
    print("      RESGATE NO CASTELO DOS 11 ANDARES  ")
    print("=========================================")
    print("1. Novo Jogo")
    print("2. Carregar Jogo Salvo")

    opcao = input("Escolha: ")
    player = None

    if opcao == "2":
        player = carregar_jogo()

    if player is None:
        nome_pai = input("\nDigite o seu nome (Pai/Mãe): ")
        nome_filha = input("Digite o nome da sua filha (ou Pressione Enter para 'Sofia'): ")
        if not nome_filha.strip():
            nome_filha = "Sofia"

        # Dicionário do Jogador com todas as estatísticas
        player = {
            "nome": nome_pai,
            "nome_filha": nome_filha,
            "andar": 1,
            "nivel": 1,
            "xp": 0,
            "xp_proximo_nivel": 50,
            "vida": 70,
            "vida_max": 70,
            "ataque_base": 12,
            "ouro": 30,
            "pocoes": 2,
            "lvl_espada": 1,
            "custo_espada": 25,
            "lvl_armadura": 1,
            "custo_armadura": 30,
        }

    # Loop de opções no corredor do castelo
    while player["vida"] > 0:
        print(f"\n--- CORREDOR DO CASTELO (Objetivo: Salvar {player['nome_filha']}) ---")
        print(f"Andar Atual: {player['andar']}/11 | Nível: {player['nivel']} | Ouro: {player['ouro']} G")
        print("1. Entrar na próxima sala (Batalha)")
        print("2. Visitar Ferreiro (Melhorar Armas/Armaduras)")
        print("3. Ver Status Detalhados")
        print("4. Salvar Jogo")
        print("5. Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            batalhar(player)
        elif escolha == "2":
            visitar_ferreiro(player)
        elif escolha == "3":
            print("\n" + "=" * 30)
            print(f"Herói: {player['nome']}")
            print(f"Filha a resgatar: {player['nome_filha']}")
            print(f"Nível: {player['nivel']} (XP: {player['xp']}/{player['xp_proximo_nivel']})")
            print(f"Andar Atual: {player['andar']}/11")
            print(f"Vida: {player['vida']}/{player['vida_max']}")
            print(f"Ataque: {player['ataque_base']}")
            print(f"Ouro: {player['ouro']} G")
            print(f"Poções: {player['pocoes']}")
            print(f"Nível da Espada: {player['lvl_espada']}")
            print(f"Nível da Armadura: {player['lvl_armadura']}")
            print("=" * 30)
        elif escolha == "4":
            salvar_jogo(player)
        elif escolha == "5":
            print("Até logo! Sua filha espera por você.")
            break
        else:
            print("Opção inválida!")


# Executa o jogo
menu_principal()