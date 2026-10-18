qtd_valores = 0
cont = 0

while (qtd_valores < 5):
    valor = int(input('insira um valor numerico: '))

    if (valor < 0):
        cont += 1

    qtd_valores += 1

print(f'entre os valores inseridos, havia {cont} valores negativos')