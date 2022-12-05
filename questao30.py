t1 = 1
t2 = 1
soma = 0
while True:
    t3 = t1 + t2
    if t3 <= 1000:
        if t3 % 2 == 0:
            soma = soma + t3
    else: # so roda se t3 > 1000
        break

    t1 = t2
    t2 = t3

print(f'Soma = {soma}')

