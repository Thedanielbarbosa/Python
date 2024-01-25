# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis
# sobre ela

algo = input('Digite algo: ')

print(' O tipo primitivo desse valor é: ', type(algo))
print('É um número? {}' .format(algo.isnumeric()))
print('é um alfanumérico? {}'.format( algo.isalnum()))
print('É um alfabético? {}'.format(algo.isalpha()))
print('Esta em letras maiusculas? {}'.format(algo.isupper()))
print('Esta em letras minusculas? {}'.format(algo.islower()))
print('é capitalizado? {}'.format(algo.isascii()))
print('tem espaços? {}'.format(algo.istitle()))
