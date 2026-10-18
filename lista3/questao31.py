n = int(input('numero (ou 0 para parar): '))
cont = 0

while n != 0:

    if cont%20 == 0:
        print(f'valor lido | quadrado |  cubo  | raiz quadrada')

    print(f'     {n}' , end='        ')
    print(f' {n**2}', end='        ')
    print(f' {n**3}', end='         ')
    print(f' {n**0.5:.2f}')

    cont += 1

    n = int(input('\nnumero (ou 0 para parar): '))