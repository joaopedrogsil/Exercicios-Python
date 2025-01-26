lag = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
are = lag * alt
print("Sua parede tem a dimenssão de {}X{} e sua área é de {}m²".format(lag, alt, are))
t = are / 2
print("Para pintar essa parede, você irá precisar de {}l de tinta".format(t))