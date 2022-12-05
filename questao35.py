from math import pi
valor_pi = 3
print(f'aproximacao 1 = {valor_pi}')
n = 2
for i in range(2,16):
    if i % 2 == 0:
        valor_pi = valor_pi + 4 / (n * (n + 1) * (n + 2))
        print(f'aproximacao {i} = {valor_pi}')
    else:
        valor_pi = valor_pi - 4 / (n * (n + 1) * (n + 2))
        print(f'aproximacao {i} = {valor_pi}')
    n = n + 2
