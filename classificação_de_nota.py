#Classificação de nota

nota = float(input("Digite uma nota de 0 a 10: "))

if nota >= 9 and nota <= 10:
    print("Execelente")
elif nota >= 7 and nota <= 8:
    print("Bom")
elif nota >= 5 and nota <= 6:
    print("Regular")
elif nota >= 0 and nota < 5:
    print("Ruim")
elif nota > 10:
    print("Notas aceitas somente de 1 a 10.")




