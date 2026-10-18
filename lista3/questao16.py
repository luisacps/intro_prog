num = int(input('insira um valor inteiro: '))

fatorial = 1

while (num > 0):
    fatorial = fatorial * num
    num -= 1
print(fatorial)