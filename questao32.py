print('Numeros primos entre 100 e 200')
soma = 0
for n in range(100,201):
    eh_primo = True
    for i in range(2,n):
        if n % i == 0:
            eh_primo = False
            break

    if eh_primo == True:
        print(n)
        soma = soma + n

print(f'Soma ={soma}')