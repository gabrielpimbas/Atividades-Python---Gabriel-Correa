# exercício 15 - desconto na compra
# objetivo: resolver desconto na compra conforme o enunciado

# entrada
valor = float(input("Valor da compra: "))
# decisão
if valor >= 100:
    desconto = valor * 0.10
    valor = valor - desconto
    print("Valor final: R$", valor)
else:
    print("Valor final: R$", valor)

