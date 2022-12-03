nome = input('Informe seu nome:')
s = input('Informe o seu sexo (F) Feminino - (M) Masculino:')

if s.lower() == 'm':
    print(f'Ilustrissimo Sr. {nome} bem vindo')
elif s.lower() == 'f':
    print(f'Ilustrissima Srt. {nome} bem vinda')
else:
    print('Me desculpe não identifiquei seu sexo, tente novamente')
