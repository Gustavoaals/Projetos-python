# crie um algoritmo que leia um numero que mostre o seu
# dobro, triplo e raiz quadrada

num = int(input("Digite um numero: "))


print(f"O dobro de {num} é {num*2} e o triplo {num*3} ")
print(f"E a Raiz quadrada é {num ** (1/2):.2f}")
print(f"E a raiz quadrada é {pow(num, (1/2)):.2f}")# outra forma de calcular raiz quadrada
