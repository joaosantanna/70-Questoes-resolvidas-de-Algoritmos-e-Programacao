n = int(input('Informe um numero inteiro:'))

eh_primo = True
for i in range(2,n):
    if n % i == 0:
        print(f'{n} não é primo')
        eh_primo = False
        break

if eh_primo == True:
    print(f'{n} é um numero primo')