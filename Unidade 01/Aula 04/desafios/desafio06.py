# Construa um programa onde o usuário digitará
# um valor e o programa mostrará, na tela, a
# tabuada de multiplicação deste número.

num = int(input("Digite o número: "))
multi = int(num * 2) / 2
for i in range(num, 101 , multi) :
    print(i)
