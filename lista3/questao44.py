qtd_numeros_perfeitos = 0
a = 1
divisor = 1
soma_divisores = 0

while qtd_numeros_perfeitos < 5:

    while divisor <= a/2:

        if a % divisor == 0:
            soma_divisores += divisor
    
        divisor += 1

    if soma_divisores == a:       
        print(f'{a} é um numero perfeito')
        qtd_numeros_perfeitos += 1

    divisor = 1
    soma_divisores = 0
    a += 1