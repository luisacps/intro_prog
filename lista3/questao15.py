base = int(input('base: '))
expoente = int(input('expoente: '))
cont = 0
resultado = 1

while (cont < expoente):
    resultado *= base
    cont += 1
print(f'{base}^{expoente} = {resultado}')