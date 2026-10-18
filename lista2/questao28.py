h = float(input('insira sua altura: '))
sexo = input('digite seu sexo (M/F): ') #poderia usar um .upper ou .lower para capturar inputs maiúsculos e minúsculos
peso_ideal = 0

if sexo == 'M':
    peso_ideal = (72.7 * h) - 58

elif sexo == 'F':
    peso_ideal = (62.1 * h) - 44.7

print(f'seu peso ideal é {peso_ideal:.2f}')