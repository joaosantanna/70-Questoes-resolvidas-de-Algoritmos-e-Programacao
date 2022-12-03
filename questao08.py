
lado = float(input('informe o lado do quadrado:'))
area_quadrado = lado**2

base_menor = float(input('Informe a base menor do trapezio:'))
base_maior = float(input('Informe a base maior do trapezio:'))
altura_trapezio = float(input('Informe a altura do trapezio:'))
area_trapezio = (base_menor+base_maior)*altura_trapezio/2

alutura_triangulo = float(input('Informe a altura do triangulo:'))
base_triangulo = float(input('Informe a base do triangulo:'))
area_triangulo = base_triangulo * alutura_triangulo/2

print(f"area quadrado = {area_quadrado}")
print(f'area do trapezio = {area_trapezio}')
print(f'area do triangulo = {area_triangulo}')

if area_triangulo > area_trapezio and area_triangulo > area_quadrado:
    print('Triangulo tem maior area')
if area_quadrado > area_trapezio and area_quadrado > area_triangulo:
    print('Quadrado tem a maior area')
if area_trapezio > area_quadrado and area_trapezio > area_triangulo:
    print('Trapezio tem a maior area')

'''
# resolucao alternativa
maior = max(area_triangulo,area_trapezio,area_quadrado)
if maior == area_quadrado:
    print('Quadrado tem a maior area')
if maior == area_triangulo:
    print('Triangulo tem maior area')
if maior == area_trapezio:
    print('Trapezio tem a maior area')

'''