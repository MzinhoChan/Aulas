# Construa um programa onde o usuário digitará
# um número e o programa completará o número
# digitado até cem, apenas com números pares.

num = int(input("Digite o seu número: "))
range(num,101,1)

while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1