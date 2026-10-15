# exercício 18 - maior ou iguais
# objetivo: resolver maior ou iguais conforme o enunciado

# entrada
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
# decisão e saída
if a > b:
    print("O maior é", a)
elif b > a:
    print("O maior é", b)
else:
    print("Os números são iguais")
