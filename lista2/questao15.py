mes = int(input('informe o numero do mês: '))

if 1 <= mes <= 12:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print(f'o mês {mes} tem 31 dias')
    elif mes==2:
        print(f'o mês {mes} tem 28 dias')
    else:
        print(f'o mês {mes} tem 30 dias')
else:
    print('esse numero não corresponde a nenhum mês')