def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

def proximos_10_primos(numero):
    contador = 0
    teste = numero + 1
    while True:
        if primo(teste) == True:
            print(teste)
            contador = contador + 1

        teste = teste + 1
        if contador == 10 :
            break
    # fim da funcao


proximos_10_primos(1000)
