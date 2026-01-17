# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se 
#podem ou não formar um triângulo.
import time
print('-=' * 20)
print("ANALISANDOR DE TRINÂNGULO".center(40))
print('-=' * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
time.sleep(2)
print("ANALISANDO...".center(40))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos acima podem formar um triângulos!")
else:
    print("Os segmentos acima NÃO podem formar triângulo")