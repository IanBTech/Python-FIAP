#Dupla: Ian Batinga Barbosa / Giovanna Carmona Roman Lopes
#calcular média semestral

#obtenção das notas (entradas)
print("Digite suas notas de 0 a 10!")
num1 = float(input('Checkpoint 1 = '))
num2 = float(input('Checkpoint 2 = '))
num3 = float(input('Checkpoint 3 = '))
sp1 = float(input('Sprint 1 = '))
sp2 = float(input('Sprint 2 = '))
gs = float(input('Global Solution = '))

#cálculo e descarte da menor nota
maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
elif num3 >= num1 and num3 >= num2:
    maior = num3

maior2 = num1
if num2 >= num1 and num2 <= num3:
    maior2 = num2
elif num3 >= num2 and num3 <= num1:
    maior2 = num3

#cálculo da média Aritimética
mediaA = (maior + maior2 + sp1 + sp2)/4

#cálculo da média Semestral
mediaS = (mediaA*0.4) + (gs*0.6)

#saída
print(f'Média semestral = {mediaS:.1f}')