# exercício 16 - saque no caixa eletrônico
# objetivo: resolver saque no caixa eletrônico conforme o enunciado

# entrada
saldo = float(input("Saldo: "))
saque = float(input("Saque: "))
# decisão e saída
if saldo >= saque:
    saldo = saldo - saque
    print("Saque realizado. Novo saldo: R$", saldo)
else:
    print("Saldo insuficiente")
