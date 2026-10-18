# imprimir o contrário de um número, mantendo o sinal

n = int(input('numero: '))

if n > 0:
    while n > 0:
        novo_num = n%10
        print(novo_num, end='')

        n = n//10

else:
    num = n * -1

    print('-', end='')
    while num > 0:
        novo_num = num%10
        print(novo_num, end='')

        num = num // 10
