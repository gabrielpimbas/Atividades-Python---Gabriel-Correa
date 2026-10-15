# exercício 33 - voto obrigatório
# objetivo: determinar a situação de voto de uma pessoa com base na idade

# comando de entrada
idade = int (input ("Digite a idade: "))

# lógica de determinação da situação de voto
if idade < 16:
    print ("Não pode votar.")
    
elif idade >= 16 and idade < 17:
    print ("Voto facultativo.")
    
elif idade >= 18 and idade <= 70:
    print ("Voto obrigatório.")
    
else:
    print ("Voto facultativo.")