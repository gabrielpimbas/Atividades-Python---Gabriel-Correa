# exercício 15 - desconto na compra
# objetivo: resolver desconto na compra conforme o enunciado

# entrada
valor = float(input("Valor da compra: "))
# decisão
if valor >= 100:
    valor = valor * 0.9
# saída
print("Valor final: R$", valor)
