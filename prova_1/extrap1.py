n = int(input('numero: '))

divisor = 1
qtd_divisores = 0

cont_digitos = 0

div = 1
cont_div = 0
qtd_rotacoes_primas = 0

while n > 0:

    while divisor <= n:
        if n % divisor == 0:
            qtd_divisores += 1
        divisor += 1

    if qtd_divisores == 2:
        primo = n

        while primo > 0:
            p = primo % 10
            primo = primo // 10
            cont_digitos += 1

        rotacao = cont_digitos - 1
        rotacao_primo = n

        while rotacao > 0:

            novo_num = rotacao_primo % (10 ** (cont_digitos - 1))
            resto = rotacao_primo // (10 ** (cont_digitos - 1))
            nova_config = (novo_num * 10) + resto

            while div <= nova_config:
                if nova_config % div == 0:
                    cont_div += 1
                div += 1

            if cont_div == 2:
                qtd_rotacoes_primas += 1

            rotacao_primo = nova_config
            rotacao -= 1

        if qtd_rotacoes_primas == (cont_digitos - 1):
            print(f'{n} é um primo circular')
        else:
            print(f'{n} não é um primo circular')

        div = 1
        cont_div = 0
        qtd_rotacoes_primas = 0

    else:
        print(f'{n} não é um numero primo')

    divisor = 1
    qtd_divisores = 0
    cont_digitos = 0

    n = int(input('numero: '))