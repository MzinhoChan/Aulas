import random
import time
import os
import winsound
import threading

# --- CORES ANSI ---
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
ROXO = "\033[95m"
CINZA = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

# --- SISTEMA DE ÁUDIO ---
def som_complexo(frequencias):
    def play():
        for freq, dur in frequencias:
            winsound.Beep(freq, dur)
    threading.Thread(target=play, daemon=True).start()

def efeito_som(tipo):
    if tipo == "atq_leve":
        som_complexo([(400, 50), (800, 80)])
    elif tipo == "atq_pesado":
        som_complexo([(200, 100), (100, 200)])
    elif tipo == "magia":
        som_complexo([(600, 80), (900, 80), (1300, 120)])
    elif tipo == "cura":
        som_complexo([(800, 100), (1000, 100), (1200, 150)])
    elif tipo == "dano":
        som_complexo([(250, 120)])
    elif tipo == "vitoria":
        som_complexo([(523, 100), (659, 100), (783, 100), (1046, 300)])
    elif tipo == "derrota":
        som_complexo([(300, 150), (200, 200), (100, 400)])

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BANCO DE DADOS DE MONSTROS ---
BESTIARIO = {
    1: {"nome": "Goblin Esfomeado", "hp": 40, "hp_max": 40, "atq": 8, "xp": 25, "ouro": 15, "icone": "👺"},
    2: {"nome": "Lobo das Sombras", "hp": 65, "hp_max": 65, "atq": 12, "xp": 45, "ouro": 25, "icone": "🐺"},
    3: {"nome": "Guerreiro Esqueleto", "hp": 90, "hp_max": 90, "atq": 16, "xp": 70, "ouro": 45, "icone": "💀"},
    4: {"nome": "Orc Barbaro", "hp": 130, "hp_max": 130, "atq": 22, "xp": 110, "ouro": 70, "icone": "👹"},
    5: {"nome": "DRAGÃO ANCESTRAL", "hp": 250, "hp_max": 250, "atq": 32, "xp": 300, "ouro": 200, "icone": "🐉"}
}

# --- ATRIBUTOS DO JOGADOR ---
hero = {
    "nome": "",
    "classe": "",
    "nivel": 1,
    "xp": 0,
    "xp_prox": 50,
    "hp": 100,
    "hp_max": 100,
    "mp": 30,
    "mp_max": 30,
    "atq_base": 12,
    "def_base": 3,
    "ouro": 30,
    "pocoes_hp": 3,
    "pocoes_mp": 2,
    "andar": 1
}

def barra_status(atual, maximo, cor, icone):
    proporcao = int((atual / maximo) * 10)
    proporcao = max(0, min(10, proporcao))
    return f"{icone} {cor}" + "█" * proporcao + f"{CINZA}" + "░" * (10 - proporcao) + f"{RESET} ({atual}/{maximo})"

def criar_personagem():
    limpar()
    print(f"{BOLD}{ROXO}==================================================================")
    print("         ⚔️  CRÔNICAS DE ERANDOR - CRIAÇÃO DE HERÓI ⚔️")
    print(f"=================================================================={RESET}")
    hero["nome"] = input(f"{AMARELO}Digite o nome do seu Campeão: {RESET}").strip()
    if not hero["nome"]:
        hero["nome"] = "Guerreiro Sem Nome"

    print(f"\n{CIANO}Escolha sua Classe:{RESET}")
    print(" [1] Guerreiro   (Alto HP, Ataque Físico Forte)")
    print(" [2] Mago        (Pouco HP, Magia Devastadora)")
    print(" [3] Ladino      (Ataques Críticos e Alta Agilidade)")

    op = ""
    while op not in ["1", "2", "3"]:
        op = input(f"\n{AMARELO}Escolha (1-3): {RESET}").strip()

    if op == "1":
        hero["classe"] = "Guerreiro"
        hero["hp_max"] = 120
        hero["hp"] = 120
        hero["atq_base"] = 15
        hero["def_base"] = 5
    elif op == "2":
        hero["classe"] = "Mago"
        hero["mp_max"] = 60
        hero["mp"] = 60
        hero["atq_base"] = 8
        hero["def_base"] = 2
    elif op == "3":
        hero["classe"] = "Ladino"
        hero["hp_max"] = 90
        hero["hp"] = 90
        hero["atq_base"] = 18
        hero["def_base"] = 3

def menu_principal():
    limpar()
    print(f"{BOLD}{ROXO}==================================================================")
    print(f" 🏰 CIDADELA DE ERANDOR | ANDAR ATUAL: {hero['andar']}/5")
    print(f"=================================================================={RESET}")
    print(f" 👤 {BOLD}{hero['nome']}{RESET} ({hero['classe']} Nv.{hero['nivel']})")
    print(f" {barra_status(hero['hp'], hero['hp_max'], VERMELHO, '❤️')}")
    print(f" {barra_status(hero['mp'], hero['mp_max'], AZUL, '🧪')}")
    print(f" 🪙 OURO: {AMARELO}{hero['ouro']}{RESET} | 🎒 POÇÕES: HP({hero['pocoes_hp']}) MP({hero['pocoes_mp']})")
    print(f" ⭐ XP: {hero['xp']}/{hero['xp_prox']}")
    print(f"{ROXO}------------------------------------------------------------------{RESET}")
    print(" [1] ⚔️  Explorar a Masmorra (Batalhar)")
    print(" [2] 🏪 Visitar a Loja do Povoado")
    print(" [3] 💤 Descansar na Estalagem (Custa 15 Ouro)")
    print(" [0] 🚪 Sair do Jogo")
    print(f"{ROXO}------------------------------------------------------------------{RESET}")

def subir_nivel():
    if hero["xp"] >= hero["xp_prox"]:
        hero["nivel"] += 1
        hero["xp"] -= hero["xp_prox"]
        hero["xp_prox"] = int(hero["xp_prox"] * 1.6)
        hero["hp_max"] += 20
        hero["hp"] = hero["hp_max"]
        hero["mp_max"] += 10
        hero["mp"] = hero["mp_max"]
        hero["atq_base"] += 4
        hero["def_base"] += 2
        efeito_som("vitoria")
        print(f"\n{BOLD}{AMARELO}✨ LEVEL UP! Você alcançou o Nível {hero['nivel']}! Atributos aumentados!{RESET}")
        time.sleep(2)

def loja():
    while True:
        limpar()
        print(f"{BOLD}{AMARELO}==================================================================")
        print("               🏪 LOJA DE SUPRIMENTOS DO POVOADO")
        print(f"=================================================================={RESET}")
        print(f" Seu Ouro: {AMARELO}{hero['ouro']}🪙{RESET}\n")
        print(f" [1] Poção de HP (+50 HP)  - 15 Ouro (Possui: {hero['pocoes_hp']})")
        print(f" [2] Poção de MP (+30 MP)  - 15 Ouro (Possui: {hero['pocoes_mp']})")
        print(f" [3] Melhoria de Arma (+3 ATQ) - 50 Ouro")
        print(" [0] Voltar")
        print(f"{AMARELO}------------------------------------------------------------------{RESET}")
        
        op = input(f"{CIANO}Escolha o que comprar: {RESET}").strip()
        if op == "1" and hero["ouro"] >= 15:
            hero["ouro"] -= 15
            hero["pocoes_hp"] += 1
            efeito_som("cura")
        elif op == "2" and hero["ouro"] >= 15:
            hero["ouro"] -= 15
            hero["pocoes_mp"] += 1
            efeito_som("cura")
        elif op == "3" and hero["ouro"] >= 50:
            hero["ouro"] -= 50
            hero["atq_base"] += 3
            efeito_som("vitoria")
            print(f"{VERDE}Sua arma foi afiada! Ataque aumentou para {hero['atq_base']}!{RESET}")
            time.sleep(1.5)
        elif op == "0":
            break

def combate():
    m_id = min(hero["andar"], 5)
    m_data = BESTIARIO[m_id]
    monstro = {
        "nome": m_data["nome"],
        "hp": m_data["hp"],
        "hp_max": m_data["hp_max"],
        "atq": m_data["atq"],
        "xp": m_data["xp"],
        "ouro": m_data["ouro"],
        "icone": m_data["icone"]
    }

    log = f"Um {monstro['nome']} enfurecido surge das sombras!"

    while monstro["hp"] > 0 and hero["hp"] > 0:
        limpar()
        print(f"{BOLD}{VERMELHO}==================================================================")
        print(f"                      ⚔️ BATALHA EM ANDAMENTO ⚔️")
        print(f"=================================================================={RESET}")
        
        # Status Monstro
        print(f" {monstro['icone']} {BOLD}{monstro['nome']}{RESET}")
        print(f" {barra_status(monstro['hp'], monstro['hp_max'], VERMELHO, '💀')}\n")
        
        # Status Jogador
        print(f" 👤 {BOLD}{hero['nome']}{RESET}")
        print(f" {barra_status(hero['hp'], hero['hp_max'], VERDE, '❤️')}")
        print(f" {barra_status(hero['mp'], hero['mp_max'], AZUL, '🧪')}")
        print(f"{VERMELHO}------------------------------------------------------------------{RESET}")
        print(f"📜 LOG: {log}")
        print(f"{VERMELHO}------------------------------------------------------------------{RESET}")
        
        print(" [1] 🗡️  Ataque Físico")
        print(" [2] 🔮 Magia (10 MP)")
        print(" [3] 🧪 Usar Poção de HP")
        print(" [4] 🏃 Tentar Fugir")
        
        acao = input(f"\n{AMARELO}Sua Ação: {RESET}").strip()

        # Turno do Jogador
        dano_causado = 0
        if acao == "1":
            critico = 2 if random.random() < 0.2 else 1
            dano_causado = int((hero["atq_base"] + random.randint(-2, 4)) * critico)
            monstro["hp"] -= dano_causado
            efeito_som("atq_leve" if critico == 1 else "atq_pesado")
            msg_crit = " CRÍTICO!" if critico == 2 else ""
            log = f"Você atacou o {monstro['nome']} causando {dano_causado} de dano!{msg_crit}"

        elif acao == "2":
            if hero["mp"] >= 10:
                hero["mp"] -= 10
                dano_causado = int(hero["atq_base"] * 2.2)
                monstro["hp"] -= dano_causado
                efeito_som("magia")
                log = f"Você lançou uma bola de fogo devastadora causando {dano_causado} de dano mágico!"
            else:
                log = "Mana insuficiente!"
                continue

        elif acao == "3":
            if hero["pocoes_hp"] > 0:
                hero["pocoes_hp"] -= 1
                cura = 50
                hero["hp"] = min(hero["hp_max"], hero["hp"] + cura)
                efeito_som("cura")
                log = f"Você tomou uma poção e recuperou {cura} de HP!"
            else:
                log = "Você não tem poções de HP!"
                continue

        elif acao == "4":
            if random.random() < 0.5:
                log = "Você conseguiu fugir com sucesso!"
                time.sleep(1.5)
                return False
            else:
                log = "Falha ao fugir! O monstro bloqueou seu caminho!"

        time.sleep(1)

        # Turno do Monstro (Se continuar vivo)
        if monstro["hp"] > 0:
            dano_sofrido = max(1, monstro["atq"] - hero["def_base"] + random.randint(-2, 2))
            hero["hp"] -= dano_sofrido
            efeito_som("dano")
            log += f" | O {monstro['nome']} atacou te causando {dano_sofrido} de dano!"
            time.sleep(1)

    # Fim da Batalha
    if hero["hp"] <= 0:
        efeito_som("derrota")
        limpar()
        print(f"\n{BOLD}{VERMELHO}☠️ VOCÊ FOI DERROTADO PELO {monstro['nome'].upper()}... GAME OVER!{RESET}\n")
        return True

    if monstro["hp"] <= 0:
        efeito_som("vitoria")
        hero["xp"] += monstro["xp"]
        hero["ouro"] += monstro["ouro"]
        limpar()
        print(f"\n{BOLD}{VERDE}🏆 VITÓRIA! O {monstro['nome']} foi destruído!{RESET}")
        print(f"Recompensas: +{monstro['xp']} XP | +{monstro['ouro']} Ouro🪙")
        
        if hero["andar"] == m_id and hero["andar"] < 5:
            hero["andar"] += 1
            print(f"{CIANO}Você liberou o acesso ao Andar {hero['andar']} da Masmorra!{RESET}")

        subir_nivel()
        time.sleep(2.5)
        return False

# --- LOOP PRINCIPAL ---
criar_personagem()

while True:
    menu_principal()
    opcao = input(f"{AMARELO}Escolha sua ação: {RESET}").strip()

    if opcao == "1":
        game_over = combate()
        if game_over:
            break
    elif opcao == "2":
        loja()
    elif opcao == "3":
        if hero["ouro"] >= 15:
            hero["ouro"] -= 15
            hero["hp"] = hero["hp_max"]
            hero["mp"] = hero["mp_max"]
            efeito_som("cura")
            print(f"\n{VERDE}Você descansou na estalagem. HP e MP totalmente restaurados!{RESET}")
        else:
            print(f"\n{VERMELHO}Ouro insuficiente!{RESET}")
        time.sleep(1.5)
    elif opcao == "0":
        print(f"\n{CIANO}Saindo de Erandor... Até a próxima aventura!{RESET}")
        break