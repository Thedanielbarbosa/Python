import random
A1 = str(input('Informe o nome do primeiro alunos: '))
A2 = str(input('Informe o nome do segundo alunos: '))
A3 = str(input('Informe o nome do terceiro alunos: '))
A4 = str(input('Informe o nome do quarto alunos: '))

lista = [A1, A2, A3, A4]

print('O aluno sorteado foi {}!'.format(random.choice(lista)))
