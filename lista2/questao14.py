idade = int(input('digite sua idade: '))

if (idade > -1):
    if (idade <= 18):
        print('essa pessoa é menor de idade')
    elif (idade > 18 and idade < 65):
        print('essa pessoa é maior de idade')
    else:
        print('essa pessoa é idosa')
else:
    print('essa idade não é valida')