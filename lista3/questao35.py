codigo = int(input('código do produto: '))

cont_qtd_produtos = 0
soma_preco = 0
soma_novo_preco = 0

while codigo >= 0:
    preco = float(input('preço do produto: '))

    soma_preco += preco

    cont_qtd_produtos += 1

    novo_preco = preco + preco*0.2
    soma_novo_preco += novo_preco

    print(f'código do produto: {codigo} | novo preço: R${novo_preco}')

    codigo = int(input('código do produto: '))

media_preco = soma_preco / cont_qtd_produtos
media_novo_preco = soma_novo_preco / cont_qtd_produtos

print(f'a média de preços antigos dos produtos é R${media_preco:.2f}')
print(f'a nova média de preços é de R${media_novo_preco:.2f}')