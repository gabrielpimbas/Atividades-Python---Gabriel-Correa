# exercício 12 - divisão segura
# objetivo: resolver divisão segura conforme o enunciado

# entrada
a = float(input("Dividendo: "))
b = float(input("Divisor: "))
# decisão e saída
if b == 0:
    print("Erro: não existe divisão por zero")
else:
    print("Resultado:", a / b)
