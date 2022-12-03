soma = 0
for numero in range(100,201):
    if numero % 13 != 0:
        soma = soma + numero # soma += numero

print(f'A soma dos numeros que não são multiplos de 13')
print(f'entre 100 e 200 = {soma}')