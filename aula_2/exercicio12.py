#12. Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (x2 + y2) / (x – y)2

x = int(input("Escreva um numero inteiro: "))
y = int(input("Escreva outro numero inteiro: "))
z = ((x * x) + (y * y)) / ((x - y) * (x - y))

print(f"De acordo com a formula z = (x² + y²) / (x – y)² o resultado de z obitido foi de {z}")