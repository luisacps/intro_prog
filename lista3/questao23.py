voto = int(input('insira o código para voto: '))

qtd_total_votos = 0
candidato1 = 0; candidato2 = 0; candidato3 = 0; candidato4 = 0; brancos = 0; nulos = 0

while (voto != 0):
    if (voto == 1):
        candidato1 += 1

    elif (voto == 2):
        candidato2 += 1

    elif (voto == 3):
        candidato3 += 1

    elif (voto == 4):
        candidato4 += 1

    elif (voto == 5):
        nulos += 1

    elif (voto == 6):
        brancos += 1

    else:
        print('código de voto inválido')

    voto = int(input('insira o código para voto: '))

print(f'candidato 1: {candidato1} votos')
print(f'candidato 2: {candidato2} votos')
print(f'candidato 3: {candidato3} votos')
print(f'candidato 4: {candidato4} votos')
print(f'nulos: {nulos} votos')
print(f'brancos: {brancos} votos')