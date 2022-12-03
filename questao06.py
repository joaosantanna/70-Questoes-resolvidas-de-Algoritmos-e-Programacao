# Entradas
# valores de x e y

x = float(input('Digite um valor para x:'))
y = float(input('Digite um valor para y :'))

# processamento
# troque os valores destas variáveis

x,y = y,x
'''
tmp = x
x = y
y = tmp
'''

# saida
# imprimir valores de x e y

print(f'valor de x = {x}')
print(f'Valor de y = {y}')
