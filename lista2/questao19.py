a = int(input('medida do lado 1 do triângulo: '))
b = int(input('medida do lado 2 do triângulo: '))
c = int(input('medida do lado 3 do triângulo: '))

if (a < b+c and b < a+c and c < a+b):
    sp = (a + b + c) / 2
    area = (sp*((sp - a)*(sp - b)*(sp - c)))**0.5
    print(f'a area do triangulo formado é = {area:.2f}')
else:
    print('esses valores não formam um triângulo')