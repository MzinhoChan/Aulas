while True:
 a = int(input("Digite o valor do primeiro número: "))
 b = int(input("Digite o valor do segundo número: "))
 c = input("Escolha uma operação (ou 'sair' para fechar): ")

 if c == "sair":
    print("Calculadora encerrada.")
    break
 def soma(a,b):
    resultado_soma = a+b
    return resultado_soma
 resultado = soma(a,b)
 if c == "+":
    print(resultado)

 def subtracao(a,b):
    resultado_subtracao = a-b
    return resultado_subtracao
 resultado = subtracao(a,b)
 if c == "-":
    print(resultado)

 def divisao(a,b):
    resultado_divisao = a/b
    return resultado_divisao
 resultado = divisao(a,b)
 if c == "/":
    print(resultado)

 def multiplicacao(a,b):
    resultado_multiplicacao = a*b
    return resultado_multiplicacao
 resultado = multiplicacao(a,b)
 if c == "*":
    print(resultado)

 def raiz(a):
    resultado_raiz = a ** 0.5
    return resultado_raiz
 if c == "v":
    resultado = raiz(a)
    print(resultado)