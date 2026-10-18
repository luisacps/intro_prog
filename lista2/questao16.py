a = float(input('insira o valor: '))
b = float(input('insira o valor: '))
c = float(input('insira o valor: '))

if (a > b and a > c):
    media = ((a*5) + (b+c)*2.5) / 10
    print(f'a media ponderada entre os valores é = {media:.2f}')

elif (b > a and b > c):
    media = (b*5) + ((a+c)*2.5) / 10
    print(f'a media ponderada entre os valores é = {media:.2f}')

elif (c > a and c > b):
    media = (c*5) + ((a+b)*2.5) / 10
    print(f'a media ponderada entre os valores é = {media:.2f}')