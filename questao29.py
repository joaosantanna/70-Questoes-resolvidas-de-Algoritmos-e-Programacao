t1 = 1
t2 = 1
print('Fibo = 1,1,',end='')
for i in range(18):
    t3 = t1 + t2
    print(t3,end=',')
    t1 = t2
    t2 = t3
