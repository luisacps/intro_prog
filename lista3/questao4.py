n = int(input('defina a quantidade de valores: '))

cont = 0
negativo = 0

while (cont < n):
    num = int(input('insira um valor: '))

    if (num < 0):
        negativo += 1
    cont += 1

print(f'entre os numeros digitados, haviam {negativo} negativo(s)')