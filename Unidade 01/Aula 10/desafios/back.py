# Crie um estoque de produtos funcional em Python
# para um mercado ultilizando Dicionários.

# Crie uma lista de estoque.
# Os produtos serão um dicionário com TIPO, PREÇO UNITÁRIO, QUANTIDADE.
# Devemos poder ACESSAR e CRIAR produtos.
# Crie funções para obtermos a SOMA TOTAL de preços e a SOMA TOTAL DE QUANTIDADES.

estoque = [
    {"tipo":"arroz","preço":"20","quantidade":"10"},
    {"tipo":"feijão","preço":"10","quantidade":"15"},
    {"tipo":"macarrão","preço":"7","quantidade":"20"},
    {"tipo":"farofa","preço":"5","quantidade":"30"},
    {"tipo":"carne","preço":"80","quantidade":"35"},
    {"tipo":"sal","preço":"2","quantidade":"25"},
]

while True:
    escolha_usuario = int(input("Menu\n1-Lista\n2-Acrescentar\n3-Valor\n4-Estoque\n0-Sair\n:"))

    if escolha_usuario == 1:
        for chave in estoque:
                print(chave)

    elif escolha_usuario == 2:
            produto = {
                "tipo":input("Digite o nome do produto: "),
                "valor":input("Digite o valor do produto: "),
                "quantidade":input("Digite a quantidade do produto: ")
            }
            estoque.append(produto)

    elif escolha_usuario == 0:
         print("Obrigado por usar o nosso sistema.")
         break
