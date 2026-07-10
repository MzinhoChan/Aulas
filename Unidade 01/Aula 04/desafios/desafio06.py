# Construa um programa onde o usuário digitará
# um valor e o programa mostrará, na tela, a
# tabuada de multiplicação deste número.

num = int(input("Digite o seu número: "))
for i in range(1, 11):
    resultado = num * i
    print(num,  i,  resultado)

