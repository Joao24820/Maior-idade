nome = str(input('Informe o seu nome: '))
i = int(input('Informe a sua idade: '))

if i >= 18:
    print('senhor {} voce já e considerado(a) de maior idade !  '.format(nome))
else:
    print('Senhor {} voce ainda é considerado(a) Menor de idade ! .'.format(nome))
