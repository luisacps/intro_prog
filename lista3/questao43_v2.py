a = 92
divisor = 1
qtd_divisores = 0
produto = 1

while a <= 1478:

    raiz = a**0.5

    while divisor <= raiz:

        if a % divisor == 0:
            qtd_divisores += 1

        divisor += 1

    if qtd_divisores == 1:
        produto *= a

    qtd_divisores = 0
    divisor = 1
    a += 1

print(f'o produto entre os numeros primos do intervalo é igual a: {produto}')