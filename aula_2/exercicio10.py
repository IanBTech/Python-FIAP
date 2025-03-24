#10. Escreva um programa que converta uma temperatura digitada em ºC em ºF.
# A fórmula para essa conversão é F = ((9 x C) / 5) + 32

C = float(input("Digite a temperatura em Celcius: "))
F = ((9 * C) / 5) + 32

print(f"A temperatura {C}ºC convertida em ºF é {F}ºF")
