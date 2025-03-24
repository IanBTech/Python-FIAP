#13. Escreva um programa que receba o salário de um funcionário (float) e retorne o resultado
# do novo salário com reajuste de 35%.

salario1 = float(input("Digite o valor do seu salario: "))
reajuste = (salario1 * 35)/100

print(f"O seu salario com reajuste de 35% é de {reajuste:.2f}")