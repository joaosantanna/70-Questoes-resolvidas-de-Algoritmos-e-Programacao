print('Digite 3 numeros')
a = int(input())
b = int(input())
c = int(input())
# funcao max faz isso ai , maior = max(a,b,c)

if a > b and a > c:
    print(f'{a} é o maior numero')
elif b > a and b > c:
    print(f'{b} é o maior numero')
else:
    print(f'{c} é o maior numero')
