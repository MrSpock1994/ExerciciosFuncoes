"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""


def valorpagamento(valor, dias):
    global novo_valor
    if dias == 0:
        novo_valor = valor
        #print(novo_valor)
    elif dias >= 1:
        novo_valor = valor + (valor * (3/100)) + ((valor * (1/1000)) * dias)
        #print(novo_valor)



prestacoes_ajust = []
while True:
    a = float(input('Digite o valor da prestação a ser paga: '))
    if a == 0:
        break
    b = int(input('Digite a quantidade de dias em atraso: '))
    valorpagamento(a, b)
    prestacoes_ajust.append(novo_valor)



print()
print('**** RELATORIO DO DIA ****')
print()
print(f'O valor total de prestações pagas hoje foi de: {sum(prestacoes_ajust)}\n')
print(f'A quantidade de prestações pagas hoje foi de: {len(prestacoes_ajust)}')