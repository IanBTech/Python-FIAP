#2. Escreva um programa que leia três números e que
# imprima o maior e o menor.

num1 = float(input('Escreva um numero: '))
num2 = float(input('Escreva um numero: '))
num3 = float(input('Escreva um numero: '))

maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
elif num3 >= num1 and num3 >= num2:
    maior = num3

menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
elif num3 <= num1 and num3 <= num2:
    menor = num3

print(f'o maior número é: {maior:.0f}')
print(f'o menor número é: {menor:.0f}')
