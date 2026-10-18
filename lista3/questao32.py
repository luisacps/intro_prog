n = int(input('digite um numero: '))

qtd_intervalo1 = 0
qtd_intervalo2 = 0
qtd_intervalo3 = 0
qtd_intervalo4 = 0

while 0 < n < 101:

    if 0 <= n <= 25:
        qtd_intervalo1 += 1

    elif 26 <= n <= 50:
        qtd_intervalo2 += 1

    elif 51 <= n <= 75:
        qtd_intervalo3 += 1

    else:
        qtd_intervalo4 += 1

    n = int(input('digite um numero: '))

print(f'há {qtd_intervalo1} valores em [0,25]')
print(f'há {qtd_intervalo2} valores em [26,50]')
print(f'há {qtd_intervalo3} valores em [51,75]')
print(f'há {qtd_intervalo4} valores em [76,100]')
