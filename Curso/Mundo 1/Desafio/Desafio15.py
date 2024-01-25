dias = int(input('Quantos dias ele foi alugado? '))
km = float(input('Quantos Km ele rodou? '))
diaria = float(input('Qual o valor da diária ? R$'))
km_valor = float(input('Qual o valor po Km rodados? R$'))

val_final: float = (km_valor * km) + (dias * diaria)
print('O valor final apagar por {} dias e {:.1f}Km rodados é de R${:.2f}'.format(dias, km, val_final))


