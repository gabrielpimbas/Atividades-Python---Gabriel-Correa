# exercício 24 - calculadora de imc
# objetivo: resolver calculadora de imc conforme o enunciado

# entrada
peso = float(input("Peso: "))
altura = float(input("Altura: "))
# processamento
imc = peso / (altura * altura)
# decisão
if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc < 25:
    situacao = "Peso normal"
elif imc < 30:
    situacao = "Sobrepeso"
else:
    situacao = "Obesidade"
# saída
print("IMC:", round(imc, 2), "—", situacao)
