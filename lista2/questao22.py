n1 = float(input('insira a 1a nota: '))
n2 = float(input('insira a 2a nota: '))
n3 = float(input('insira a 3a nota: '))

media_aritmetica = (n1 + n2 + n3) / 3

if (media_aritmetica >= 6):
    print(f'a média é {media_aritmetica:.2f}')
    print('ALUNO APROVADO')

else:
    print(f'a média é {media_aritmetica:.2f}')
    print('ALUNO REPROVADO')