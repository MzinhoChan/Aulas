segundos_digitados = int(input("Digite os segundos: "))
horas = int( segundos_digitados / 3600 )
resto_divisao = segundos_digitados % 3600
minutos = int (segundos_digitados / 60)
segundos = resto_divisao % 60

print(f"{horas} horas, {minutos},{segundos}")