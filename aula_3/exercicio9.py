#9. Refaça o exercício 4, identificando o conceito aprovado (média superior ou igual a 6),
# exame (média maior ou igual a 4 e menor que 6) ou reprovado (média inferior a 4).

nota1 = float(input('Escreva a primeira nota: '))
nota2 = float(input('Escreva a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 6 :
    print('Aprovado')
elif 4 <= media < 6:
    print('Exame')
else:
    print('Reprovado')