def area(d):
    area_circ = 3.14159 * ((d/2)**2)
    return area_circ

def main():
    diametro = float(input('diametro da circ: '))
    if diametro > 0:
        circunferencia = area(diametro)
        print(f'area da circ = {circunferencia}')

    else:
        print('valor inválido (negativo)')

main()