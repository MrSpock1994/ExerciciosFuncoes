"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha

"""


def imprimir_num(n):
    x = 1
    while x <= n:
        print(f'{str(x) * x}')
        x += 1


num = int(input('Digite um numero: '))
imprimir_num(num)
