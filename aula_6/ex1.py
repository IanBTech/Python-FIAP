#1. Altere o programa do exemplo anterior de formar
# a imprimir o menor elemento da lista.

L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)

