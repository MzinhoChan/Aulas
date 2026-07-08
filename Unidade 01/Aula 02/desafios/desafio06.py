peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

media = peso / (altura*2)

if media > 25:
    print("Acima do peso")
else:
    print("Peso ok")