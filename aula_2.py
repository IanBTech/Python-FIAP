print("hello world")

#1. faça um programa que exiba seu nome na tela

print("Meu nome é Ian Batinga Barbosa")

#2. Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5

a = 3
b = 5

print((2 * a) * (3 * b))

#3. Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

a1 = 6
a2 = 9
a3 = 1

print(a1 + a2 + a3)

#4. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela

num1 = int(input("Escreva um número para somar: "))
num2 = int(input("Escreva o segundo numero para somar com o anterior: "))
print("A soma desses números é", num1 + num2)

#5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Escreva uma medida em métros para tornar em milímetros: "))

print(metros * 1000)

#6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total
# em segundos.

dias = int(input("Escreva a quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))

print("A soma dos dias, horas, minutos, segundos em segundos é: ", (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos)
