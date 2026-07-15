# Importações
# Variáveis Globais
# Funções
# Resto do Programa

def exbir_menu_infantil():
    print("Relampago Marquinhos")
    print("Hotwheels")
    print("Patrulha Canina")
    print("Thomas e seus Amigos")

def exibir_menu_normal():
    print("Toyota -> À partir de R$ 180.000")
    print("Mercedes -> À partir de R$ 300.000")
    print("Fiat -> À parit de R$ 70.000")

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
   