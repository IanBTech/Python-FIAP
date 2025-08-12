#2. A lista de temperaturas de Mons, na Bélgica, foi
# armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça
# um programa que imprima a menor e a maior
# temperatura, assim como a temperatura média.


T = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = T[0]
for e in T:
    if e < minimo:
        minimo = e
print(f"Temperatura minima {minimo:.0f}")

maximo = T[0]
for e in T:
    if e > maximo:
        maximo = e
print(f"Temperatura máxima {maximo:.0f}")

soma = 0
for e in T:
    soma += e
print(f"Temperatura Media {soma/len(T):.0f}")


media = sum(T)/len(T) # "sum" = soma tudo na lista
print(f"Temperatura Média {media:.0f}")
