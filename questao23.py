
while True:
    n = int(input('digite um numero para a tabuada:'))
    if n >= 1 and n <=10:
        print('numero valido')
        break
    else:
        print('Erro, numero invalido , tente novamente')

for i in range(1,11):
    print(f'{n} x {i} = {n*i}')
