#3. Escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, de 15%.

salario = float(input('Digite seu salário: '))
calculo1 = ((salario * 10)/100) + salario
calculo2 = ((salario * 15)/100) + salario
if salario > 1250:
    print(f'R$ {calculo1:.2f}')
else:
    print(f'R$ {calculo2:.2f}')