# Construa um programa que exiba na tela todas as
# horas possíveis em um dia, utilizando estrutura de
# repetição.
# -Você pode criar um loop para as horas, outro
# para os minutos e outro para os segundos!-

for horas in range(24):
    for minutos in range (60):
        for segundos in range (60):
            print(horas,":", minutos,":", segundos)
    