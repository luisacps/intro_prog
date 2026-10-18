n1 = int(input('insira um valor numerico: '))
n2 = int(input('insira outro valor numerico: '))
n3 = int(input('insira mais um valor numerico: '))

#usar o >= nessa situação, evita falhas em caso de empate, por exemplo, se o input fosse 10,10,5. Se não houvesse o "=", cairia no else e estaria errado.

if (n1 >= n2 and n1 >= n3):
    print(f'o maior entre os valores inseridos é {n1}')

elif (n2 >= n1 and n2 >= n3):
    print(f'o maior entre os valores inseridos é {n2}')

else:
    print(f'o maior entre os valores inseridos é {n3}')