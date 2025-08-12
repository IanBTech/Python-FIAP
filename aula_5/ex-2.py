# 2. Faça um programa que leia duas listas e que gere
# uma terceira com os elementos das duas primeiras.

L1 = ["Michele","Gustavo", "Giovanna", "Vinicius"]
L2 = []

while True:
    aluno_novo = input("Nome (fim para sair): ")
    if aluno_novo == "fim":
        break
    L2.append(aluno_novo)

L3 = []
L3.extend (L1 + L2)
print(L3)