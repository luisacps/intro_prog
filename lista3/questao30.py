n = int(input('numero: '))

cont = 0
soma_media = 0
qtd_pares = 0
qtd_impares = 0

while n > 0:

    if n % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

    soma_media += n
    cont += 1

    n = int(input('numero: '))

media = soma_media / cont
porcentagem_par = (qtd_pares/cont) * 100
porcentagem_impar = (qtd_impares/cont) * 100

print(f'qdt de pares: {qtd_pares}')
print(f'qtd de impares: {qtd_impares}')
print(f'a média é: {media:.2f}')
print(f'{porcentagem_par:.2f}% de valores pares')
print(f'{porcentagem_impar:.2f}% de valores impares')
