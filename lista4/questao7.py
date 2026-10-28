def media(n1, n2, n3):
    m = (n1 + n2 + n3) / 3
    return m

def situacao(f, m):
    if f > 18:
        print('REPROVADO POR FALTA')
    elif m < 6:
        print('REPROVADO')
    else:
        print('APROVADO')

def main():
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    nota3 = float(input('nota 3: '))
    faltas = int(input('numero de faltas: '))

    media_aluno = media(nota1, nota2, nota3)
    situacao(faltas, media_aluno)

main()