d = int(input("Quantos dias foram alugado: "))
k = float(input("Quantos km foram rodados: "))
dp = 60 * d
kp = 0.15 * k
tp = dp + kp
print("Com base nos dias e nos km, o total a pagar é {}".format(tp))