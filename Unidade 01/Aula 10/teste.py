try:
    print(x)
except(NameError):
    print("Variável X não foi definida.")
except:
    print("Ocorreu um erro.")