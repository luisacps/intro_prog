def troca(x,y):
    a = x
    x = y
    y = a
    print(f'x={x} y={y}')

def main():
    x = int(input()) 
    y = int(input())
    print(f'conteudo: x={x} y={y}')
    print('troca: ', end='')
    troca(x, y)
main()