def sinal(n):
    if n > 0:
        print('POSITIVO')

    elif n == 0:
        print('ZERO')

    else:
        print('NEGATIVO')

def main():
    num = int(input('numero: '))
    sinal(num)

main()