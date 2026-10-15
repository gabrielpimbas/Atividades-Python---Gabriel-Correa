# exercício 31 - tipo de triângulo
# objetivo: resolver tipo de triângulo conforme o enunciado

# entrada
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
# decisão e saída
if a >= b + c or b >= a + c or c >= a + b:
    print("Esses lados não formam um triângulo")
elif a == b and b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")
