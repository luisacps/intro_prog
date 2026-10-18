m = int(input('digite um numero: '))

possivel_divisor = 1
cont_divisores = 0

cont_fatorial = 1
resultado_fatorial = 1

cont_soma_fator = 0
soma_fator = 0

while m > 0:

    if m % 2 == 0:

        while possivel_divisor <= m:
            if m % possivel_divisor == 0:
                print(f'{possivel_divisor} é divisor de {m}')
                cont_divisores += 1

            possivel_divisor += 1

        print(f'{m} possui {cont_divisores} divisores')
        possivel_divisor = 1
        cont_divisores = 0

    else:

        if m < 10:
            while cont_fatorial <= m:
                resultado_fatorial *= cont_fatorial
                cont_fatorial += 1
            print(f'{m}! = {resultado_fatorial}')

        else:
            while (cont_soma_fator <= m):
                cont_soma_fator += 1
                soma_fator += cont_soma_fator
            print(f'soma dos fatores de 1 a {m} = {soma_fator}')

    m = int(input('\ndigite um numero: '))