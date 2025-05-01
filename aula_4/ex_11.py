# 11. Escreva um programa para
# controlar uma pequena máquina
# registradora. Você deve solicitar
# ao usuário que digite o código do
# produto e a quantidade
# comprada. Utilize a tabela de
# códigos a seguir para obter o
# preço de cada produto:
# Código Operação
# 1 = 0,50
# 2 = 1,00
# 3 = 4,00
# 5 = 7,00
# 9 = 8,00
# Seu programa deve exibir o total
# das compras depois que o
# usuário digitar 0. Qualquer outro
# código deve gerar a mensagem
# de erro “Código inválido”.

p = 0
while True:
    c = int(input("Código do produto (0 para sair): "))
    preco = 0
    if c == 0:
        break
    elif c == 1:
        preco = 0.5
    elif c == 2:
        preco = 1
    elif c == 3:
        preco = 4
    elif c == 5:
        preco = 7
    elif c == 9:
        preco = 8
    else:
        print("Código inválido!")
    if preco != 0:
        qtd = int(input("Quantidade: "))
        p = p + (preco * qtd)
print(f"Total a pagar R${p:.2f}")
