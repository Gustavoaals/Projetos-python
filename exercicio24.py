#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nasc = input("Em que cidade você nasceu? ").strip().lower()

print(nasc.startswith("santo"))

#ou de outra forma:
#cidade = str(input("onde voce nasce? "))
#print(cid[:5].upper() == "SANTO")