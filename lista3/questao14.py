num = int(input('numero: '))
cont = 1
produto = 1

while (cont <= num):
    print(cont, end=' ')
    produto = produto*cont
    cont += 1
    
print(f'produto = {produto}')