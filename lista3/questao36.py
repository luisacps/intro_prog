num = int(input('digite um numero: '))

cont = 1
soma = num
maior = num
menor = num

while cont < 500:
    num = int(input('digite um numero: '))

    soma += num
    cont += 1

    if num > maior:
        maior = num

    if num < menor:
        menor = num

media = soma / cont

print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')
print(f'a média dos valores é {media:.2f}')