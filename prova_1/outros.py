#falha para numero terminados em zero

n = int(input('numero: '))
invertido = 0

if n > 0:

    while n > 0:
        num = n % 10
        invertido = (invertido * 10) + num
        n = n // 10

else:
    n = n * -1
    while n > 0:
        num = n % 10
        invertido = (invertido * 10) + num
        n = n // 10
    invertido *= -1

print(invertido)