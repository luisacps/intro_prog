cont = 0
cont2 = 1

while (cont < 5):
    n = int(input('\nvalor de n: '))

    while (cont2 <= n):
        print(f'{cont2} x {n} = {cont2*n}')
        cont2 += 1
    cont2 = 1

    cont += 1