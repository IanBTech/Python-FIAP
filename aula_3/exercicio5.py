#5. Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma, subtração, multiplicação e divisão.
# Exiba o resultado da operação solicitada.

num1 = float(input('Escreva o primeiro número: '))
operacao = str(input('Escreva a operação que deseja realizar ((+), (-), (/), (*)): '))
num2 = float(input('Escreva o segundo número: '))

if operacao == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operacao == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operacao == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif operacao == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print(f'operação invalida, digite um número válido e utilize apenas (+), (-), (/), (*).')