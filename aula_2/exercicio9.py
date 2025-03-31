#9. Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

d = float(input("Digite a distância a percorrer em km: "))
vm = float(input("Digite a velociade média do veiculo em km/h: "))
tempo = d/vm

print(f"O tempo estimado para percorrer o percurso com essa velociadade é de {tempo:.2f} horas")
