salario = float(input('informe seu salario: '))

maior_salario = 0
cont = 0
soma_qtd_filhos = 0
soma_salario = 0
salario_ate_100 = 0

while salario >= 0:

    qtd_filhos = int(input('qtd de filhos: '))

    soma_salario += salario
    soma_qtd_filhos += qtd_filhos

    cont += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 100:
        salario_ate_100 += 1

    salario = float(input('informe seu salario: '))

media_filhos = soma_qtd_filhos / cont
media_salario = soma_salario / cont
porcentagem_salario_ate_100 = (salario_ate_100/cont)*100

print(f'a media de salario é R${media_salario:.2f}')
print(f'a media de filhos é {media_filhos}')
print(f'o maior salario é R${maior_salario}')
print(f'{porcentagem_salario_ate_100}% da população tem salario até R$100,00')
