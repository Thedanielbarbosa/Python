salario = float(input('Informe o valor do salario do funcionario: '))

if salario > 1250:
    final: float = salario + (salario * 10 / 100)
    print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}".format(salario, '10', final))

else:
    final2 = salario + (salario * 15 / 100)
    print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}".format(salario, '15', final2))
