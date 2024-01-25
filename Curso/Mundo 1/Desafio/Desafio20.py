import random
print('Sorteio para a ordem de apresentação dos trabalhos')
n: str = 'Informe os dados'
print('{:^40}'.format(n))
A1 = str(input('Infomer o nome do 1° aluno: '))
A2 = str(input('Informe o nome do 2° aluno: '))
A3 = str(input('Informe o nome do 3° aluno: '))
A4 = str(input('Informe o nome do 4° aluno: '))
lista = [A1, A2, A3, A4]

random.shuffle(lista)

print('\nA ordem de apresentação será: ')
print(lista)
