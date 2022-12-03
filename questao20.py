peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

imc = peso/(altura**2)

print(f'Indice de Massa Corporal = {imc:.2f}')

if imc < 20:
    print('Abaixo do peso ideal')
if imc >= 20 and imc < 25:
    print('Peso ideal')
if imc >= 25:
    print('Acima do peso ideal')
