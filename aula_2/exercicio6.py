#6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

dias = int(input("Valor em dias:"))
horas = int(input("Valor em horas:"))
minutos = int(input("Valor em minutos:"))
segundos = int(input("Valor em segundos:"))

s1 = (dias * 86400)
s2 = (horas * 3600)
s3 = (minutos * 60)
s4 = segundos

soma = s1 + s2 + s3 + s4

print("o valor em segundos é:", soma)
