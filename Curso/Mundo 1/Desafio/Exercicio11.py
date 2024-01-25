altura = float(input("informe a altura da parede: "))
base = float(input("Informe a largura da parede: "))

area = base * altura
tinta = area/2

print("A área da parede é {:.2f}m² e a quantidade de tinta necessaria é {:.1f}L".format(area, tinta))

