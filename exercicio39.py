idade = int(input("Qual sua idade ? "))

if idade == 18 or idade > 18:
    print("Você ja é maior de idade, precisa se alistar.")
elif idade < 18:
    print(f"Você ainda é menor de idade, ainda não pode se alistar.")
else:
    print(f"Ainda falta {idade - 18} anos para você se alistar. ")