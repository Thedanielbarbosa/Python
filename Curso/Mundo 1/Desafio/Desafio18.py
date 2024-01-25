from math import cos, sin, tan, radians

a = float(input('Informe um ângulo: '))

c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))

print('O cosseno do ângulo {} é {:.2f}.\nO seno do ângulo {} é {:.2f}\nA tangente do ângulo {} é {:.2f}'.format(a, c, a, s, a, t))

