"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato
D de mesPorExtenso de AAAA.

"""


def data(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    print(f'{dia} de {meses[mes-1]} de {ano}')


datas = str(input('Digite a data no formato DD/MM/AAAA: '))
data(int(datas[0:2]), int(datas[3:5]), int(datas[6:]))