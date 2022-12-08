def calcula_gorgeta(total, p):
    resultado = total * p /100
    return resultado

def racha_conta(total, numero_amigos):
    r = total /numero_amigos
    return r


total = float(input('Quanto deu a conta?'))
p_gorgeta = float(input('Quantos % de gorgeta:'))
numero_amigos = int(input('Numero de amigos:'))
g = calcula_gorgeta(total, p_gorgeta)
print(f'Total da conta R$ {(total + g) :.2f} sendo R${g:.2f} de gorgeta')
valor_individual = racha_conta((total+g),numero_amigos)
print(f'Valor para cada um = R${valor_individual:.2f}')