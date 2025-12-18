# Desenvolva um programa que leia as duas notas de um aluno e calcule a media


nome = str(input("Qual é seu nome?: "))
nota1 = float(input("Digite a primeira Nota: "))
nota2 = float(input("Digite a segunda Nota: "))

media = (nota1 + nota2) / 2

print(f"Então, {nome}, a media das sua notas foram: {media:.2f} ")
