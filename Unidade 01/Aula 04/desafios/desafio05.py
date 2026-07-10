# Construa um programa onde o usuário digitará
# um número, o programa fará uma contagem
# regressiva até zero e, depois, contará de zero até o
# número que o usuário digitou.

num = int(input("Digite seu número: "))


for i in range(num, -1, -1):
    print(i)

for i in range(0, num + 1):
    print(i)
    
