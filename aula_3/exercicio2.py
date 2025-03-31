#2. Escreva um programa que leia três números e que
# imprima o maior e o menor.

num1 = float(input('Escreva um numero: '))
num2 = float(input('Escreva um numero: '))
num3 = float(input('Escreva um numero: '))

#maior número
if num1 >= num2 and num1 >= num3:
    print(f'o maior número é {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'o maior número é {num2}')
elif num3 >= num1 and num3 >= num2:
    print(f'o maior número é {num3}')
else:
    print("Algo de errado não está certo.")

#menor número
if num1 <= num2 and num1 <= num3:
    print(f'o menor número é {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'o menor número é {num2}')
elif num3 <= num1 and num3 <= num2:
    print(f'o menor número é {num3}')
else:
    print("Algo de errado não está certo.")