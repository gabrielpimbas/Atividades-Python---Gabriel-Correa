# exercício 5 - minutos em horas
# objetivo: resolver minutos em horas conforme o enunciado

# entrada
minutos = int(input("Minutos: "))
# processamento
horas = minutos // 60
resto = minutos % 60
# saída
print(horas, "hora(s) e", resto, "minuto(s)")
