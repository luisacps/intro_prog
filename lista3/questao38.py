altura = float(input('altura: '))
maior_altura = altura
menor_altura = altura

soma_alt_turma = 0
cont_turma = 0

soma_alt_mulheres = 0
cont_mulheres = 0

while altura > 0:

    sexo = input('sexo (F/M): ')

    soma_alt_turma += altura
    cont_turma += 1

    if sexo == 'F':
        soma_alt_mulheres += altura
        cont_mulheres += 1

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

    altura = float(input('altura: '))

media_alt_turma = soma_alt_turma / cont_turma
media_alt_mulheres = soma_alt_mulheres / cont_mulheres # se o input não incluir mulheres, isso aqui dá erro, aí teria que fazer um if cont_mulheres > 0

print(f'maior altura da turma: {maior_altura}m')
print(f'menor altura da turma: {menor_altura}m')
print(f'média de altura das mulheres: {media_alt_mulheres:.2f}m')
print(f'média de altura da turma: {media_alt_turma:.2f}m')