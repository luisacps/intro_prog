a = int(input('insira um numero: '))
b = int(input('insira outro numero: '))

if (a > b):
    if (a % b == 0):
        print(f'{a} e {b} são múltiplos')

    else:
        print(f'{a} e {b} não são múltiplos')

elif (b > a):
    if (b % a == 0):
        print(f'{a} e {b} são múltiplos')

    else:
        print(f'{a} e {b} não são múltiplos')

else:
    print(f'os valores são iguais e múltiplos')