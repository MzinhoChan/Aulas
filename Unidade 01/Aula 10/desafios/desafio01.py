estoque = [
    {"tipo": "arroz", "preço": 20, "quantidade": 10},
    {"tipo": "feijão", "preço": 10, "quantidade": 15},
    {"tipo": "macarrão", "preço": 7, "quantidade": 20},
    {"tipo": "farofa", "preço": 5, "quantidade": 30},
    {"tipo": "carne", "preço": 80, "quantidade": 35},
    {"tipo": "sal", "preço": 2, "quantidade": 25},
]

while True:
    escolha_usuario = int(input("Menu\n1- Lista\n2- Acrescentar\n3- Valor\n4- Estoque\n5- Buscar Produto\n0- Sair\n: "))

    if escolha_usuario == 1:
        for chave in estoque:
            print(chave)

    elif escolha_usuario == 2:
        try:
            produto = {
                "tipo": input("Digite o nome do produto: "),
                "preço": float(input("Digite o valor do produto: ")),
                "quantidade": int(input("Digite a quantidade do produto: "))
            }

            estoque.append(produto)
            print("Produto adicionado com sucesso.")

        except:
            print("Algo deu errado. Tente novamente.")

    elif escolha_usuario == 3:
        def somar_total():
            total_geral = 0
            for chave in estoque:
                total_geral += chave["preço"] * chave["quantidade"]
            print(f"Total geral do estoque: {total_geral}")
        
        somar_total()  

    elif escolha_usuario == 4:
        def somar_quantidade_total():
            total_geral = 0
            for chave in estoque:
                total_geral += chave["quantidade"]
            print(f"Total geral do estoque: {total_geral}")
        
        somar_quantidade_total()

    elif escolha_usuario == 5:
        def buscar_produto():
            busca = input("Digite o produto buscado: ")  

            for chave in estoque:
                if chave ["tipo"] == busca:
                    print(chave["quantidade"])
                    print(chave["preço"])
        buscar_produto()

    elif escolha_usuario == 0:  
        print("Obrigado por usar o nosso sistema.")
        break
