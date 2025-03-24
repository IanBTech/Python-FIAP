#7. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Escreva o valor do seu salário: "))
aumento = float(input("Escreva o valor da porcentagem de aumento (apenas numeros): "))
aumentamento = (aumento * salario)/100
aumentado = aumentamento + salario
print(f"O aumento do seu salário foi de R$ {aumentamento} somado com o atual resulta em R$ {aumentado}")
