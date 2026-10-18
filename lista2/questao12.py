salario = float(input('valor do salario: '))
prestacao = float(input('valor da prestação: '))

if (prestacao <= (salario * 0.3)):
    print('seu emprestimo pode ser concedido :)')
else:
    print('infelizmente o emprestimo não pode ser concedido')