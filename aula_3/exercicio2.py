#2. Escreva um programa que leia três números e que
# imprima o maior e o menor.

num1 = int(input('Escreva um numero: '))
num2 = int(input('Escreva um numero: '))
num3 = int(input('Escreva um numero: '))
if num1 > num2 > num3:
    print(num1)
else:
    if num1 > num3 > num2:
        print(num1)
    else:
        if num2 > num1 > num3:
            print(num2)
        else:
            if num2 > num3 > num1:
                print(num2)
            else:
                if num3 > num2 > num1:
                    print(num3)
                else:
                    if num3 > num1 > num2:
                        print(num3)