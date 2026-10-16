# exercicio 38 - equação do segundo grau
# objetivo - resolver uma equação do segundo grau

# comandos de entrada
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# verificação se é uma equação do segundo grau
if a == 0:
    print("Não é uma equação do segundo grau.")

# cálculo do delta
delta = b**2 - 4 * a * c

# comandos lógicos que verificam o delta e dão as raízes
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print("A equação tem uma raiz real:", x)
else:
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print("X1= ", x1, " e X2= ", x2)
