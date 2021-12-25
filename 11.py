"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres
embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação
possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa
baixa, independentemente de como foram digitados.

"""

import random


def embaralha(palavra):
    n = 0
    indices = []
    nova_palavra = []
    while n < len(palavra):
        c = random.randint(0, len(palavra) - 1)
        while c in indices:
            c = random.randint(0, len(palavra) - 1)
        indices.append(c)
        nova_palavra.append(palavra[c])
        n += 1
    result = [''.join(nova_palavra)]
    print(result[0])


a = str(input('Digite uma palavra para embaralhar: '))
embaralha(a)