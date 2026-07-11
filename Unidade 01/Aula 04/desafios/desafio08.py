# Construa um programa que só aceite notas
# escolares entre zero e dez (treinamento para
# controle de erros).

nota = float(input("Digite a nota: "))

while (nota < 0 or nota > 10) and nota != None:
    print("Nota inválida!")
    nota = float(input("Digite a nota: "))
