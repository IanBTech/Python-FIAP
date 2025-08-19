# 1. Altere o exemplo anterior de forma a solicitar ao
# usuário o produto e a quantidade vendida. Verifique se o
# nome do produto digitado existe no dicionário e só então
# efetue a baixa no estoque.

estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]}

produto = input("Digite o produto: ")
vendido = int(input("Digite o venda: "))
venda = [[produto, vendido]]

total = 0
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco} = {custo}")
    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total: {total}")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: R$ {dados[1]}")