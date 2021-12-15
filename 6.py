"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e
uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
repita esse cálculo para novos valores de entrada todas as vezes que desejar.

"""


def converte_horas(horas, minutos):
    lista_horas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    lista_horas2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    if horas in lista_horas1:
        print(f'{horas}:{minutos} AM')
    if horas in lista_horas2:
        indice = lista_horas2.index(horas)
        print(f'{lista_horas1[indice]}:{minutos} PM')


while True:

    print("Conversor de horas, formato 24 horas para 12 horas.\n")
    hora = int(input('Digite a hora: '))
    minuto = int(input('Digite os minutos: \n'))

    converte_horas(hora, minuto)
    print()
    outro = input('Deseja inserir outro horario? [S/N]: ').strip().upper()
    if outro == 'N':
        print("Programa finalizado!")
        break
    if outro not in 'SN':
        print("Opção invalida, programa finalizado.")
        break
