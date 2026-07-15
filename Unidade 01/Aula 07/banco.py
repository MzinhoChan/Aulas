import os
# Operações básicas: Saque, Saldo, Deposito
# Operações avançadas: Login, Impressão de Recibo, Suporte, Cofrinho

saldo_inicial = 0

usuario = "Mauricio"
senha = "1234"

def limpar():
    os.system("cls")

def saque(saldo):
    valor = int(input("Digite o valor desejado\n"))
    saldo -= valor
    return saldo

def deposito(saldo):
    valor = int(input("Digite o valor desejado\n"))
    saldo += valor
    return saldo

def cofrinho(saldo_cofrinho):
    valor = float(input("Digite o seu valor para adicionar:|n"))
    saldo_cofrinho += valor

    for mes in range(1,13):
        montante = saldo_cofrinho*(1+0.01)
        saldo_cofrinho = montante
        print(f"O cofrinho rendeu! Valor atual: {montante}")

    return saldo_cofrinho

    
    

def menu():
    saldo_inicial = 0
    saldo_cofrinho = 0

    while True:
        escolha_usuario = int(input("Menu\n1-Saldo\n2-Saque\n3-Deposito\n4-Cofrinho\n0-Sair\n"))

        if escolha_usuario == 1:
            limpar()
            print(saldo_inicial)

        elif escolha_usuario == 2:
            saldo_inicial = saque(saldo_inicial)
            limpar()
            
        elif escolha_usuario == 3:
            saldo_inicial = deposito(saldo_inicial)
            limpar()

        elif escolha_usuario == 4:
             saldo_cofrinho = cofrinho(saldo_cofrinho)

        elif escolha_usuario == 0:
            limpar()
            print("Obrigado por usar o nosso sistema.")
            break
        
# Enquanto o usuario não digitar o usuario correta, pedimos para digitar novamente.
while True: 
    usuario_digital = input("Insira o seu cartão.")
    if usuario_digital == usuario:
        # Enquanto o usuario não digitar a senha correta, pedimos para digitar novamente.
        while True:
             senha_digitada = input("Digite sua senha\n")
             if senha_digitada == senha:
                    menu()
                    break
             else:
               print("Senha incorreta")
        break
   
    else:
        print("Conta inválida. Verifique se o cartão foi inserido corretamente e se a conta é valida.")
                