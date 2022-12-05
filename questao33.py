n = int(input('Informe o numero n:'))

for i in range(1,n):
    dobro = 2*i
    soma = 0
    for x in range(1,i + 1):
        if i % x == 0:
            soma = soma + x
    if dobro == soma:
        print(i)