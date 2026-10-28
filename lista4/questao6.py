def aumento(x,y):
    aumentar = x + ((x * y) / 100)
    #esse cálculo também pode ser escrito como x (1 + y / 100)
    return aumentar

def main():
    k = float(input('percentual de aumento: '))

    matricula = int(input('matricula: '))
    while matricula != 0:
        nome = input('nome: ')
        salario = float(input('salario: '))
        aumento_salario = aumento(salario, k)

        print(f'nome: {nome} |salario antigo: R${salario}| novo salario: R${aumento_salario}')

        matricula = int(input('matricula: '))

main()