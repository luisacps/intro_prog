n = int(input('insira um numero de 4 digitos: '))

pega_milhar_centena = n//100
pega_dezena_unidade = n%100
soma = pega_milhar_centena + pega_dezena_unidade
quadrado = soma**2

if (quadrado == n):
    print(f'o numero {n} possui a propriedade!')
    print(f'{pega_milhar_centena} + {pega_dezena_unidade} = {soma}')
    print(f'{soma}^2 = {quadrado}')

else:
    print(f'o numero {n} não apresenta a propriedade')