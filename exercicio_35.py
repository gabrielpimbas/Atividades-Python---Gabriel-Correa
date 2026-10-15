# exercicio 35 - calculadora
# objetivo: realizar operações matemáticas básicas

# comandos de entrada
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

# comando que verifica a operação e realiza o cálculo
if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":

    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Operador inválido.")
