tabela = {"alface": 0.45, "batata": 1.2, "tomate": 2.3, "feijão": 1.5}
while True:
    produto = input("Digite o nome do produto ou fim para terminar:")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço: R$ {tabela[produto]:.2f}")
    else:
        print("Produto não encontrado.")