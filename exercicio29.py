#

velocidade = int(input("Digite a veloidade do seu carro: "))

multa = velocidade * 7

if velocidade >= 80:
    print(f"Você foi ultrapassou a velocidade de 80km/h e foi multado, e vai custa R${multa}")
else:
    print("Você andou na velocidade recomendada.")