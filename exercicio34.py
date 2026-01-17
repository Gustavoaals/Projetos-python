#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input("Qual é seu salário? R$"))

aumento10 = (10 * salario) / 100 + salario
aumento15 = (15 * salario) / 100 + salario

if salario >= 1250: 
    print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento10:.2f} ")
else:
    print(f"Agora quem ganhava R${salario:.2f} agora vai ganhar R${aumento15:.2f}")