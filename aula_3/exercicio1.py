#1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba
# uma mensagem dizendo que o usuário foi multado.Nesse caso, exiba o valor da multa,
# cobrando R$5 por km acima de 80km/h.

velocidade = float(input("Digite a velocidade em Km/h: "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f"Você foi multado em R$ {multa:.2f} ")
else:
    print("Você está dentro do limite de velocidade!")
