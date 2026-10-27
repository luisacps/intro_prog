def media(x,y,z):
    m = (x + y + z) / 3
    return m

def main():

    nome = input('nome: ')

    while nome != 'FIM':

        x = float(input('nota 1: '))
        y = float(input('nota 2: '))
        z = float(input('nota 3: '))
        print(f'nome: {nome} | media = {media(x,y,z):.2f}')

        nome = input('nome: ')

main()