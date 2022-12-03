# entrada: as 3 notas do aluno
print(' Informe 3 notas para o aluno')
n1 = float(input('n1:'))
n2 = float(input('n2:'))
n3 = float(input('n3:'))
#processamento :calculo da media
media = (n1+n2+n3)/3
# saida : testar se o aluno passou ou nao
if media >= 6:
    print(f'Aluno aprovado media = {media:.2f}')
else:
    print(f'Aluno reprovado media = {media:.2f}')





