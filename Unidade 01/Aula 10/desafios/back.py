import plyer

estoque = []

produto = {
    "tipo": "Café",
    "preco_unitario": 28.99,
    "quantidade": 300
}

def buscar_produto():
    busca = input("Digite o produto buscado")

    for produto in estoque:
        if produto["tipo"] == busca:
            print(produto["quantidade"])
            print(produto["preco_unitario"])

def adicionar_produtos():
    try:
        produto = {
            "tipo": input("Digite o tipo de produto: "),
            "preco_unitario": float(input("Digite o preço unitário: ")),
            "quantidade": int(input("Digite a quantidade: "))
        }
        estoque.append(produto)
        print("Produto adicionado corretamente.")

    except:
        print("Algo deu errado. Tente novamente.")

def listar_produtos():
    for produto in estoque:
        print(produto)

def somar_total():
    total_geral = 0

    for produto in estoque:
        total_geral += produto["preco_unitario"] * produto["quantidade"]

    print(f"Total geral do estoque: {total_geral}")

def somar_quantidade_total():
    total_geral = 0

    for produto in estoque:
        total_geral += produto["quantidade"]

    for produto in estoque:
        frase = produto["tipo"] + " - " + str(produto["quantidade"])
        print(frase)

    print(f"Total geral do estoque: {total_geral}")

# Crie uma função que, quando executada, exiba todos os produtos
# que estão com estoque abaixo do mínimo (abaixo de 50).

def limite_estoque():
    for produto in estoque:
        if produto["quantidade"] < 50:
            plyer.notification.notify(
                title = "Falta de orgamento.",
                message = f"Atenção! O patrão está sem grana.",
                app_name = "Sistema de Estoque",
                timeout = 5
            )
        else:
            print("Todos acima do limite!")
    


while True:
    opcao = input("1- Adicionar produto\n2- Listar produtos\n3- Preço Total\n4- Quantidade Total\n5- Limite estoque\n: ")

    if opcao == "1":
        adicionar_produtos()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        somar_total()
    elif opcao == "4":
        somar_quantidade_total()
    elif opcao == "5":
        limite_estoque()
    else:
        print("Digite uma opção válida.")