valor_do_salario = float(input("Digite o seu salario. "))
vale_transporte = (6/100)*valor_do_salario
saude = valor_do_salario * 0.03

salario_liquido = valor_do_salario - vale_transporte - saude

print(salario_liquido)
print(vale_transporte)
print(saude)