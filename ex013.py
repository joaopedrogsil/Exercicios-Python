s = float(input("Digite o valor do salario do funcionario R$ "))
ns = s + (s * 15 / 100)
print("O salario atual é R${:.2f} e com um aumento de 15% passa a ser de R${:.2f}.".format(s, ns))