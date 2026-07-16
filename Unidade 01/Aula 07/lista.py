# Criando a Lista!
lista_de_compras = ["Maça", "Uva"]

# Colocando um intem na Lista!
lista_de_compras.append("Café")
print(lista_de_compras)

# Colocando um intem em primeiro na Lista!
lista_de_compras.insert(0,"Pão")
print(lista_de_compras)

# Juntando as Listas!
segunda_lista = ["Manteiga"]
lista_de_compras.extend(segunda_lista)
print(lista_de_compras)

# Removendo um intem especifico da Lista!
lista_de_compras.remove("Café")
print(lista_de_compras)

# Removendo o primeiro intem da Lista!
lista_de_compras.pop(0)
print(lista_de_compras)

#Removendo tudo da Lista!
lista_de_compras.clear()
print(lista_de_compras)