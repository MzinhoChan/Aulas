import random
import time
import os
import winsound
import threading

# --- CORES ANSI & EFEITOS ---
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
ROXO = "\033[95m"
CINZA = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

# --- SISTEMA DE ÁUDIO ARCADIA ---
def som_complexo(frequencias):
    def play():
        for freq, dur in frequencias:
            winsound.Beep(freq, dur)
    threading.Thread(target=play, daemon=True).start()

def efeito_som(tipo):
    if tipo == "passo":
        som_complexo([(180, 25)])
    elif tipo == "chave":
        som_complexo([(1200, 60), (1600, 90)])
    elif tipo == "dano":
        som_complexo([(250, 100), (150, 200)])
    elif tipo == "vitoria":
        som_complexo([(523, 100), (659, 100), (783, 100), (1046, 300)])
    elif tipo == "derrota":
        som_complexo([(300, 150), (200, 200), (100, 400)])
    elif tipo == "lanterna":
        som_complexo([(800, 40)])

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- CONFIGURAÇÃO DA MASMORRA ---
LARGURA = 13
ALTURA = 10

# Posição Inicial
px, py = 1, 1

# Elementos
tesouros = [[2, 6], [5, 2], [7, 10]]
inimigos = [
    {"pos": [3, 4], "dir": 1, "nome": "Espectro"},
    {"pos": [1, 9], "dir": -1, "nome": "Sombra"},
    {"pos": [6, 5], "dir": 1, "nome": "Rastejante"}
]

saida = [ALTURA - 2, LARGURA - 2]
chaves_coletadas = 0
total_chaves = len(tesouros)
hp = 3
passos = 0
lanterna_carga = 100
raio_visao = 2  # Névoa de Guerra (Visibilidade limitada)

# Mensagens de Lore Dinâmicas
narrativa = "Você acorda nas profundezas geladas. Apenas sua lanterna ilumina a escuridão..."
game_over = False
vitoria = False

limpar()
print(f"{BOLD}{ROXO}==================================================================")
print("     O SARCÓFAGO DAS SOMBRAS - ECO DE UM ABISMO")
print(f"=================================================================={RESET}")
print(f"{CIANO}O ar é denso. A escuridão envolve as paredes de pedra maciça.")
print("Apenas o que está ao alcance da sua lanterna pode ser visto...")
print(f"\n{AMARELO}Controles: [W] Cima | [S] Baixo | [A] Esquerda | [D] Direita | [F] Foco de Luz{RESET}\n")
input(f"{BOLD}Pressione ENTER para acender a lanterna e entrar...{RESET}")

while not game_over:
    limpar()
    
    # 1. Painel Atmosférico
    cor_hp = VERDE if hp == 3 else (AMARELO if hp == 2 else VERMELHO)
    barra_lanterna = f"{CIANO}" + "█" * (lanterna_carga // 10) + f"{CINZA}" + "░" * (10 - (lanterna_carga // 10)) + f"{RESET}"
    
    print(f"{BOLD}{CINZA}┌────────────────────────────────────────────────────────────────┐{RESET}")
    print(f"  🕯️  VITALIDADE: {cor_hp}{'❤️ ' * hp}{RESET}  │ 🔑 SECTORES: {chaves_coletadas}/{total_chaves}  │ 🔋 LANTERNA: [{barra_lanterna}] {lanterna_carga}%")
    print(f"{BOLD}{CINZA}└────────────────────────────────────────────────────────────────┘{RESET}")

    # 2. Renderização com NÉVOA DE GUERRA (Fog of War)
    print("   " + "──" * LARGURA)
    for y in range(ALTURA):
        linha = "  │"
        for x in range(LARGURA):
            # Cálculo de Distância (Névoa de Guerra em raio em torno do jogador)
            dist = abs(x - px) + abs(y - py)
            
            # Fora do alcance da luz -> Névoa total
            if dist > raio_visao and (x != px or y != py):
                linha += f"{CINZA}░░{RESET}"
                continue

            # Parede Externa
            if y == 0 or y == ALTURA - 1 or x == 0 or x == LARGURA - 1:
                linha += f"{AZUL}▓▓{RESET}"
            elif x == px and y == py:
                linha += f"{AMARELO}🧙{RESET}"
            elif [y, x] == saida:
                linha += "🚪" if chaves_coletadas == total_chaves else f"{VERMELHO}🔒{RESET}"
            elif [y, x] in tesouros:
                linha += f"{AMARELO}🗝️ {RESET}"
            elif any(e["pos"][0] == y and e["pos"][1] == x for e in inimigos):
                linha += f"{VERMELHO}👾{RESET}"
            else:
                linha += "  "
        linha += "│"
        print(linha)
    print("   " + "──" * LARGURA)

    # Log da Narrativa Ambiental
    print(f"\n{BOLD}{ROXO}📜 ECO DAS SOMBRAS:{RESET}")
    print(f"  > {narrativa}\n")

    # 3. Entrada de Comando
    acao = input(f"{BOLD}{AMARELO}Sua Ação (W/A/S/D | F - Aumentar Foco): {RESET}").strip().lower()
    
    nx, ny = px, py
    if acao == 'w': ny -= 1
    elif acao == 's': ny += 1
    elif acao == 'a': nx -= 1
    elif acao == 'd': nx += 1
    elif acao == 'f':
        if lanterna_carga >= 15:
            raio_visao = 4 if raio_visao == 2 else 2
            lanterna_carga -= 15
            efeito_som("lanterna")
            narrativa = "Você ajusta o foco da lanterna, rasgando temporariamente a escuridão!"
        else:
            narrativa = "A bateria da sua lanterna está muito fraca para focar!"
        continue
    else:
        continue

    # Movimentação e Física
    if 0 < nx < LARGURA - 1 and 0 < ny < ALTURA - 1:
        px, py = nx, ny
        passos += 1
        lanterna_carga = max(0, lanterna_carga - 1)
        efeito_som("passo")
        
        # Reduz raio de visão se lanterna acabar
        if lanterna_carga == 0:
            raio_visao = 1
            narrativa = "Sua lanterna apagou! A escuridão total o envolve..."

    # 4. IA dos Inimigos (Patrulha Inteligente)
    for inimi in inimigos:
        ey, ex = inimi["pos"]
        nova_ex = ex + inimi["dir"]
        
        if 0 < nova_ex < LARGURA - 1:
            inimi["pos"][1] = nova_ex
        else:
            inimi["dir"] *= -1
            inimi["pos"][1] += inimi["dir"]

    # 5. Interações
    # Coletar Chaves
    if [py, px] in tesouros:
        tesouros.remove([py, px])
        chaves_coletadas += 1
        lanterna_carga = min(100, lanterna_carga + 35) # Recarrega um pouco
        efeito_som("chave")
        narrativa = f"Você encontrou um Fragmento de Chave Reluzente! A luz se intensifica."

    # Encontro com Inimigo
    for inimi in inimigos:
        if inimi["pos"][0] == py and inimi["pos"][1] == px:
            hp -= 1
            efeito_som("dano")
            narrativa = f"UM {inimi['nome'].upper()} TE ALCANÇOU! As sombras atacam violentamente!"
            px, py = 1, 1 # Recua para o início da zona
            break

    # Condição de Vitória/Derrota
    if hp <= 0:
        game_over = True
        vitoria = False

    if [py, px] == saida and chaves_coletadas == total_chaves:
        game_over = True
        vitoria = True

# --- TELA FINAL ---
limpar()
print(f"\n{BOLD}{ROXO}==================================================================")
if vitoria:
    efeito_som("vitoria")
    print(f"{VERDE}🏆 O PORTÃO SE ABRE COM UM URRO METÁLICO! VOCÊ ESCAPOU DO ABISMO!")
    print(f"{CIANO}Estatísticas da Fuga: {passos} passos dados | {hp} vidas restantes.{RESET}")
else:
    efeito_som("derrota")
    print(f"{VERMELHO}☠️ A ESCURIDÃO O CONSUMIU COMPLETAMENTE...")
    print(f"{CINZA}Sua alma agora vaga indefinidamente pelos corredores de pedra.{RESET}")
print(f"{ROXO}=================================================================={RESET}\n")