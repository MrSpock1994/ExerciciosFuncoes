"""

Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def imprimir_num(n):
    x = 1
    numeros = []
    while x <= n:
        numeros.append(x)
        print(numeros)
        x += 1


num = int(input('Digite um numero: '))
imprimir_num(num)
