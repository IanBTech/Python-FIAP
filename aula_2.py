print("hello world")

#1. faça um programa que exiba seu nome na tela

print("Meu nome é Ian Batinga Barbosa")

#2. Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5

a = 3
b = 5
equacao = ((2 * a) * (3 * b))
print(equacao)

#3. Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

a1 = 6
a2 = 9
a3 = 1
soma = (a1 + a2 + a3)
print(soma)

#4. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela

num1 = int(input("Escreva um número para somar: "))
num2 = int(input("Escreva o segundo numero para somar com o anterior: "))
soma1 = num1 + num2
print(f"A soma desses números é {soma1}")

#5. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Escreva uma medida em métros para tornar em milímetros: "))
milimetros = metros * 1000
print(milimetros)

#6. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total
# em segundos.

dias = int(input("Escreva a quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))

print("A soma dos dias, horas, minutos, segundos em segundos é: ", (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos)

#7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Escreva o valor do seu salário: "))
aumento = float(input("Escreva o valor da porcentagem de aumento (apenas numeros): "))

print("O aumento do seu salário foi de R$", ((aumento * salario)/100), "somado com o atual resulta em R$", ((aumento * salario)/100) + salario)

#