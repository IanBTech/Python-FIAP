# 6. Faça um programa para exibir os resultados de uma
# tabuada no formato: 2 x 1 = 2, 2 x 2 = 4, ...

n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x:.0f}")
    x = x + 1