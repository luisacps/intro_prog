vendas = float(input('insira o valor das vendas da semana: '))
salario = 0

if (vendas > 1000):
    salario = 1000 + (vendas*0.09) #juntei 200 + 800 de bonus
else:
    salario = 200 + (vendas*0.09)
print(f'seu salário essa semana é de R${salario}')