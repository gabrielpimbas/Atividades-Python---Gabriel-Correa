# exercicio 39 - caixa eletrônico: contagem de notas
# objetivo: distribuir o valor do saque em notas de 100, 50, 20 e 10

# comando de entrada
valor = int(input("Digite o valor do saque: "))

# comando lógico para verificar se o valor é válido
if valor <= 0 or valor % 10 != 0:
    print("Valor inválido para saque.")

# comando lógico para calcular a contagem de notas
if valor > 0:
    notas_100 = valor // 100
    valor %= 100
    notas_50 = valor // 50
    valor %= 50
    notas_20 = valor // 20
    valor %= 20
    notas_10 = valor // 10
    valor %= 10

    # comando de saída onde exibi a contagem de notas
    print(notas_100, " nota(s) de R$ 100")
    print(notas_50, " nota(s) de R$ 50")
    print(notas_20, " nota(s) de R$ 20")
    print(notas_10, " nota(s) de R$ 10")
