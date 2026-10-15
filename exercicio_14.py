# exercício 14 - radar de velocidade
# objetivo: resolver radar de velocidade conforme o enunciado

# entrada
velocidade = int(input("Velocidade: "))
# decisão e saída
if velocidade > 80:
    print("Multado! Você passou", velocidade - 80, "km/h do limite.")
else:
    print("Velocidade dentro do limite. Boa viagem!")
