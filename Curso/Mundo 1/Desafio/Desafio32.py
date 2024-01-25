ano = int(input('Informe o ano: '))

if (ano % 4) == 0 and (ano % 400) and (ano % 100) != 0:
    print('O ano {} e bissexto'.format(ano))

else:
    print('O ano {} não é bissexto'.format(ano))
