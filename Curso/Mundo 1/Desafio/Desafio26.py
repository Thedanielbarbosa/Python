frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {}'.format(frase.upper().count('A')))
print('ela apare pela primeira vez na posição {}'.format((frase.upper().find('A')+1)))
print('ela apare pela primeira vez na posição {}'.format((frase.upper().rfind('A')+1)))

