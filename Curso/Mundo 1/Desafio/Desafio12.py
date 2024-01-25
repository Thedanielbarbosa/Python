preco = float(input("Informe o preço: "))
desc = int(input(" informe o valor do desconto: "))

var = desc/100
var_final = preco-(preco * var)
print("O produto que custava R${:.2f}, na promoção com desconto {}% vai custar R${:.2f}".format(preco, desc, var_final))
