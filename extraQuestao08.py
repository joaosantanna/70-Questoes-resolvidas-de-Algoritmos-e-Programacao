def area_quadrado(lado):
    return lado**2
def area_trapezio(base_maior , base_menor, altura):
    return (base_maior+base_menor)*altura/2

def area_triagulo(base, altura):
    return base*altura/2

a_q = area_quadrado(4)
a_t = area_trapezio(200,10,2)
a_tri = area_triagulo(8,10)
maior = max(a_tri,a_q,a_t)
if maior == a_q:
    print(f'Maior é o quadrado = {a_q}')
elif maior == a_t:
    print(f'Maior é o trapezio = {a_t}')
else:
    print(f'Maior é o triangulo = {a_tri}')