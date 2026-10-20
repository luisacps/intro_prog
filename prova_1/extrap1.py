#determinar se um numero é primo circular

n = int(input('numero: '))

divisor = 2
cont_div = 0

cont_digitos = 0

nova_config = 0
div = 2
cont_div_circular = 0
cont_circular_primo = 0

while n > 0:

    # verificar se o numero digitado é primo
    while divisor <= n:
        if (n/2) % divisor == 0:
            cont_div += 1
        divisor += 1

    if cont_div == 0:
        primo = n

        while primo > 0:
            p = primo % 10
            primo = primo // 10
            cont_digitos += 1

        cont = cont_digitos - 1

        numero_primo = n

        while cont > 0:

            novo_num = numero_primo % (10 ** (cont_digitos-1))
            resto = numero_primo // (10 ** (cont_digitos-1))
            nova_config = (novo_num * 10) + resto

            while div <= nova_config:
                if nova_config / 2 % div == 0:
                    cont_div_circular += 1
                div += 1

            if cont_div_circular == 0:
                cont_circular_primo += 1

            div = 2
            cont_div_circular = 0

            cont -= 1
            numero_primo = nova_config

        if cont_circular_primo == (cont_digitos-1):
            print(f'{n} é um numero primo circular!')
        else:
            print(f'{n} não é um primo circular')

    else:
        print(f'o numero digitado não é primo')

    divisor = 2
    cont_div = 0
    cont_digitos = 0
    cont_circular_primo = 0

    n = int(input('numero: '))