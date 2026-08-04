game = {
    "titulo" : "God of War",
    "studio" : "Santa Monica",
    "ano" : 2018,
    "genero" : ["Ação", "Aventura"],
    "plataforma" : ["Playstation", "Steam"]
}

#Atualizar algo do Código
game.update({"ano":2022})

#Deletar algo do Código
del game["genero"]

#Fazer em Listas
lista_chaves = game.keys()

for chave in lista_chaves:
    print(chave)