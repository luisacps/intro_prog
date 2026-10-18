num = int(input('digite um numero inteiro < 0: '))

if (num > 0):
    verificar = num%2
    if (verificar == 0):
        print('esse numero é par!')
    else:
        print('esse numero é impar!')
else:
    print('numero invalido!')