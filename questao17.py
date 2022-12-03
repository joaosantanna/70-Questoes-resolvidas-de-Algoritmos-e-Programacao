mes = int(input('Informe o mes correspondente de 1 a 12:'))

if mes == 1:
    print('Janeiro')
elif mes == 2:
    print('Fevereiro')
elif mes == 3:
    print('Março')
elif mes == 4:
    print('Abril')
elif mes == 5 :
    print('Maio')
elif mes == 6:
    print('Junho')
elif mes == 7:
    print('Julho')
elif mes == 8:
    print('Agosto')
elif mes == 9:
    print('Setembro')
elif mes == 10:
    print('Outubro')
elif mes == 11:
    print('Novembro')
elif mes == 12:
    print('Dezembro')
else:
    print('Erro - mes invalido ')

'''
# versao nova so funciona do python 3.10 em diante
match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case _:
        print('Erro - mes invalido')
'''