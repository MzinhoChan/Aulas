
a = int(input("Digite o valor do primeiro número: "))
b = int(input("Digite o valor do segundo número: "))
c = input("Escolha uma operação (ou 'sair' para fechar): ")

def soma(a,b):
    resultado_soma = a+b
    return resultado_soma
resultado = soma(a,b)

def subtracao(a,b):
    resultado_subtracao = a-b
    return resultado_subtracao
resultado = subtracao(a,b)
 
def divisao(a,b):
    resultado_divisao = a/b
    return resultado_divisao
resultado = divisao(a,b)
 

def multiplicacao(a,b):
    resultado_multiplicacao = a*b
    return resultado_multiplicacao
resultado = multiplicacao(a,b)

def raiz(a):
    resultado_raiz = a ** 0.5
    return resultado_raiz

while True:
  a = int(input("Digite o valor do primeiro número: "))
  b = int(input("Digite o valor do segundo número: "))
  c = input("Escolha uma operação (ou 'sair' para fechar): ")

  if c == "sair":
    print("Calculadora encerrada.")
    break
  elif c == "+":
    print(resultado)
  elif c == "-":
    print(resultado)
  elif c == "/":
    print(resultado)
  elif c == "*":
    print(resultado)