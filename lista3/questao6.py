num = int(input('digite um numero: '))

cont = 0
soma = 0

while (num != 0):

    if (num % 2 == 0):
        soma += num
        cont += 1
    num = int(input('digite um numero: '))

print(f'a média aritmética entre os valores pares digitados é {soma/cont:.1f}')