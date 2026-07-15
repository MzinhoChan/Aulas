# Importações
# Variáveis Globais
# Funções
# Resto do Programa

def exbir_menu_infantil():
    menu_infantil = ["Relampago Marquinhos", "Hotwheels", "Patrulha Canina", "Thomas e seus Amigos"]
    for index, intem in enumerate(menu_infantil):
        print(f"{index+1},{intem}")
        

def exibir_menu_normal():
    menu_normal = ["Toyota -> À partir de R$ 180.000", "Mercedes -> À partir de R$ 300.000", "Fiat -> À parit de R$ 70.000"]
    for intem in menu_normal:
        print(intem)

def checar_idade(idade):
    if idade < 18:
        exbir_menu_infantil()
    else:
        exibir_menu_normal()

while True:
    idade = int(input("Digite sua idade ou digite 0 para sair: "))
    if idade == 0:
        break
    else:
        checar_idade(idade)
   