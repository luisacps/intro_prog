v = []
cont_negativo = 0

for i in range(6):
    num = int(input('digite um numero: '))
    v.append(num)

    if num < 0:
        cont_negativo += 1

print(v)
print(f'há {cont_negativo} valores negativos na lista')

# segunda forma de fazer: terminar a lista e acessa-la posteriormente

v = []

for i in range(6):
    num = int(input('digite um numero: '))
    v.append(num)

cont_negativo = 0

for i in range(6):
    if v[i] < 0:
        cont_negativo += 1

print(v)
print(f'há {cont_negativo} valores negativos na lista')