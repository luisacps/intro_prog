x = int(input('valor que vai procurar: '))
n = int(input('qtd de numeros que vai inserir: '))

cont = 1
posicao = 0

while cont <= n:
    num = int(input('numero: '))

    if num == x:
        posicao = cont

    cont += 1

if posicao == 0:
    print(f'o valor {x} não apareceu :(')
else:
    print(f'o valor {x} apareceu! ele foi o {posicao}° numero digitado')