# Peguei no google para ter uma ideia.

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def multiplicacao(a, b):
    return a * b

def raiz(a):
    if a < 0:
        return "Erro: Não existe raiz real de número negativo!"
    return a ** 0.5


while True:
    c = input("\nEscolha uma operação (+, -, *, /, v) ou 'sair' para fechar: ")

    if c.lower() == "sair":
        print("Calculadora encerrada.")
        break

    if c in ["+", "-", "*", "/", "v"]:
        a = int(input("Digite o valor do primeiro número: "))
        
        if c != "v":
            b = int(input("Digite o valor do segundo número: "))

        if c == "+":
            print(f"Resultado: {soma(a, b)}")
        elif c == "-":
            print(f"Resultado: {subtracao(a, b)}")
        elif c == "*":
            print(f"Resultado: {multiplicacao(a, b)}")
        elif c == "/":
            print(f"Resultado: {divisao(a, b)}")
        elif c == "v":
            print(f"Resultado: {raiz(a)}")
    else:
        print("Operação inválida! Tente novamente.")