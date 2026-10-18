num_aluno = int(input('numero do aluno: '))
altura_aluno = float(input('altura do aluno: '))

cont = 1

num_maior_aluno = num_aluno
num_menor_aluno = num_aluno
altura_maior_aluno = altura_aluno
altura_menor_aluno = altura_aluno

while cont < 5:

    num_aluno = int(input('numero do aluno: '))
    altura_aluno = float(input('altura do aluno: '))

    if altura_aluno > altura_maior_aluno:
        altura_maior_aluno = altura_aluno
        num_maior_aluno = num_aluno

    if altura_aluno < altura_menor_aluno:
        altura_menor_aluno = altura_aluno
        num_menor_aluno = num_aluno

    cont += 1

print(f'aluno {num_maior_aluno} é o maior aluno, com {altura_maior_aluno}m')
print(f'aluno {num_menor_aluno} é o menor aluno, com {altura_menor_aluno}m')
