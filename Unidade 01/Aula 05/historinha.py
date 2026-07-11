import random

inicios = [" Era uma vez ", "Em um reino distante "," Certo dia "]
herois = [" seu carlos", " o peter parker "," neymar jr "]
climaxs = [" achou um pote "," errou o penalti e ganhou "," caiu em um buraco com "]
finais = [" feijão e se empanturrou. "," bola de ouro e foi feliz pra sempre"," e achou ouro"]

inicio = random.choice(inicios)
heroi = random.choice(herois)
climax = random.choice(climaxs)
final = random.choice(finais)

print(f"{inicio}{heroi}{climax}{final}")