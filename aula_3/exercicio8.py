#8. Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado
# (para ser aprovado a média deve ser no mínimo 6).

nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2

if media > 6:
    print('Aprovado')
else:
    print('Reprovado')