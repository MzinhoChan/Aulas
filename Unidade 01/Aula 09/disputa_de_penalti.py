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
BOLD = "\033[1m"
RESET = "\033[0m"

# --- VARIÁVEIS DE CHEAT ---
cheats_ativos = {
    "raio_x": False,
    "super_chute": False,
    "goleiro_divino": False
}

# --- SONS ---
def som_efeito(tipo):
    def play():
        if tipo == "apito":
            winsound.Beep(1200, 200)
            winsound.Beep(1600, 400)
        elif tipo == "corrida":
            for _ in range(4):
                winsound.Beep(200, 50)
                time.sleep(0.05)
        elif tipo == "chute":
            winsound.Beep(150, 120)
        elif tipo == "gol":
            for f in [400, 600, 800, 1200]:
                winsound.Beep(f, 120)
        elif tipo == "defesa":
            winsound.Beep(300, 150)
            winsound.Beep(150, 300)
        elif tipo == "trave":
            winsound.Beep(1800, 80)
            winsound.Beep(1200, 150)
        elif tipo == "fora":
            winsound.Beep(250, 300)
        elif tipo == "barreira":
            winsound.Beep(100, 200)
            winsound.Beep(80, 200)
        elif tipo == "cheat":
            winsound.Beep(2000, 100)
            winsound.Beep(2500, 150)
    threading.Thread(target=play, daemon=True).start()

POSICOES = {
    "1": ("Esq Alto", 0, 0),
    "2": ("Meio Alto", 0, 1),
    "3": ("Dir Alto", 0, 2),
    "4": ("Esq Baixo", 1, 0),
    "5": ("Meio Baixo", 1, 1),
    "6": ("Dir Baixo", 1, 2)
}

EFEITOS_FALTA = {
    "1": "Curva Esq",
    "2": "Direto / Colocado",
    "3": "Curva Dir",
    "4": "Folha Seca (Trivela)"
}

historico_jog = []
historico_ia = []

def formatar_historico(historico):
    res = ""
    for status in historico:
        res += "🟢 " if status == "GOL" else "🔴 "
    res += "⚪ " * (5 - len(historico))
    return res.strip()

def checar_fim_matematico(placar_j, placar_i, cob_j, cob_i):
    restantes_j = 5 - cob_j
    restantes_i = 5 - cob_i

    if placar_j + restantes_j < placar_i:
        return True, "IA_CAMPEA"
    if placar_i + restantes_i < placar_j:
        return True, "JOGADOR_CAMPEAO"

    return False, None

def menu_cheats():
    som_efeito("cheat")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{BOLD}{ROXO}=========================================")
        print("          👾 MENU DE TRAPAÇAS 👾")
        print(f"========================================={RESET}")
        print(f" [1] Raio-X no Goleiro    : [{'LIGADO' if cheats_ativos['raio_x'] else 'DESLIGADO'}]")
        print(f" [2] Super Chute 100% Gol : [{'LIGADO' if cheats_ativos['super_chute'] else 'DESLIGADO'}]")
        print(f" [3] Goleiro Divino       : [{'LIGADO' if cheats_ativos['goleiro_divino'] else 'DESLIGADO'}]")
        print(" [0] Voltar ao Jogo")
        print(f"{ROXO}-----------------------------------------{RESET}")
        
        op = input(f"{AMARELO}Escolha uma opção: {RESET}").strip()
        if op == "1":
            cheats_ativos["raio_x"] = not cheats_ativos["raio_x"]
        elif op == "2":
            cheats_ativos["super_chute"] = not cheats_ativos["super_chute"]
        elif op == "3":
            cheats_ativos["goleiro_divino"] = not cheats_ativos["goleiro_divino"]
        elif op == "0":
            break

def renderizar_estadio(gol_matriz, placar_jog, placar_ia, rodada, modo_jogo, forca=0, narracao="", fase="", barreira_pos=""):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    torcida = "".join(random.choice(["░", "▒", "▓", "█", "🤹", "🙌", "👏"]) for _ in range(35))
    nome_modo = "COBRANÇAS DE FALTA" if modo_jogo == "FALTAS" else "DECISÃO POR PÊNALTIS"
    
    print(f" {AMARELO}{torcida}{RESET}")
    print(f"{BOLD}{CIANO}=================================================================")
    print(f"      🏆 FINAL DA COPA - {nome_modo} 🏆")
    print(f"================================================================={RESET}")

    vis_jog = formatar_historico(historico_jog)
    vis_ia = formatar_historico(historico_ia)
    
    status_cheat = f" {ROXO}[👾 CHEATS]{RESET}" if any(cheats_ativos.values()) else ""
    print(f" {BOLD}RODADA: {min(rodada, 5)}/5{RESET}{status_cheat}")
    print(f" ⚽ {VERDE}{BOLD}VOCÊ: [{placar_jog}]{RESET}  -> {vis_jog}")
    print(f" 🤖 {VERMELHO}{BOLD}IA  : [{placar_ia}]{RESET}  -> {vis_ia}")
    print(f"{CIANO}-----------------------------------------------------------------{RESET}")

    # TRAVE E GOL
    print("            ┌─────────────────────────────────────────┐")
    print("            │                T R A V E                │")
    print("            ├──────────────┬──────────────┬───────────┤")
    print(f"            │  {gol_matriz[0][0]}       │  {gol_matriz[0][1]}       │  {gol_matriz[0][2]}    │")
    print("            ├──────────────┼──────────────┼───────────┤")
    print(f"            │  {gol_matriz[1][0]}       │  {gol_matriz[1][1]}       │  {gol_matriz[1][2]}    │")
    print("            └──────┬───────┴──────────────┴───────┬───┘")
    print("                   │                              │")
    
    # BARREIRA DE FALTAS (SE ESTIVER NO MODO FALTAS)
    if modo_jogo == "FALTAS":
        barreira_vis = "       [🧍🧍🧍 Barreira na Esquerda]" if barreira_pos == "Esq" else "       [Barreira na Direita 🧍🧍🧍]"
        print(f"{AMARELO}{barreira_vis}{RESET}")
    
    if fase == "preparacao":
        print(f"                               {VERDE}⚽{RESET}")
        distancia = "[ Barreira posicionada a 9.15m ]" if modo_jogo == "FALTAS" else "[ Marca do Pênalti ]"
        print(f"                         {distancia}")
    elif fase == "corrida":
        print(f"                            {VERDE}🏃... ⚽{RESET}")
    elif fase == "impacto":
        print(f"                               {VERMELHO}💥⚽{RESET}")
    else:
        print("                                   ")

    if forca > 0:
        barras = int(forca / 10)
        cor_barra = VERDE if forca < 80 else (AMARELO if forca < 95 else VERMELHO)
        barra_vis = cor_barra + "█" * barras + "░" * (10 - barras) + RESET
        print(f"\n   POTÊNCIA DO CHUTE: [{barra_vis}] {forca}%")
    else:
        print("\n")

    print(f"{BOLD}{ROXO}📻 LOCUTOR AO VIVO:{RESET}")
    print(f"  > {narracao}")
    print(f"{CIANO}-----------------------------------------------------------------{RESET}\n")

def animar_chute(pos_chute_key, forca, efeito_escolhido, pos_goleiro_key, placar_jog, placar_ia, rodada, modo_jogo, barreira_pos="", sou_batedor=True):
    gol = [["  .  ", "  .  ", "  .  "],
           ["  .  ", "  .  ", "  .  "]]

    _, r_b, c_b = POSICOES[pos_chute_key]
    _, r_g, c_g = POSICOES[pos_goleiro_key]

    som_efeito("apito")
    renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "O juiz autoriza a cobrança!", fase="preparacao", barreira_pos=barreira_pos)
    time.sleep(1.2)

    som_efeito("corrida")
    renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "Tomou distância... corre para a bola!", fase="corrida", barreira_pos=barreira_pos)
    time.sleep(0.8)

    som_efeito("chute")

    # CHEATS
    if sou_batedor and cheats_ativos["super_chute"]:
        gol[r_b][c_b] = f"{VERDE} ⚽ {RESET}"
        som_efeito("gol")
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, 100, "SUPER CHUTE! A bola passou como um foguete sem chance para ninguém!", fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return True

    if not sou_batedor and cheats_ativos["goleiro_divino"]:
        gol[r_b][c_b] = f"{VERMELHO} 💥 {RESET}"
        gol[r_g][c_g] = f"{AMARELO} 🧤 {RESET}"
        som_efeito("defesa")
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "GOLEIRO DIVINO! Defesa espetacular no ângulo!", fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return False

    # TESTE DE BARREIRA NO MODO FALTAS
    if modo_jogo == "FALTAS":
        # Se chutar baixo na barreira ou errar o efeito contra a barreira
        hit_barreira = False
        if barreira_pos == "Esq" and pos_chute_key in ["1", "4"] and efeito_escolhido != "1":
            hit_barreira = True
        elif barreira_pos == "Dir" and pos_chute_key in ["3", "6"] and efeito_escolhido != "3":
            hit_barreira = True

        if hit_barreira and random.random() < 0.70:
            som_efeito("barreira")
            renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "CARIMBOU A BARREIRA! A bola explodiu na barreira humana!", fase="impacto", barreira_pos=barreira_pos)
            time.sleep(2.2)
            return False

    # SIMULAÇÃO NORMAL (ISOLADA E TRAVE)
    chutou_fora = forca > 90 and random.random() < 0.45
    bateu_trave = forca > 80 and not chutou_fora and random.random() < 0.30

    gol[r_g][c_g] = f"{AMARELO} 🧤 {RESET}"

    if chutou_fora:
        som_efeito("fora")
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "ISOLOU! A bola subiu demais!", fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return False
    
    if bateu_trave:
        som_efeito("trave")
        gol[r_b][c_b] = f"{AMARELO} 🔔 {RESET}"
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, "NA TRAAAAVE!", fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return False

    if pos_chute_key == pos_goleiro_key:
        som_efeito("defesa")
        gol[r_b][c_b] = f"{VERMELHO} 💥 {RESET}"
        msg = "DEFENDEU! O goleiro buscou no canto!" if sou_batedor else "DEFESAÇO! Você espalmou a cobrança!"
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, msg, fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return False
    else:
        som_efeito("gol")
        gol[r_b][c_b] = f"{VERDE} ⚽ {RESET}"
        msg = "GOOOOOOOOOOL! QUE GOLAÇO NA GAVETA!" if sou_batedor else "GOL DA IA! Cobrança perfeita!"
        renderizar_estadio(gol, placar_jog, placar_ia, rodada, modo_jogo, forca, msg, fase="impacto", barreira_pos=barreira_pos)
        time.sleep(2.2)
        return True

# --- SELEÇÃO DE MODO DE JOGO ---
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{BOLD}{CIANO}=====================================================")
print("             ⚽ SELEÇÃO DE MODO DE JOGO ⚽")
print(f"====================================================={RESET}")
print(" [1] Disputa de Pênaltis (Cara a cara com o goleiro)")
print(" [2] Cobrança de Faltas  (Com barreira e curva na bola)")
print(f"{CIANO}-----------------------------------------------------{RESET}")

modo_op = ""
while modo_op not in ["1", "2"]:
    modo_op = input(f"{AMARELO}Escolha o modo (1 ou 2): {RESET}").strip()

modo_jogo = "PENALTIS" if modo_op == "1" else "FALTAS"

# --- GAME LOOP ---
placar_jog = 0
placar_ia = 0
rodada = 1
fim_antecipado = False

while rodada <= 5:
    gol_base = [["  .  ", "  .  ", "  .  "], ["  .  ", "  .  ", "  .  "]]
    barreira_pos = random.choice(["Esq", "Dir"])

    # --- TURNO JOGADOR ---
    goleiro_ia = str(random.randint(1, 6))
    
    canto = ""
    while canto not in POSICOES:
        renderizar_estadio(gol_base, placar_jog, placar_ia, rodada, modo_jogo, narracao="Sua vez de cobrar! Escolha o canto. (ADMIN para cheats)", fase="preparacao", barreira_pos=barreira_pos)
        print("Onde quer mandar?")
        print(" [1] Esq Alto  | [2] Meio Alto  | [3] Dir Alto")
        print(" [4] Esq Baixo | [5] Meio Baixo | [6] Dir Baixo")
        
        canto = input(f"\n{BOLD}{AMARELO}Escolha o canto (1-6 ou ADMIN): {RESET}").strip()
        if canto.upper() == "ADMIN":
            menu_cheats()
            canto = ""

    efeito_escolhido = "2"
    if modo_jogo == "FALTAS":
        print("\nEscolha o Efeito na Bola:")
        print(" [1] Curva Esq | [2] Direto/Colocado | [3] Curva Dir | [4] Folha Seca")
        efeito_escolhido = input(f"{BOLD}{CIANO}Efeito (1-4): {RESET}").strip()
        if efeito_escolhido not in EFEITOS_FALTA:
            efeito_escolhido = "2"

    efeito_tipo = input(f"{BOLD}{CIANO}Tipo de chute - [F]orte ou [C]olocado? (F/C): {RESET}").strip().upper()
    forca_chute = random.randint(60, 98) if efeito_tipo == 'F' else random.randint(45, 80)

    gol_marcado = animar_chute(canto, forca_chute, efeito_escolhido, goleiro_ia, placar_jog, placar_ia, rodada, modo_jogo, barreira_pos=barreira_pos, sou_batedor=True)
    
    if gol_marcado:
        placar_jog += 1
        historico_jog.append("GOL")
    else:
        historico_jog.append("ERRO")

    acabou, vencedor = checar_fim_matematico(placar_jog, placar_ia, len(historico_jog), len(historico_ia))
    if acabou:
        fim_antecipado = True
        break

    # --- TURNO IA ---
    chute_ia = str(random.randint(1, 6))
    efeito_ia = str(random.randint(1, 4))
    
    dica_raio_x = f" {ROXO}[RAIO-X: IA VAI NO {POSICOES[chute_ia][0].upper()}]{RESET}" if cheats_ativos["raio_x"] else ""

    defesa = ""
    while defesa not in POSICOES:
        renderizar_estadio(gol_base, placar_jog, placar_ia, rodada, modo_jogo, narracao=f"A IA vai cobrar a falta/pênalti. Prepare-se!{dica_raio_x}", fase="preparacao", barreira_pos=barreira_pos)
        print("Para onde você vai pular?")
        print(" [1] Esq Alto  | [2] Meio Alto  | [3] Dir Alto")
        print(" [4] Esq Baixo | [5] Meio Baixo | [6] Dir Baixo")

        defesa = input(f"\n{BOLD}{AMARELO}Escolha onde pular (1-6 ou ADMIN): {RESET}").strip()
        if defesa.upper() == "ADMIN":
            menu_cheats()
            defesa = ""

    forca_ia = random.randint(60, 85)
    gol_ia = animar_chute(chute_ia, forca_ia, efeito_ia, defesa, placar_jog, placar_ia, rodada, modo_jogo, barreira_pos=barreira_pos, sou_batedor=False)
    
    if gol_ia:
        placar_ia += 1
        historico_ia.append("GOL")
    else:
        historico_ia.append("ERRO")

    acabou, vencedor = checar_fim_matematico(placar_jog, placar_ia, len(historico_jog), len(historico_ia))
    if acabou:
        fim_antecipado = True
        break

    rodada += 1

# --- FIM DE JOGO ---
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\n{BOLD}{AMARELO}=====================================================")
print("                  RESULTADO FINAL")
print(f"====================================================={RESET}")

if fim_antecipado:
    print(f"{BOLD}{ROXO}⚡ FIM DE JOGO ANTECIPADO! Matematicamente a disputa foi encerrada!{RESET}\n")

print(f"Placar Final: {BOLD}{VERDE}Você {placar_jog}{RESET} ({formatar_historico(historico_jog)}) x {BOLD}{VERMELHO}{placar_ia} IA{RESET} ({formatar_historico(historico_ia)})\n")

if placar_jog > placar_ia:
    print(f"{BOLD}{VERDE}🏆 É CAMPEÃO! VOCÊ VENCEU A DISPUTA!{RESET}\n")
elif placar_ia > placar_jog:
    print(f"{BOLD}{VERMELHO}☠️ VICE-CAMPEÃO! A IA LEVOU A MELHOR.{RESET}\n")
else:
    print(f"{BOLD}{AMARELO}🤝 EMPATE NAS COBRANÇAS REGULAMENTARES!{RESET}\n")