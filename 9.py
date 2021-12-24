"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

"""


def reverso(numero):
    novo_numero = str(numero)
    invertido = list(reversed(novo_numero))
    result = [''.join(invertido)]
    print(result[0])


n = int(input('Digite um numero: '))
reverso(n)
