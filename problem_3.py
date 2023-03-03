# -*- coding: utf-8 -*-

# WU LUZIEN
# UAG00098
# Problem Set 2 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Digite um número de ponto flutuante.
Exemplo 1:
Digite o valor: 25.01
Exemplo 2:
Digite o valor: 25.00
Exemplo 3:
Digite o valor: -25.02

Processes:
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0, 25], (25, 50], (50, 75], (75, 100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem "Fora de intervalo.".

O símbolo (representa "maior que". Por exemplo:
[0, 25]  indica valores entre 0 e 25.0000, inclusive eles.
(25, 50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Output(s):
A saída deve ser uma mensagem conforme exemplo abaixo.
Exemplo 1:
Intervalo (25, 50]
Exemplo 2:
Intervalo [0, 25]
Exemplo 3:
Fora de intervalo.
"""


def main():

    valor = float(input("Digite o valor: "))

    if valor >= 0 and valor <= 25:
        print("Intervalo [0, 25]")
    elif valor > 25 and valor <= 50:
        print("Intervalo (25, 50]")
    elif valor > 50 and valor <= 75:
        print("Intervalo (50, 75]")
    elif valor > 75 and valor <= 100:
        print("Intervalo (75, 100]")
    else:
        print("Fora de intervalo.")
if __name__ == '__main__':
    main()
