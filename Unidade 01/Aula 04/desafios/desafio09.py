# Construa um programa que exiba a sequência de
# Fibonacci de zero até dois mil.

num_um = 0
num_dois = 1

while num_dois <= 2000:
    print(num_dois)

proximo = num_um + num_dois
num_um = num_dois
num_dois = proximo