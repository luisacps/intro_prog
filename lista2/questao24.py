compra = float(input('insira o valor da compra: '))
prestacao = 0

if (0 < compra <= 500):
    prestacao = compra / 5
    print(f'sua compra pode ser dividida em 5x de R${prestacao}')

elif (compra > 500):
    prestacao = compra / 8
    print(f'sua compra pode ser dividida em 8x de R${prestacao}')

else:
    print('valor de compra inválido')