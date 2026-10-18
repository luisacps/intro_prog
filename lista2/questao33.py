peso = float(input('informe o peso: '))
altura = float(input('informe a altura: '))

imc = peso / (altura)**2

if imc < 18.5:
    print('ABAIXO DO PESO')

elif 18.5 <= imc < 25:
    print('PESO NORMAL')

elif 25 <= imc < 30:
    print('ACIMA DO PESO')

else:
    print('OBESO')

print(f'seu imc é {imc:.2f}')