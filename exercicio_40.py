# exercicio 40 - bilheteria da festa do pinhão
# objetivo: calcular o valor da entrada com base na idade e situação de estudante

# comandos de entrada
idade = int(input("Digite a idade: "))
estudante = input("É estudante? (s/n): ")

# comandos de processamento para verificar a situação do cliente
if idade < 6:
    tipo = "Gratuito"
    valor = 0
elif idade <= 17 or idade >= 60 or estudante == "s":
    tipo = "Meia entrada"
    valor = 20
else:
    tipo = "Inteira"
    valor = 40

# comandos de processamento que calculam o valor final com base nas informações do cliente e forma de pagamento
if valor == 0:
    print("Gratuito - R$ 0.00")
else:
    pagamento = int(input("1 - PIX\n2 - Débito\n3 - Crédito\nEscolha uma opção: "))
    if pagamento == 1:
        forma = "PIX"
        valor = valor * 0.95
    elif pagamento == 2:
        forma = "Débito"
    elif pagamento == 3:
        forma = "Crédito"
        valor = valor * 1.05
    else:
        forma = "Inválida"

    # comandos de saída onde mostram os resultados
    if forma == "Inválida":
        print("Forma de pagamento inválida!")
    else:
        print(tipo, "-", forma, "- R$", valor)
