import math
cat_op = float(input('Informe o valor do cateto oposto: '))
cat_ad = float(input('Informe o valor do cateto adjacente: '))

hp = math.hypot(cat_op, cat_ad)

print('A hipotenusa vai medir {:.2f}'.format(hp))
