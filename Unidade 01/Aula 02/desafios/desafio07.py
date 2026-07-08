nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 4:
    print("Aluno Reprovado")
elif media > 7:
    print("Aluno aprovado Direto")
else:
    print("aluno em recuperação")
    nota_recuperação = float(input("Digite sua nota de recuperação "))
    if nota_recuperação > 5:
        print("Aluno aprovado em recuperação")
    else:
        print("Aluno reprovado na recuperação")