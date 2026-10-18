pi = 3.1415926535

r = float(input('insira o valor do raio: '))
area = pi * (r)**2

print(f'a area da circunferencia é {area}')

pergunta = input('deseja calcular mais areas? (S/N): ')
while pergunta == 'S':

    r = float(input('insira o valor do raio: '))
    area = pi * (r)**2
    
    print(f'a area da circunferencia é {area}')

    pergunta = input('deseja calcular mais areas? (S/N): ')