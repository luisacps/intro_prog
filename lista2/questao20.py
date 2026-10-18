a = int(input('medida do lado 1 do triângulo: '))
b = int(input('medida do lado 2 do triângulo: '))
c = int(input('medida do lado 3 do triângulo: '))

if a < b+c and b < a+c and c < a+b:
    if a == b == c:
        print('esse triângulo é equilátero')

    elif (a == b != c or a == c != b or b == c != a):
        print('esse triângulo é isóceles')

    elif a != b != c != a:
        print('esse triângulo é escaleno')
else:
    print('esses valores não formam um triângulo')