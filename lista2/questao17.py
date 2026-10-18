salario = float(input('valor do salário: '))
codigo = int(input('código do cargo: '))
novo_salario = 0
cargo = ''

if codigo == 101:
    cargo = 'Gerente'
    novo_salario = salario

elif codigo == 102:
    cargo = 'Analista'
    novo_salario = salario + (salario*0.005)

elif codigo == 103:
    cargo = 'Programador'
    novo_salario = salario + (salario*0.015)

elif codigo == 104:
    cargo = 'Designer'
    novo_salario = salario + (salario*0.03)

else:
    cargo = 'Desconhecido'
    novo_salario = salario + (salario*0.4)

diferenca = novo_salario - salario

print(f'seu cargo é {cargo} ')
print(f'seu antigo salário era R${salario:.2f}')
print(f'agora, seu salário é de R${novo_salario:.2f}')
print(f'há uma diferença de {diferenca:.2f} reais!')