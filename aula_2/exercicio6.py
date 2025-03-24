#6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total
# em segundos.

dias = int(input("Escreva a quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))
ssegs = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"A soma dos dias, horas, minutos, segundos em segundos é: {ssegs}")