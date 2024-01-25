Salario = float(input("Qual o salario do funcionario? R$"))
Desc = float(input("qual o valor do aumento? "))

Salario_final: float = Salario + (Salario * Desc/100)
print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}".format(Salario, Desc, Salario_final))
