#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome completo: ")).strip()

nome = n.split()
print(f"Seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[-1]}")
