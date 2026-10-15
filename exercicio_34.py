# exercicio 34 - aprovação com frenquência
# objetivo: determinar a aprovação de um aluno com base em nota e frequência

# comandos de entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = int(input("Digite a frequência: "))

# cálculo da média
media = (nota1 + nota2) / 2

# comando com lógica determinando a situação do aluno
if media >= 7.0 and frequencia >= 75:
    print("Aluno aprovado.")
    
elif media < 7.0 and frequencia >= 75:
    print("Reprovado por nota.")
    
elif media >= 7.0 and frequencia < 75:
    print("Reprovado por falta.")
    
else:
    print("Reprovado por nota e falta.")