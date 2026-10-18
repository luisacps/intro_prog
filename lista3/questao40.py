idade = int(input('idade: '))
maior_idade = idade

cont = 0

while idade != -1:
    sexo = input('sexo (F/M): ' )
    cor_olhos = input('cor dos olhos (castanho/verde/azul): ')
    cor_cabelo = input('cor do cabelo (castanho/preto/loiro): ')

    if sexo == 'F':
        if 18 <= idade <= 35:
            if cor_olhos == 'verde':
                if cor_cabelo == 'loiro':
                    cont += 1

    if idade > maior_idade:
        maior_idade = idade

    idade = int(input('idade: '))

print(f'a pessoa mais velha tem {maior_idade} anos')
print(f'há {cont} mulheres com idade entre 18 e 35 anos, de olhos verdes e loiras')