#3. Modifique o exemplo anterior de forma a realizar a
# mesma tarefa, mas sem utilizar a variável achou. Dica:
# observe a condição de saída do while.

L = [15, 7, 27, 39]
pesquisa = int(input("Digite o valor a pesquisar: "))
x = 0
while x < len(L):
    if L[x] == pesquisa:
        break
    x += 1
if x < len(L):
    print(f"{pesquisa} achado na posição {x}.")
else:
    print(f"{pesquisa} não encontrado.")
