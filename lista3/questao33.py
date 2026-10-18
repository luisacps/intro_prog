n = int(input('quantos numeros serão lidos? '))
cont = 1

fatorial = 1
resultado = 1

while cont <= n:

    num = int(input(f'numero {cont}: '))

    while fatorial <= num:
        resultado *= fatorial
        fatorial += 1
    print(f'valor lido: {num} | {num}! = {resultado}')

    cont += 1