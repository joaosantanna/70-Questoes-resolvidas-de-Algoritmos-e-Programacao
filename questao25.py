
soma = 0
for numero in range(100,201):
    if numero % 7 == 0:
        soma = soma + numero # soma += numero

print(f'soma dos multiplos de 7 entre 100 e 200 = {soma}')

