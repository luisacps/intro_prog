n = int(input('numero de medições: '))
cont_medicoes = 1

if 1 <= n <= 100:

    while cont_medicoes <= n:

        m1 = int(input('valor 1: '))

        if -1000000 <= m1 <= 1000000:
            maior = m1
            menor = m1

        else:
            print('valor inválido para medição')

        m2 = int(input('valor 2: '))

        if -1000000 <= m2 <= 1000000:
            if m2 > maior:
                maior = m2

            if m2 < menor:
                menor = m2

        else:
            print('valor inválido para medição')

        m3 = int(input('valor 3: '))

        if -1000000 <= m3 <= 1000000:
            if m3 > maior:
                maior = m3

            if m3 < menor:
                menor = m3

        else:
            print('valor inválido para medição')

        mediana = (m1 + m2 + m3) - maior - menor

        print(f'mediana = {mediana}')
        cont_medicoes += 1

else:
    print('esse valor é inválido!')