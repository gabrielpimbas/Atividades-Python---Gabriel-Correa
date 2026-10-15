# exercício 25 - radar com tipo de infração
# objetivo: resolver radar com tipo de infração conforme o enunciado

# entrada
limite = float(input("Limite: "))
velocidade = float(input("Velocidade: "))
# decisão e saída
if velocidade <= limite:
    print("Sem infração")
else:
    percentual = (velocidade - limite) / limite * 100
    if percentual <= 20:
        tipo = "Infração média"
    elif percentual <= 50:
        tipo = "Infração grave"
    else:
        tipo = "Infração gravíssima"
    print(str(round(percentual, 2)) + "% acima — " + tipo)
