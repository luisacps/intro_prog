n = int(input('insira valor inteiro e impar: '))
theta = float(input('valor de theta: '))

expoente = 1
fator = 1
fatorial = 1
multiplicador = -1
seno = 0

while expoente <= n:

    if expoente % 2 != 0:
        impar = expoente
        print(impar)
        while fator <= impar:
            fatorial *= fator
            print(f'{fator}! = {fatorial}')
            fator += 1

    expoente += 1



"""     while fator <= expoente:
        fatorial *= fator
        fator += 1

    seno += ((theta**expoente)/ fatorial) * multiplicador
    
    expoente += 2
    multiplicador *= -1

sen_t = theta + seno
print(f'{sen_t:.5f}') """