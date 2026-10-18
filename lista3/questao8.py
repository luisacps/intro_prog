n = int(input('insira a qtd de valores que serão digitados: '))

if (n >= 3):
    num = int(input('digite um valor: '))
    maior = num
    menor = num
    soma = num
    cont = 1

    while (cont < n):

        num = int(input('digite um valor: '))

        if (num > maior):
            maior = num
        elif (num < menor):
            menor = num
        soma += num
        cont += 1

    soma_para_media = soma - (maior + menor) #exclui da soma o maior e o menor valor
    media = soma_para_media/(cont-2) # exclui 2 unidades da contagem, representantes do maior e menor valor
    print(f'a media entre os valores é = {media}, excluindo o menor valor = {menor} e o maior = {maior}')

else:
    print('Erro! A qtd precisa ser maior que 3')