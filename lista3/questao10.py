nome = input('nome do aluno: ')
qtd_provas = int(input('qtd de provas feitas: '))

cont = 1
soma = 0

while cont <= qtd_provas:
    nota_prova = float(input(f'nota da prova {cont}: '))
    soma += nota_prova

    cont += 1

media = soma / qtd_provas
print(f'a média de notas do aluno(a) {nome} em {qtd_provas} provas é: {media:.2f}')
