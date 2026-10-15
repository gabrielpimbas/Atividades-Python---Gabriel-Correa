# exercício 21 - faixa etária
# objetivo: resolver faixa etária conforme o enunciado

# entrada
idade = int(input("Idade: "))
# decisão e saída
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
