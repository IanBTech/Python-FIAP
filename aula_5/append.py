L = []
while True:
    na = str(input("Digite o nome de um aluno (0 sai): "))
    if na == "0":
        break
    L.append(na)

L.sort() #ordem alfabetica
x = 0
while x < len(L):
    print(L[x])
    x += 1