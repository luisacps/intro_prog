n = int(input('qtd de termos: '))
x = int(input('valor de x: '))

expoente = 1
fator = 1
fatorial = 1
soma = 0

while expoente < n:

    while fator <= expoente:
        fatorial *= fator
        fator += 1

    soma += ((x**expoente) / fatorial)
    expoente += 1

resultado = 1 + soma
print(f'e^x = {resultado:.5f}')