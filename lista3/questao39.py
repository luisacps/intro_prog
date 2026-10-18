idade = int(input('idade: '))
maior_idade = idade
menor_idade = idade

soma_salario = 0
cont = 0

cont_mulheres_salario = 0

while idade > 0:

    sexo = input('sexo (F/M): ')
    salario = float(input('salário: '))

    cont += 1
    soma_salario += salario

    if sexo == 'F':
       if salario <= 1000:
            cont_mulheres_salario += 1

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade:
        menor_idade = idade
    
    idade = int(input('idade: '))

media_salarial = soma_salario / cont

print(f'média salarial do grupo: R${media_salarial:.2f}')
print(f'idade da pessoa mais velha: {maior_idade}')
print(f'idade da pessoa mais nova: {menor_idade}')
print(f'qtd de mulheres com salario até R$1000: {cont_mulheres_salario}')