A = int(input('Informe o lado A do triangulo'))
B = int(input('Informe o lado A do triangulo'))
C = int(input('Informe o lado A do triangulo'))

if (A < B + C) and (B < A + C) and (C < A + B):
    print('É possível formar um triângulo com os segmentos {}cm, {}cm e  {}cm '.format(A, B, C))
else:
    print('Não é possível formar um triângulo com os segmentos {}cm, {}cm e  {}cm '.format(A, B, C))
