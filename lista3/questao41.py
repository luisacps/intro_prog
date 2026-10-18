n = int(input('valor de n: '))
cont_valores = 1
soma = 0
soma_quadrado = 0
soma_xy = 0

while cont_valores <= n:

    x = int(input(f'valor de x{cont_valores}: '))
    y = int(input(f'valor de y{cont_valores}: '))

    soma += x
    soma_quadrado += x**2
    soma_xy += x*y

    cont_valores += 1

print(f'letra a = {soma}')
print(f'letra b = {soma_xy}')
print(f'letra c = {soma_quadrado}')