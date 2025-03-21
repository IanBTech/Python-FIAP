#4. Escreva um programa que pergunte a distância que  um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens
# de até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input('Escreva quantos km deseja percorrer em km: '))
calculo1 = distancia * 0.50
calculo2 = distancia * 0.45

if distancia < 200:
    print(f'R$ {calculo1:.2f}')
else:
    print(f'R$ {calculo2:.2f}')
