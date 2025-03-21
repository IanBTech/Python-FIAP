#6. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

imovel = float(input('Escreva o valor do imovel: '))
salario = float(input('Escreva o salario: '))
anos = float(input('Escreva a quantidade de anos a pagar: '))

prestacao = (imovel / anos) / 12
permissao = (salario * 30)/100
if prestacao > permissao:
    print(f'o valor da prestação do seu imóvel para {anos:.0f} anos não permite que você pague com menos de 30% do seu salário.')
    print(f'Seu pedido de emprestimo foi negado!')
else:
    print(f'Seu pedido de empréstimo foi aprovado!')