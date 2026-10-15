# exercício 26 - desconto progressivo
# objetivo: resolver desconto progressivo conforme o enunciado

# entrada
valor = float(input("Valor da compra: "))
# decisão
if valor < 50:
    taxa = 0
elif valor < 100:
    taxa = 0.05
elif valor < 200:
    taxa = 0.10
else:
    taxa = 0.15
# processamento e saída
desconto = valor * taxa
final = valor - desconto
print("Desconto: R$", desconto, "— Final: R$", final)
