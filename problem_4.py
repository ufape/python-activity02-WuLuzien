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
    numeros_pares = 0

    for i in range(6):
        valor = int(input(f"Digite o valor {i+1}/6: "))
    
        if valor % 2 == 0:
            numeros_pares += 1

    print(f"Você digitou {numeros_pares} valores pares.")
if __name__ == '__main__':
    main()
