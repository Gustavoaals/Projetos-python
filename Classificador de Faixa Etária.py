idade = int(input("Qual sua idade: "))

if idade < 12:
    print("Você ainda é criança.")
elif idade < 18:
    print("Você é adolescente")
else:
    print(f"Você é adulto pois tem {idade} anos")