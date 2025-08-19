# 3. Faça um programa para selecionar os elementos de
# uma lista e copiá-los para outras. Copiar os valores
# pares para a lista P que estão na lista V = [9, 8, 7, 12, 0,
# 13, 21] e os ímpares para a lista I.

V = [9,8,7,12,0,13,21]
P = []
I = []

for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print("Pares: ",P)
print("Impares: ",I)