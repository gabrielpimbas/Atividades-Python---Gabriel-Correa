# exercício 23 - cardápio da cantina
# objetivo: resolver cardápio da cantina conforme o enunciado

# saída do cardápio
print("1 - Pão de queijo - R$ 4.50")
print("2 - Coxinha    -    R$ 6.00")
print("3 - Pastel     -    R$ 7.00")
print("4 - Suco       -    R$ 5.00")
print("5 - Café       -    R$ 3.00")
# entrada
codigo = int(input("Código: "))
quantidade = int(input("Quantidade: "))
# decisão
if codigo == 1:
    preco = 4.5
elif codigo == 2:
    preco = 6.0
elif codigo == 3:
    preco = 7.0
elif codigo == 4:
    preco = 5.0
elif codigo == 5:
    preco = 3.0
else:
    preco = 0
# saída
if preco == 0:
    print("Código inválido")
else:
    print("Total: R$", preco * quantidade)
