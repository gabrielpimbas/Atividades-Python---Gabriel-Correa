# exercício 29 - o maior de três
# objetivo: resolver o maior de três conforme o enunciado

# entrada
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
# decisão e saída
if a > b and a > c:
    print("O maior é", a)
elif b > a and b > c:
    print("O maior é", b)
else:
    print("O maior é", c)
