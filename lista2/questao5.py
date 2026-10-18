num = int(input('digite um valor inteiro: '))

if (num%10 == 0):
    print(f'{num} é divisivel por 10, por 5 e por 2')

elif (num%5 == 0):
    print(f'{num} é divisivel por 5')

elif (num%2 == 0):
    print(f'{num} é divisivel por 2')

elif (num%10 != 0 and num%5 != 0 and num%2 != 0):
    print(f'{num} não é divisivel nem por 10, nem por 5, nem por 2')