# 3. Faça um programa para selecionar os elementos de
# uma lista e copiá-los para outras. Copiar os valores
# pares para a lista P que estão na lista V = [9, 8, 7, 12, 0,
# 13, 21] e os ímpares para a lista I.

V = [9,8,7,12,0,13,21]
P = []
p = []

for p in range (0,30,2):
    if V == p:
        P.append(p)

print(P)