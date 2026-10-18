num = int(input('digite um valor: '))
maior = num
menor = num
cont = 1

while (cont < 50):
    num = int(input('digite um valor: '))

    if (num > maior):
        maior = num
    elif (num < menor):
        menor = num
    cont += 1

print(f'o menor valor digitado é {menor}')
print(f'o maior valor digitado é {maior}')