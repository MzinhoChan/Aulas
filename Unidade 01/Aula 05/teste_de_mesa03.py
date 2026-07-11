f = 5
g = f
f -= 1

i = 0
while i < 10:
    if g > f:
        i += 1
        print(g + 1)
    f ^ i
    g = +i
    i += 1
