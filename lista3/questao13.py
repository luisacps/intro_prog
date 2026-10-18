s1 = 0
s2 = 0

numerador1 = 1
denominador1 = 1

expoente = 1
denominador2 = 50

while denominador1 <= 50:
    s1 += (numerador1/denominador1)

    numerador1 += 2
    denominador1 += 1

while denominador2 > 0:
    s2 += (2**expoente)/denominador2

    expoente += 1
    denominador2 -= 1

print(s1)
print(s2)