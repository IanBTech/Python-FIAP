#2. Escreva um programa que leia três números e que
# imprima o maior e o menor.

num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva um numero: '))
num3 = int(input('Escreva um numero: '))

#maior número
if num1 > num2 > num3:
    print(f'o maior número é {num1}')
if num1 > num3 > num2:
    print(f'o maior número é {num1}')
if num2 > num1 > num3:
    print(f'o maior número é {num2}')
if num2 > num3 > num1:
    print(f'o maior número é {num2}')
if num3 > num2 > num1:
    print(f'o maior número é {num3}')
if num3 > num1 > num2:
    print(f'o maior número é {num3}')

#menor número
if num1 > num2 > num3:
    print(f'o menor número é {num3}')
if num1 > num3 > num2:
    print(f'o menor número é {num2}')
if num2 > num1 > num3:
    print(f'o menor número é {num3}')
if num2 > num3 > num1:
    print(f'o menor número é {num1}')
if num3 > num2 > num1:
    print(f'o menor número é {num1}')
if num3 > num1 > num2:
    print(f'o menor número é {num2}')