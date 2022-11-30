frase = input('Digite uma frase qualquer:')

contador = 0
espaco = 0
total = 0
for letra in frase:
    total = total + 1
    if letra == 'a' or letra == 'A':
        contador += 1
    if letra == 'e' or letra == 'E':
        contador = contador + 1
    if letra == 'i' or letra == 'I':
        contador = contador + 1
    if letra == 'o' or letra == 'O':
        contador = contador + 1
    if letra == 'u' or letra == 'U':
        contador = contador + 1
    if letra == ' ':
        espaco += 1

print(f'numero de vogais na frase {frase}  = {contador}')
print(f'numero do consoantes {total - contador - espaco}')

i