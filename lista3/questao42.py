num = int(input('digite um numero: '))
divisor = 1
verifica_primo = 0
divisores = ''

if num > 1:

    while divisor <= num:

        if num % divisor == 0:
            divisores = divisores + str(divisor) + ' '
            verifica_primo += 1

        divisor += 1

    if verifica_primo == 2:
        print(f'\n{num} É PRIM0')
    else:
        print(f'\n{num} não é primo')
        print(f'divisores de {num} = {divisores}')

else:
    print('esse número é menor que 1, números primos são sempre maiores que 1')