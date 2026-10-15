# exercício 32 - login com usuário e senha
# objetivo: permitir que um usuário entre no sistema se as credenciais estiverem corretas

# comandos de entrada
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

# lógica de autenticação
if usuario == "aluno":
    if senha == "1234":
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")
