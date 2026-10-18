codigo = int(input('código: '))

soma_nota = 0

while codigo >= 0:

    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    nota3 = float(input('nota 3: '))

    maior_nota = nota1

    if nota2 > maior_nota:
        maior_nota = nota2

    if nota3 > maior_nota:
        maior_nota = nota3

    soma_nota = nota1 + nota2 + nota3
    soma_nota -= maior_nota
    media = ((maior_nota*4) + (soma_nota*3)) / 10

    print(f'\ncódigo do aluno: {codigo}')
    print(f'nota 1: {nota1}')
    print(f'nota 2: {nota2}')
    print(f'nota 3: {nota3}')
    print(f'a média do aluno é {media:.2f}')

    if media >= 5:
        print('APROVADO')

    else:
        print('REPROVADO')

    cont = 1

    codigo = int(input('\ncódigo: '))
        

