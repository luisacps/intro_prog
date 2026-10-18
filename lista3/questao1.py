a = int(input('insira um valor: '))
b = int(input('insira outro valor: '))

numeros = ''
impares = ''
impares_multiplos_3 = ''

while a <= b:

    numeros += str(a) + ' '

    if a % 2 != 0:
        impares += str(a) + ' '

    if a % 3 == 0:
        impares_multiplos_3 += str(a) + ' '

    a += 1

print(f'numeros do intervalo: {numeros}')
print(f'impares do intervalo: {impares}')
print(f'impares multiplos de 3: {impares_multiplos_3}')