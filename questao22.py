# entrada: um numero inteiro
n = int(input('Informe o numero:'))
# processamento: multiplicacoes sucessivas
fat = 1
for i in range(n,1,-1):
    fat = fat * i
# saida: resultado final na tela
print(f'fatoria de {n} = {fat}')
#3 = 3 * 2 *1