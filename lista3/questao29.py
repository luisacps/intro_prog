n = int(input('numero (ou 0 para parar): '))

cont = 0
soma_media = 0
qtd_positivo = 0
qtd_negativo = 0

while n != 0:

    if n > 0:
        qtd_positivo += 1
    else:
        qtd_negativo += 1

    soma_media += n
    cont += 1

    n = int(input('numero (ou 0 para parar): '))

media = soma_media / cont
porcentagem_positivo = (qtd_positivo/cont) * 100
porcentagem_negativo = (qtd_negativo/cont) * 100

print(f'qtd positivos: {qtd_positivo}')
print(f'qtd negativos: {qtd_negativo}')
print(f'média dos valores: {media:.2f}')
print(f'{porcentagem_positivo}% de valores positivos')
print(f'{porcentagem_negativo}% de valores positivos')