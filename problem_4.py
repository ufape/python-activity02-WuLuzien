# -*- coding: utf-8 -*-

# Wu Luzien
# UAG00098
# Problem Set 2 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Digite 6 valores inteiros quaisquer.
Exemplo:
Digite o valor 1/6: 2
Digite o valor 2/6: 3
Digite o valor 3/6: 4
Digite o valor 4/6: 5
Digite o valor 5/6: 6
Digite o valor 6/6: 7

Processes:
Faça um programa que leia 6 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Output(s):
Exemplo:
Você digitou 3 valores pares.
"""


def main():
    numero_par = 0

    for num in range(6):
       numero = int(input('Digite um número:'))
       if (numero % 2 ==0):
          numero_par += 1
          print(f'Detectamos {numero_par} Valores Pares')

if __name__ == '__main__':
    main()
