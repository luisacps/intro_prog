a = 92
divisor = 1
qtd_divisores = 0
produto = 1

while a <= 1478:

    while divisor <= a:
        if a % divisor == 0:
            qtd_divisores += 1

        divisor += 1

    if qtd_divisores == 2:
        produto *= a

    qtd_divisores = 0
    divisor = 1
    a += 1

print(f'o produto dos primos do intervalo é igual a {produto}')