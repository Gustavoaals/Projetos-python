#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite a veloidade do seu carro: "))

if velocidade > 80 :
    print(f"MULTADO!!Você exedeu a velocidade de 80km/h e foi multado, e vai custa R${velocidade}")
    multa = (velocidade - 80) * 7
else:
    print("Tenha um bom dia! Dirija com seguraça.")