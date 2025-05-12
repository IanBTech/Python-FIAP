# 1. Escreva um programa para ler 7 notas e calcular a
# média aritmética.

notas = [6, 7, 5, 8, 9, 5, 8]
soma = 0
x = 0
while x < 7:
    soma += notas[x]
    x += 1
print(f"Média = {(soma/x):.2f}")