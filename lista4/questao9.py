def nome_mes(mes):
    if mes == 1:
        nome = 'Janeiro'
    elif mes == 2:
        nome = 'Fevereiro'
    elif mes == 3:
        nome = 'Março'
    elif mes == 4:
        nome = 'Abril'
    elif mes == 5:
        nome = 'Maio'
    elif mes == 6:
        nome = 'Junho'
    elif mes == 7:
        nome = 'Julho'
    elif mes == 8:
        nome = 'Agosto'
    elif mes == 9:
        nome = 'Setembro'
    elif mes == 10:
        nome = 'Outubro'
    elif mes == 11:
        nome = 'Novembro'
    elif mes == 12:
        nome = 'Dezembro'

    return nome


def main():
    dia = int(input('dia: '))
    mes = int(input('mes (numero): '))
    ano = int(input('ano: '))
    print(f'{dia} de {nome_mes(mes)} de {ano}')

main()    