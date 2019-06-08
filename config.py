#!/usr/bin/python


# -*- coding: windows-1252 -*-
# Eduardo Ribeiro Leal <eduardoleal.contact@gmail.com>
# calculo de determinantes

import math
import numpy as np

# Só mecher aqui se souber o que estiver fazendo

exemplo_matriz2 = '\n\n' \
                  '(a11, a12)\n' \
                  '(a21, a22)\n'

exemplo_matriz3 = '\n\n' \
                  '(a11, a12, a13)\n' \
                  '(a21, a22, a23)\n' \
                  '(a31, a32, a33)\n'

exemplo_matriz4 = '\n\n' \
                  '(a11, a12, a13, a14)\n' \
                  '(a21, a22, a23, a24)\n' \
                  '(a31, a32, a33, a34)\n' \
                  '(a41, a42, a43, a44)\n'

exemplo_matriz5 = '\n\n' \
                  '(a11, a12, a13, a14, a15)\n' \
                  '(a21, a22, a23, a24, a25)\n' \
                  '(a31, a32, a33, a34, a35)\n' \
                  '(a41, a42, a43, a44, a45)\n' \
                  '(a51, a52, a53, a54, a55)\n'


def ex_matriz(n):
    if n == 2:
        print("Considere que a matriz terá esse formato: {}".format(exemplo_matriz2))
    elif n == 3:
        print("Considere que a matriz terá esse formato: {}".format(exemplo_matriz3))
    elif n == 4:
        print("Considere que a matriz terá esse formato: {}".format(exemplo_matriz4))
    elif n == 5:
        print("Considere que a matriz terá esse formato: {}".format(exemplo_matriz5))


def determinante(matriz_a):
    n = np.shape(matriz_a)[0]
    if n == 2:
        det = matriz_a[0, 0] * matriz_a[1, 1] - matriz_a[0, 1] * matriz_a[1, 0]
    else:
        det = 0
        for i in range(n):
            novamatriz = matriz_a[1:, :]
            novamatriz = np.delete(novamatriz, i, axis=1)
            det += math.pow(-1, 1 + i + 1) * matriz_a[0, i] * (determinante(novamatriz))

    return det


def define_matriz():
    while True:
        try:
            tamanho_da_matriz = int(input("Qual o tamanho da matriz nxn ? (entre 2 até 5) "))
            if tamanho_da_matriz <= 1:
                tamanho_da_matriz = 2
                print("Devido ao valor digitado ser inválido\n"
                      "A matriz será considerada {}".format(tamanho_da_matriz))
                return tamanho_da_matriz
            elif tamanho_da_matriz >= 6:
                tamanho_da_matriz = 5
                print("Devido ao valor digitado ser inválido\n"
                      "A matriz será considerada {}".format(tamanho_da_matriz))
                return tamanho_da_matriz
            else:
                return tamanho_da_matriz
        except ValueError:
            print("Valor digitado inválido")


def pega_matriz():
    matriz = define_matriz()
    while True:
        try:
            if matriz == 2:
                ex_matriz(matriz)
                a11 = int(input("Digite valor de a11: "))
                a12 = int(input("Digite valor de a12: "))
                a21 = int(input("Digite valor de a21: "))
                a22 = int(input("Digite valor de a22: "))

                return [(a11, a12),
                        (a21, a22)]

            elif matriz == 3:
                ex_matriz(matriz)
                a11 = int(input("Digite valor de a11: "))
                a12 = int(input("Digite valor de a12: "))
                a13 = int(input("Digite valor de a13: "))
                a21 = int(input("Digite valor de a21: "))
                a22 = int(input("Digite valor de a22: "))
                a23 = int(input("Digite valor de a23: "))
                a31 = int(input("Digite valor de a31: "))
                a32 = int(input("Digite valor de a32: "))
                a33 = int(input("Digite valor de a33: "))

                return [(a11, a12, a13),
                        (a21, a22, a23),
                        (a31, a32, a33)]

            elif matriz == 4:
                ex_matriz(matriz)
                a11 = int(input("Digite valor de a11: "))
                a12 = int(input("Digite valor de a12: "))
                a13 = int(input("Digite valor de a13: "))
                a14 = int(input("Digite valor de a14: "))
                a21 = int(input("Digite valor de a21: "))
                a22 = int(input("Digite valor de a22: "))
                a23 = int(input("Digite valor de a23: "))
                a24 = int(input("Digite valor de a24: "))
                a31 = int(input("Digite valor de a31: "))
                a32 = int(input("Digite valor de a32: "))
                a33 = int(input("Digite valor de a33: "))
                a34 = int(input("Digite valor de a34: "))
                a41 = int(input("Digite valor de a41: "))
                a42 = int(input("Digite valor de a42: "))
                a43 = int(input("Digite valor de a43: "))
                a44 = int(input("Digite valor de a44: "))

                return [(a11, a12, a13, a14),
                        (a21, a22, a23, a24),
                        (a31, a32, a33, a34),
                        (a41, a42, a43, a44)]

            elif matriz == 5:
                ex_matriz(matriz)
                a11 = int(input("Digite valor de a11: "))
                a12 = int(input("Digite valor de a12: "))
                a13 = int(input("Digite valor de a13: "))
                a14 = int(input("Digite valor de a14: "))
                a15 = int(input("Digite valor de a15: "))
                a21 = int(input("Digite valor de a21: "))
                a22 = int(input("Digite valor de a22: "))
                a23 = int(input("Digite valor de a23: "))
                a24 = int(input("Digite valor de a24: "))
                a25 = int(input("Digite valor de a25: "))
                a31 = int(input("Digite valor de a31: "))
                a32 = int(input("Digite valor de a32: "))
                a33 = int(input("Digite valor de a33: "))
                a34 = int(input("Digite valor de a34: "))
                a35 = int(input("Digite valor de a34: "))
                a41 = int(input("Digite valor de a41: "))
                a42 = int(input("Digite valor de a42: "))
                a43 = int(input("Digite valor de a43: "))
                a44 = int(input("Digite valor de a44: "))
                a45 = int(input("Digite valor de a45: "))
                a51 = int(input("Digite valor de a51: "))
                a52 = int(input("Digite valor de a52: "))
                a53 = int(input("Digite valor de a53: "))
                a54 = int(input("Digite valor de a54: "))
                a55 = int(input("Digite valor de a55: "))

                return [(a11, a12, a13, a14, a15),
                        (a21, a22, a23, a24, a25),
                        (a31, a32, a33, a34, a35),
                        (a41, a42, a43, a44, a45),
                        (a51, a52, a53, a54, a55)]

        except ValueError:
            print("Valor digitado inválido")
