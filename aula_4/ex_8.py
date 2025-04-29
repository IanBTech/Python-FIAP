# 8. Escreva um programa que pergunte o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total
# do ganho com juros no período.

n = 1 #contador
x = float(input("Digite o valor do depósito inicial: "))
t = float(input("Digite o valor do juros: "))
t += 1
while n <= 24:
    ppc = x * t
    print(f"{n} mês(es) = {ppc:.2f}")
    n += 1
    x = ppc