preco = float(input('preço normal da entrada: '))
dia = input('dia da semana (S, T, Q, A, E, B, D): ')
musica = input('nesse dia, terá musica ao vivo (S/N)? ')

if dia == 'S' or dia == 'T' or dia == 'Q':
    if musica == 'S':
        preco += (preco*0.15 - preco*0.25)

    else:
        preco -= preco * 0.25

    print(f'o preço do ingresso é R${preco}')

elif dia =='A' or dia =='E' or dia =='B' or dia =='D':
    if musica == 'S':
        preco += preco * 0.15

    print(f'o preço do ingresso é R${preco}')

else:
    print('dados inválidos')