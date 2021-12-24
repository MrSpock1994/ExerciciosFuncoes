"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

"""

def digitos(numero):
    numero_novo = str(numero)
    print(f'A quantidade de digitos do numero informado é: {len(numero_novo)}')


n = int(input('Digite um numero inteiro: '))
digitos(n)