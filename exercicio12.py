# Algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

produto = float(input("Qual é o preço do produto? R$"))

desconto = produto - (produto * 5 / 100)

print(f"O pruduto que custava R${produto}, na promoção com desconto de 5% agora vai custar R${desconto:.2f}")