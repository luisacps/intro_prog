cont = 0

while cont < 5:
    a = int(input('valor de a: '))
    b = int(input('valor de b: '))

    while (a <= b):
        if a % 2 == 0:
            print(a, end=' ')
        a += 1

    cont += 1

    print('\n')

    