# 4. Faça um programa que lê e imprime uma lista de
# compras até que seja digitado fim.

compras = []
while True:
    item = input("Entre com o item (fim para encerrar): ")
    if item == "fim":
        break
    compras.append(item)
for i in compras:
    print(i)