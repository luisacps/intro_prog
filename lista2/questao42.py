x = int(input('valor de x: '))

fx = 0

if x <= 1:
    fx = 1

elif 1 < x <= 2:
    fx = 2

elif 2 < x <= 3:
    fx = x**2

else:
    fx = x**3

print(f'f(x) com x = {x} -> {fx}')