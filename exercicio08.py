# conversor de medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
print(f"A medida em metros é de: {medida}m e corresponde a {cm:.0f}cm e {mm:.0f}mm")

print(f"A medida em Quilômetros é de {km}km e em hectômetros {hm}hm e decâmetro {dam}dam ")
