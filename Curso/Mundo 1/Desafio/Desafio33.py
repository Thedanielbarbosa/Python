n1 = int(input('Informer o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro numero '))

if n1 > n2 and n1 > n3:
    print('maior numero é {}'.format(n1))
    
elif n2 > n1 and n2 > n3:
    print('maior numero é {}'.format(n2))

else:
    print('maior numero é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('menor numero é {}'.format(n1))

elif n2 < n1 and n2 < n3:
    print('menor numero é {}'.format(n2))

else:
    print('menor numero é {}'.format(n3))
