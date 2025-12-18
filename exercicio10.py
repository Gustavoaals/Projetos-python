# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Digite um valor em reais R$: "))

dolar = reais / 3.27

print(f"Com R${reais} você pode comprar {dolar:.2f} dolares")
