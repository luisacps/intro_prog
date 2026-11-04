def precoGasolina(preco, conv):
    p_litro = preco / 3.7854
    novo_preco = conv * p_litro
    return novo_preco

def main():
    preco_eua = float(input('preço do galão nos EUA: '))
    conv = float(input('taxa de conversão dólar-real: '))
    litro_brasil = precoGasolina(preco_eua, conv)
    print(f'preço do litro no Brasil: R${litro_brasil:.2f}')

main()