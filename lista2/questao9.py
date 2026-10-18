n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite mais um numero: '))

if (n1 < n2 and n1 < n3): #n1 menor
    if (n2 < n3):
        print(n1, n2, n3, end=' ')
    else:
        print(n1, n3, n2, end=' ')

elif (n2 < n1 and n2 < n3): #n2 menor
    if (n1 < n3):
        print(n2, n1, n3, end=' ')
    else:
        print(n2, n3, n1, end=' ')

elif (n3 < n1 and n3 < n2): #n3 menor
    if (n1 < n2):
        print(n3, n1, n2, end=' ')
    else:
        print(n3, n2, n1, end=' ')