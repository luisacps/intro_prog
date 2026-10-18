#atividade passada em sala 09/09/2026

print('avalie seu risco de credito!')
idade = int(input('informe sua idade: '))

if (idade >= 18):
    renda = float(input('renda mensal: '))
    tempo_emprego = int(input('tempo de emprego, em anos: '))
    divida = float(input('valor das dividas: '))

    if (renda < 1500 and divida > 1000):
        print('RISCO ALTO')
    else:
        if (1500 <= renda <= 3000):
                if (divida < (renda/2) and tempo_emprego >= 2):
                    print('RISCO BAIXO')
                else:
                    print('RISCO MODERADO')
        else:
            if (renda > 3000):
                    if (divida < (renda * 0.3) and tempo_emprego > 3):
                        print('RISCO BAIXO')
                    else:
                        if (divida < (renda * 0.7)):
                            print('RISCO MEDIO')
                        else:
                            print('RISCO ALTO') 
            else: 
                print('RISCO BAIXO')  
else:
    print('voce e menor de idade! esta inapto para credito.')