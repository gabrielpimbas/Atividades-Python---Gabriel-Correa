# exercício 22 - termômetro da serra
# objetivo: resolver termômetro da serra conforme o enunciado

# entrada
temperatura = float(input("Temperatura: "))
# decisão e saída
if temperatura < 0:
    print("Abaixo de zero — risco de geada!")
elif temperatura < 10:
    print("Muito frio — capriche no agasalho")
elif temperatura < 18:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
else:
    print("Calor")
