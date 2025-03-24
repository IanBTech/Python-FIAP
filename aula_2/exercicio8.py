#8. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco = float(input("Escreva o valor do produto: "))
percentual = float(input("Escreva o valor percentual do desconto a ser aplicado (apenas numeros): "))
desconto = (preco * percentual)/100
valorf = preco - desconto

print(f"O valor do desconto é igual a R$ {desconto} o que resulta no valor final de {valorf:.2f}")
