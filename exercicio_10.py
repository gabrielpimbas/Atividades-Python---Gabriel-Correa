# exercício 10 - aprovado ou reprovado
# objetivo: resolver aprovado ou reprovado conforme o enunciado

# entrada
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
# processamento
media = (n1 + n2) / 2
# decisão e saída
if media >= 7:
    print("Média:", media, "— Aprovado")
else:
    print("Média:", media, "— Reprovado")
