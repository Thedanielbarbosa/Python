r = float(input("Informe o valor de sua carteira: R$ "))
taxa_dolar = float(input("Informe a taxa de cambio do dolar: "))
taxa_euro = float(input("Informe a taxa de cambio do euro: "))
d: float = r / taxa_dolar
e: float = r / taxa_euro

print("Com R$ {:.2f} você pode comprar: U$ {:.2f} ou € {:.2f}".format(r, d, e))

