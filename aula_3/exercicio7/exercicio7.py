#7. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
# I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela seguir.

kWh = float(input('Escreva a quantidade de kWh consumida: '))
instalacao = str(input('Selecione o tipo da sua instalação (R) residências, (I) indústrias e (C) comércios: ')).upper()
operacaoR1 = kWh * 0.4
operacaoR2 = kWh * 0.65
operacaoC1 = kWh * 0.55
operacaoC2 = kWh * 0.60
operacaoI1 = kWh * 0.55
operacaoI2 = kWh * 0.60

if instalacao == 'R' and kWh < 500 :
    print(f'O valor a ser pago pelo consumo Residencial de {kWh}kWh é R$ {operacaoR1:.2f}')
elif instalacao == 'R' and kWh > 500 :
    print(f'O valor a ser pago pelo consumo Residencial de {kWh}kWh é R$ {operacaoR2:.2f}')
elif instalacao == 'C' and kWh < 1000 :
    print(f'O valor a ser pago pelo consumo Comercial de {kWh}kWh é R$ {operacaoC1:.2f}')
elif instalacao == 'C' and kWh > 1000 :
    print(f'O valor a ser pago pelo consumo Comercial de {kWh}kWh é R$ {operacaoC2:.2f}')
elif instalacao == 'I' and kWh < 5000 :
    print(f'O valor a ser pago pelo consumo Industrial de {kWh}kWh é R$ {operacaoI1:.2f}')
elif instalacao == 'I' and kWh > 5000 :
    print(f'O valor a ser pago pelo consumo Industrial de {kWh}kWh é R$ {operacaoI2:.2f}')
else:
    print('Selecione corretamente o tipo da sua instalação (R) , (I) e (C)')