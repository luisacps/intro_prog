n = int(input('digite um numero: '))
cont = 1
fatorial = 1
x = 1
s = 1

while (cont <= n):
    while (x <= cont):
        fatorial = cont*fatorial
        x += 1
    cont += 1
    s += 1/fatorial
print(f'valor aproximado de S = {s:.5f}')