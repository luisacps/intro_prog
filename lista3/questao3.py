# essa versão funciona com os valores são diferentes de 0:

n = int(input('defina a quantidade de valores: '))

cont = 0

while (cont < n):
    num = int(input('insira um valor: '))

    if (num > 0):
        print(f'{num} é positivo')
    elif (num < 0):
        print(f'{num} é negativo')
    cont += 1

# essa versão considera o caso com 0:

n = int(input('defina a quantidade de valores: '))

cont = 0

while (cont < n):
    num = int(input('insira um valor: '))

    if (num > 0):
        print(f'{num} é positivo')
    elif (num == 0):
        print(f'esse valor é zero.')
    else:
        print(f'{num} é negativo')
    cont += 1