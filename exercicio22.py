#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str (input("Digite seu nome completo: ")).strip() #Elimina os espaco antes e depois
primeiro_nome = nome.split()[0]

print(f"Seu nome em Maiúsculas é {nome.upper()}")
print(f"Seu nome em minuscúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {len(primeiro_nome)} caractere ")