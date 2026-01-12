#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().upper().lower()

print(f"A letra A aparece {frase.count('a')}")
print(f"A primeira letra A aparece na posição {frase.find('a')}")
print(f"A ultima letra A aparece na posicao {frase.rfind('a')+1}") 