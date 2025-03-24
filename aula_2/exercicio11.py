#11. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input("Digite quantos km foram percorridos: "))
periodo = int(input("Digite o periodo de dias que o carro foi alugado: "))
pagamento = float(km * 0.15) + float(periodo * 60)

print(f"o pagamento a ser realizado por utilizar durante {periodo} dias e percorrer {km} km é de  R$ {pagamento:.2f}")
