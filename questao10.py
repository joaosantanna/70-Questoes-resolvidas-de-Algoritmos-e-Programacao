valor = float(input('Qual o valor da conta:'))
porcentagem_gorgeta = float(input('Informe quanto em % de gorgeta vc quer pagar:'))


gorgeta = porcentagem_gorgeta *  valor/100

total = valor + gorgeta

print(f'Valor total da conta = R${total}')
print(f'Valor da gorgeta = R${gorgeta}')