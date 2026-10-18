n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))
n3 = float(input('digite a nota 3: '))

media = input('escolha a média a (aritmética) ou p (ponderada): ')

if (media == 'a'):
    m_aritmetica = (n1 + n2 + n3)/3
    print(f'a media aritmetica entre os valores é {m_aritmetica:.2f}')

elif (media == 'p'):
    m_ponderada = ((n1+n2)*3 + n3*4)/10
    print(f'a media ponderada entre os valores é {m_ponderada:.2f}')

else:
    print(f'{media} não corresponde a nenhuma média')