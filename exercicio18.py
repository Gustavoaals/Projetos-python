#programa que leia um ângulo qualquer e mostre
#  na tela o valor do seno, cosseno e tangente desse ângulo.
import math 
an = float(input("Digite o valor do angulo: "))

seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))

print(f"O ângulo de {an} tem o Seno de {seno:.2f}")
print(f"O ângulo de {an} tem o Cosseno de {cosseno:.2f}")
print(f"O ângulo de {an} tem a Tangenete de {tangente:.2f}")