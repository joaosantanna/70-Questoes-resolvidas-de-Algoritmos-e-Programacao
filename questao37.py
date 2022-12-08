def potencializar(base, expoente):
    return base ** expoente

b = int(input('Base:'))
e = int(input('Expoente:'))
x = potencializar(b,e)
print(f'Valor de {b} elevado a {e} = {x}')