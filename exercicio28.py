from random import randint
print('-' * 20)
print("JOGO DE ADVINHAÇÃO")
print('-' * 20)

num = int(input("Digite um número entre 0 e 5: "))
maquina = randint(0,5)

if num == maquina:
    print(f"PARABÉNS!!, o seu numero {num} é igual a da maquina {maquina}")
else:
    print("Que pena você perdeu, tente novamente.")
