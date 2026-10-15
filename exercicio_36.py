# exercicio 36 - pedra, papel e tesoura
# objetivo: implementar o jogo pedra, papel e tesoura

# comandos de entrada
jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")

# lógica do jogo
if jogador1 == jogador2:
    print("Empate!")
elif (
    (jogador1 == "pedra" and jogador2 == "tesoura")
    or (jogador1 == "papel" and jogador2 == "pedra")
    or (jogador1 == "tesoura" and jogador2 == "papel")
):
    print("Jogador 1 vence!")
else:
    print("Jogador 2 vence!")

if jogador1 != "pedra" and jogador1 != "papel" and jogador1 != "tesoura":
    print("Jogada inválida.")
elif jogador2 != "pedra" and jogador2 != "papel" and jogador2 != "tesoura":
    print("Jogada inválida.")
