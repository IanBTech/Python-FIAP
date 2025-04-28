# 7. Modifique o programa interior de forma que o usuário
# também digite o início e o fim da tabuada, em vez de
# começar com 1 e 10.

n = int(input("Tabuada de: "))
w = int(input("Digite até quanto deseja multiplicar: "))
x = 1
while x <= w:
    print(f"{n} x {x} = {n * x:.0f}")
    x = x + 1