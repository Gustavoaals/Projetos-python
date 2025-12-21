#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
#triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hi = math.hypot(cateto_adjacente,cateto_oposto)

print(f"A hipotenusa vai medir {hi:.2f}")