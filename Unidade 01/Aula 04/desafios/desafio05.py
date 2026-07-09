# Construa um programa onde o usuário digitará
# um número, o programa fará uma contagem
# regressiva até zero e, depois, contará de zero até o
# número que o usuário digitou.

num = int(input("Digite o número: "))

for i in range(num,-1,-1) :
    print(i)
    
