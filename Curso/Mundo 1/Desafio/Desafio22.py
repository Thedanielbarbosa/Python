nome = input('Digite seu nome: ')

print('seu nome com todas as letras minusculas {}'.format(nome.lower()))
print('seu nome com todas as letras maiúscula {}'.format(nome.upper()))
primeiro = nome.split()
total = (len(primeiro[0]) + len(primeiro[1]) + len(primeiro[2]))
print('O seu nome tem total de {} letras'.format(total))
print('O seu primeiro nome tem {} letras' .format(len(primeiro[0])))
