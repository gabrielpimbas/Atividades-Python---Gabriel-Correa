# exercício 6 - compra na cantina
# objetivo: resolver compra na cantina conforme o enunciado

# entrada
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))
pago = float(input("Valor pago: "))
# processamento
total = preco * quantidade
troco = pago - total
# saída
print("Total: R$", total)
print("Troco: R$", troco)
