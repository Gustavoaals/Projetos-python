import random
import time 

print("-" * 35)
print("SORTEIO QUEM VAI APAGAR O QUADRO")
print("-" * 35)

aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))

sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])

#ou sorteado = [aluno1,aluno2,aluno3,aluno4]
#escolhido = random.choice(lista)

print("Realizando o sorteio")
time.sleep(2)

print("E quem vai limpar o quadro é...")
time.sleep(3)

print (f"Parábens,{sorteado}! você vai limpar o quadro.")



