from random import randint

maior = 1
for i in range(50):
    n = randint(1,100)
    print(n)
    if n > maior:
        maior = n

print(f'Maior numero = {maior}')

