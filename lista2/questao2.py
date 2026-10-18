valor1 = float(input('digite um valor real: '))
valor2 = float(input('digite outro valor real: '))

if (valor1 == valor2):
    print('você digitou dois valores iguais!')
    print(f'{valor1} = {valor2}')
else:
    print('você digitou dois valores diferentes!')
    print(f'{valor1} != {valor2}')