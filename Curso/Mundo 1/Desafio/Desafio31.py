dis = float(input('Informe a distancia da sua viajem: '))

if dis <= 200:
    print('O valor da passagem é R${:.2f}'.format(0.50*dis))
else:
    print('O valor da passagem é R${:.2f}'.format(0.45*dis))