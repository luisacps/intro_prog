n = int(input('numero: '))

produto = 1

while n != 0:

    if n % 2 == 0:
        produto *= n

    n = int(input('numero: '))

print(f'o produto entre os valores pares é {produto}')