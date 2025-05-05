#Dupla: Ian Batinga Barbosa / Giovanna Carmona Roman Lopes
#calcular média de 2 semestres (anual)

#obtenção das notas (entradas)
n = 1
media1 = 0
media2 = 0
mediafinal = 0
while n <= 2:
    print("Digite suas notas de 0 a 10!")
    cp1 = float(input('Checkpoint 1 = '))
    cp2 = float(input('Checkpoint 2 = '))
    cp3 = float(input('Checkpoint 3 = '))
    sp1 = float(input('Sprint 1 = '))
    sp2 = float(input('Sprint 2 = '))
    gs = float(input('Global Solution = '))

    #cálculo e descarte da menor nota
    if cp1 <= cp2 and cp1 <= cp3:
        soma = cp2 + cp3
    elif cp2 <= cp1 and cp2 <= cp3:
        soma = cp1 + cp3
    else:
        soma = cp1 + cp2

    #cálculo da média Aritimética
    mediaA = (soma + sp1 + sp2)/4

    #cálculo da média Semestral
    mediaS = (mediaA*0.4) + (gs*0.6)

    #calculo da media final
    if n == 1:
        media1 = mediaS
    else:
        media2 = mediaS

    mediafinal = ((media1*0.4) + (media2*0.6))
    print(f'Media semestral = {mediaS:.1f}')
    n += 1
# saída
print(f'Média final = {mediafinal:.1f}')
