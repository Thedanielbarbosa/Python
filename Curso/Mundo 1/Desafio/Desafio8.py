m = float(input("Informe a quantos metros: "))

cm = m * 100
mm = m * 1000
km = m / 1000
dc = m * 10
dca = m / 10

print("A conversão de {}m para {:.0f}cm e para {:.0f}mm e para {:.2f}km para {:.0f}dc para {:.0f}dec".format(m, cm, mm, km, dc, dca))
