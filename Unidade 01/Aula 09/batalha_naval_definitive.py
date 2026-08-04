import random
import time
import os
import winsound
import threading

# --- CONFIGURAÇÕES DE CORES E INTERFACE ---
AZUL = "\033[94m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CINZA = "\033[90m"
CIANO = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

TAMANHO = 7
AGUA = f"{AZUL}~{RESET}"
ERRO = f"{CINZA}O{RESET}"
ACERTO = f"{VERMELHO}💥{RESET}"
MEU_NAVIO = f"{VERDE}🚢{RESET}"

FROTA_CONFIG = [
    {"nome": "Porta-Aviões", "tamanho": 3},
    {"nome": "Submarino", "tamanho": 2},
    {"nome": "Destroyer", "tamanho": 2}
]

# --- EFEITOS SONOROS ---
def som_efeito(tipo):
    def play():
        if tipo == "tiro":
            for f in range(600, 200, -50):
                winsound.Beep(f, 30)
        elif tipo == "acerto":
            winsound.Beep(120, 150)
            winsound.Beep(250, 200)
        elif tipo == "afundou":
            for f in [150, 200, 300, 400]:
                winsound.Beep(f, 80)
        elif tipo == "agua":
            winsound.Beep(180, 200)
    threading.Thread(target=play, daemon=True).start()

# --- ESTRUTURA DOS TABULEIROS ---
tabuleiro_jogador_visivel = [[AGUA for _ in range(TAMANHO)] for _ in range(TAMANHO)]
tabuleiro_jogador_oculto = [[None for _ in range(TAMANHO)] for _ in range(TAMANHO)]

tabuleiro_inimigo_visivel = [[AGUA for _ in range(TAMANHO)] for _ in range(TAMANHO)]
tabuleiro_inimigo_oculto = [[None for _ in range(TAMANHO)] for _ in range(TAMANHO)]

logs_combate = ["SISTEMA: Conexão estabelecida. Frota inimiga detectada!"]

# Posicionador de Frota
def posicionar_frota(tab_oculto, tab_visivel_proprio=None):
    for navio in FROTA_CONFIG:
        colocado = False
        while not colocado:
            orientacao = random.choice(["H", "V"])
            if orientacao == "H":
                r = random.randint(0, TAMANHO - 1)
                c = random.randint(0, TAMANHO - 1 - navio["tamanho"])
                posicoes = [(r, c + i) for i in range(navio["tamanho"])]
            else:
                r = random.randint(0, TAMANHO - 1 - navio["tamanho"])
                c = random.randint(0, TAMANHO - 1)
                posicoes = [(r + i, c) for i in range(navio["tamanho"])]

            if all(tab_oculto[pr][pc] is None for pr, pc in posicoes):
                instancia = {"nome": navio["nome"], "tamanho": navio["tamanho"], "vida": navio["tamanho"]}
                for pr, pc in posicoes:
                    tab_oculto[pr][pc] = instancia
                    if tab_visivel_proprio:
                        tab_visivel_proprio[pr][pc] = MEU_NAVIO
                colocado = True

# Inicialização das frotas
posicionar_frota(tabuleiro_jogador_oculto, tabuleiro_jogador_visivel)
posicionar_frota(tabuleiro_inimigo_oculto)

# Memória da IA
ia_pilha_alvos = []
ia_tiros_dados = set()

def ia_escolher_tiro():
    """IA com busca sequencial inteligente ao acertar um alvo"""
    while ia_pilha_alvos:
        r, c = ia_pilha_alvos.pop(0)
        if (r, c) not in ia_tiros_dados and 0 <= r < TAMANHO and 0 <= c < TAMANHO:
            ia_tiros_dados.add((r, c))
            return r, c
            
    while True:
        r = random.randint(0, TAMANHO - 1)
        c = random.randint(0, TAMANHO - 1)
        if (r, c) not in ia_tiros_dados:
            ia_tiros_dados.add((r, c))
            return r, c

def exibir_interface_dupla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{BOLD}{CIANO}=======================================================================")
    print("       🛰️  CENTRAL DE COMANDO - MODO DE COMBATE IA REATIVA")
    print(f"======================================================================={RESET}\n")

    header_jog = "   " + " ".join([f"{i}" for i in range(TAMANHO)])
    header_ini = "   " + " ".join([f"{i}" for i in range(TAMANHO)])
    print(f"{BOLD}{VERDE}      [SUA FROTA]{RESET}                      {BOLD}{VERMELHO}[RADAR INIMIGO]{RESET}")
    print(f" {header_jog}          {header_ini}")

    for idx in range(TAMANHO):
        linha_jog = " ".join(tabuleiro_jogador_visivel[idx])
        linha_ini = " ".join(tabuleiro_inimigo_visivel[idx])
        print(f" {BOLD}{idx}{RESET} │ {linha_jog} │      {BOLD}{idx}{RESET} │ {linha_ini} │")

    print(f"\n{BOLD}📜 RELATÓRIO DE COMBATE:{RESET}")
    for log in logs_combate[-3:]:
        print(f"  > {log}")
    print()

navios_inimigos = len(FROTA_CONFIG)
navios_jogador = len(FROTA_CONFIG)

while navios_inimigos > 0 and navios_jogador > 0:
    exibir_interface_dupla()
    
    cmd = input(f"{BOLD}{AMARELO}🎯 Digite seu tiro [Linha Coluna] (ex: 2 3): {RESET}").split()
    if len(cmd) < 2:
        continue

    try:
        r, c = int(cmd[0]), int(cmd[1])
    except ValueError:
        continue

    if r < 0 or r >= TAMANHO or c < 0 or c >= TAMANHO or tabuleiro_inimigo_visivel[r][c] != AGUA:
        logs_combate.append(f"{AMARELO}Coordenada [{r},{c}] inválida ou já disparada!{RESET}")
        continue

    # --- TURNO DO JOGADOR ---
    som_efeito("tiro")
    alvo_ini = tabuleiro_inimigo_oculto[r][c]
    if alvo_ini:
        tabuleiro_inimigo_visivel[r][c] = ACERTO
        alvo_ini["vida"] -= 1
        if alvo_ini["vida"] == 0:
            navios_inimigos -= 1
            som_efeito("afundou")
            logs_combate.append(f"{VERMELHO}💥 VOCÊ AFUNDOU o {alvo_ini['nome']} inimigo!{RESET}")
        else:
            som_efeito("acerto")
            logs_combate.append(f"{VERMELHO}🔥 HIT! Você atingiu o {alvo_ini['nome']} inimigo em [{r},{c}]!{RESET}")
    else:
        tabuleiro_inimigo_visivel[r][c] = ERRO
        som_efeito("agua")
        logs_combate.append(f"{AZUL}🌊 Seu tiro em [{r},{c}] caiu no mar.{RESET}")

    if navios_inimigos == 0:
        break

    # --- TURNO DA IA (CONTRA-ATAQUE) ---
    time.sleep(1)
    ia_r, ia_c = ia_escolher_tiro()
    alvo_jog = tabuleiro_jogador_oculto[ia_r][ia_c]

    if alvo_jog:
        tabuleiro_jogador_visivel[ia_r][ia_c] = ACERTO
        alvo_jog["vida"] -= 1
        
        # Adiciona posições adjacentes para caça nos próximos turnos
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            ia_pilha_alvos.append((ia_r + dr, ia_c + dc))

        if alvo_jog["vida"] == 0:
            navios_jogador -= 1
            logs_combate.append(f"{VERMELHO}☠️ A IA AFUNDOU o seu {alvo_jog['nome']} em [{ia_r},{ia_c}]!{RESET}")
        else:
            logs_combate.append(f"{AMARELO}⚠️ A IA ATINGIU o seu {alvo_jog['nome']} em [{ia_r},{ia_c}]!{RESET}")
    else:
        tabuleiro_jogador_visivel[ia_r][ia_c] = ERRO
        logs_combate.append(f"{CINZA}🛡️ O contra-ataque da IA em [{ia_r},{ia_c}] errou sua frota.{RESET}")

# --- FIM DE JOGO ---
exibir_interface_dupla()

if navios_inimigos == 0:
    print(f"\n{BOLD}{VERDE}🏆 VITÓRIA MILITAR! Você destruiu toda a frota da IA!{RESET}\n")
else:
    print(f"\n{BOLD}{VERMELHO}☠️ DERROTA! A IA afundou todas as suas embarcações!{RESET}\n")