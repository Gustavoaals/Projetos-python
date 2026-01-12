#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um número: "))

num, unidade = divmod(num, 10)
num, dezena = divmod(num, 10)
num, centena = divmod(num, 10)
num, milhar = divmod(num, 10)

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)
