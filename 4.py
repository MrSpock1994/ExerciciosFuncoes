"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

"""


def sinal(a):
    if a > 0:
        print('P')
    else:
        print('N')


n = float(input('Digite um numero: '))
sinal(n)