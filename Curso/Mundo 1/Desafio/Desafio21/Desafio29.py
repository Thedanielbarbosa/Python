vel = int(input('Informe a velocidade do carro: '))

if vel > 80:
    m: int = (vel - 80)*7
    print('Você foi multado no valor de R${:.2f}'.format(m))
else:
    print('Velocidade {}Km/h'.format(vel))