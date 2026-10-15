# exercício 19 - situação do aluno
# objetivo: resolver situação do aluno conforme o enunciado

# entrada
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
# processamento
media = (n1 + n2) / 2
# decisão e saída
if media >= 7:
    print("Média", media, "— Aprovado")
elif media >= 5:
    print("Média", media, "— Recuperação")
else:
    print("Média", media, "— Reprovado")
