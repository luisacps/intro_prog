valor_compra = float(input('insira o valor da compra: '))
prazo = int(input('insira o prazo: '))
valor_final = 0

if (0 < prazo <= 20):

    if (1 <= prazo <= 3):
        valor_final = valor_compra

    elif (4 <= prazo <= 7):
        valor_final = valor_compra + (valor_compra*0.005)

    elif (8 <= prazo <= 12):
        valor_final = valor_compra + (valor_compra*0.015)

    elif (13 <= prazo <= 20):
        valor_final = valor_compra + (valor_compra*0.03)

    print(f'o valor da compra será: R${valor_final:.2f}')

else:
    print('prazo inválido')