# exercício 30 - ano bissexto
# objetivo: resolver ano bissexto conforme o enunciado

# entrada
ano = int(input("Ano: "))
# decisão e saída
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Bissexto")
else:
    print("Não é bissexto")
