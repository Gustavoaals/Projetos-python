#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nasc = input("Em que cidade você nasceu? ").strip().lower()

print(nasc.startswith("santo"))
