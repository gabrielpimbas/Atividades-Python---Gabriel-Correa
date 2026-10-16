# exercicio 37 - três números em ordem crescente
# objetivo - ordenar três números em ordem crescente

# comandos de entrada
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# comandos lógicos que ordenam os números
if numero1 <= numero2 <= numero3:
    print(numero1, numero2, numero3)
elif numero1 <= numero3 <= numero2:
    print(numero1, numero3, numero2)
elif numero2 <= numero1 <= numero3:
    print(numero2, numero1, numero3)
elif numero2 <= numero3 <= numero1:
    print(numero2, numero3, numero1)
elif numero3 <= numero1 <= numero2:
    print(numero3, numero1,numero2)
else:
    print(numero3,numero2,numero1)