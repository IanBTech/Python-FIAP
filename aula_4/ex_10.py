# 10. Escreva um programa que
# leia números inteiros do teclado.
# O programa deve ler os números
# até que o usuário digite 0 (zero).
# No final da execução, exiba a
# quantidade de números digitados,
# assim como a soma e a média
# aritmética.
from typing import Union, Any

soma = 0
qtd = 0
media = 0
while True:
    num = int(input("Digite um número a somar ou 0 para sair: "))
    if num == 0:
        break
    soma += num
    qtd += 1
    media = soma / qtd
print(f"quantidade = {qtd:.0f}")
print(f"soma = {soma:.0f}")
print(f"media = {media:.0f}")