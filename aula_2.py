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
ssegs = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(f"A soma dos dias, horas, minutos, segundos em segundos é: {ssegs}")

#7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Escreva o valor do seu salário: "))
aumento = float(input("Escreva o valor da porcentagem de aumento (apenas numeros): "))
aumentamento = (aumento * salario)/100
aumentado = aumentamento + salario
print(f"O aumento do seu salário foi de R$ {aumentamento} somado com o atual resulta em R$ {aumentado}")

#8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco = float(input("Escreva o valor do produto: "))
percentual = float(input("Escreva o valor percentual do desconto a ser aplicado (apenas numeros): "))
desconto = (preco * percentual)/100
valorf = preco - desconto

print(f"O valor do desconto é igual a R$ {desconto} o que resulta no valor final de {valorf:.2f}")

#9. Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

d = float(input("Digite a distância a percorrer: "))
vm = float(input("Digite a velociade média do veiculo: "))
tempo = d/vm

print(f"O tempo estimado para percorrer o percurso com essa velociadade é de {tempo:.2f}")

#10. Escreva um programa que converta uma temperatura digitada em ºC em ºF.
# A fórmula para essa conversão é F = ((9 x C) / 5) + 32

C = float(input("Digite a temperatura em Celcius: "))
F = ((9 * C) / 5) + 32

print(f"A temperatura {C}ºC convertida em ºF é {F}ºF")


