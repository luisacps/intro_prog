num = int(input('insira um valor positivo para iniciar: '))
cont = 0
soma = 0

while (num >= 0):
    soma += num
    cont += 1
    num = int(input('insira um valor (negativo para encerrar): '))

media = soma/cont
print(f'a média entre os valores inseridos é {media:.2f}')

# adicionando um if para inserir uma resposta caso o primeiro valor seja negativo

num = int(input('insira um valor positivo para iniciar: '))
cont = 0
soma = 0

if (num >= 0):
    while (num >= 0):
        soma += num
        cont += 1

        num = int(input('insira um valor (negativo para encerrar): '))

    media = soma/cont
    print(f'a média entre os valores inseridos é {media:.2f}')

else:
    print('valor inválido')