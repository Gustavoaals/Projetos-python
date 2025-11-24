salario_mensal = float(input("Qual o seu salário?: "))
horas_trabalhadas = float(input("Horas trabalhas: "))

print(f"Salário mensal: R${salario_mensal}")
print(f"Horas trabalhadas: {horas_trabalhadas} horas")

valor_hora = salario_mensal // horas_trabalhadas

print(f"O valor hora é de R${valor_hora}")
