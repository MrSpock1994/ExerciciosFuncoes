"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.

"""


def somaImposto(taxa, custo):
    novo_valor = custo + (taxa * custo)
    print(novo_valor)


custo = float(input('Digite o preço do produto: '))
taxa = float(input('Digite a taxa de imposto em %: '))
taxa_certa = taxa / 100

somaImposto(taxa_certa, custo)