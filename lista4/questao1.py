def cubo(num):
    potencia = num**3
    return potencia

def main():
    n = float(input('numero: '))
    print(f'cubo do numero: {cubo(n)} ')
main()