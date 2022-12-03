# entrada: numero n inteiro
n = int(input('Informe um numero:'))
# processamento : procurar numeros divisores de n
print(f'Lista de divisores de {n}')
for i in range(n,0, -1):
    if n % i == 0:
        print(i)
# saida : lista de divisores de n