#Sistema de login simples

login = (input("Digite o Usuário: "))
senha = (input("Digite a Senha: "))

if login == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")