# Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário, com 15% de aumento.

salario = float(input("Insira seu salário: R$"))

aumento = (salario * 15 / 100) + salario

print(f"Seu salário de R${salario} teve um auemnto de 15%, que agora ficou de R${aumento}")