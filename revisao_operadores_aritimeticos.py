num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

s = num1 + num2 # Soma
m = num1 * num2 # multiplicação
d = num1 / num2 # Divisão
di = num1 // num2 # Divisão inteira
e = num1 ** num2 # potência (\n - quebra uma linha )

print(f"A soma é {s},\n o produto é {m} e a divisão é {d:.2f}")
print((f"Divisão inteira {di} e a potencia {e}"))
