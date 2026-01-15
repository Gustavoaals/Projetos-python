#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
from time import sleep

viagem = float(input("Qual a distancia da viagem? "))

print("PROCESSANDO....")
(sleep(1))

if viagem <= 200:
    print(f"Você está preste a começar uma viagem de {viagem}km")
    print(f"E o preço da viagem é de R${viagem * 0.50:.2f}")
else:
    print(f"Sua viagem é mais longa {viagem}km")
    print(f"E irá custa R${viagem * 0.45:.2f}") 