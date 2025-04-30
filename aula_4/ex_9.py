# 9. Altere o programa anterior de forma a perguntar
# também o valor depositado mensalmente. Esse valor
# será depositado no início de cada mês e você deve
# considerá-lo para o cálculo de juros do mês seguinte.

n = 1 #contador
x = float(input("Digite o valor do depósito inicial: "))
t = float(input("Digite o valor do juros: "))
m = float(input("Digite o valor de deposito mensal: "))
t += 1
while n <= 24:
    ppc = x * t
    print(f"{n} mês(es) = {ppc:.2f}")
    n += 1
    x = ppc + m