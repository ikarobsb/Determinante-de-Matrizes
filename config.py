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

exemplo_matriz6 = '\n\n' \
                  '(a11, a12, a13, a14, a15, a16)\n' \
                  '(a21, a22, a23, a24, a25, a26)\n' \
                  '(a31, a32, a33, a34, a35, a36)\n' \
                  '(a41, a42, a43, a44, a45, a46)\n' \
                  '(a51, a52, a53, a54, a55, a56)\n' \
                  '(a61, a62, a63, a64, a65, a66)\n'

lista_matrizes = (exemplo_matriz2, exemplo_matriz3, exemplo_matriz4, exemplo_matriz5, exemplo_matriz6)

def ex_matriz(n):
    n -= 2
    print("Considere que a matriz terá esse formato: {}".format(lista_matrizes[n]))


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
            tamanho_da_matriz = int(input("Qual o tamanho da matriz nxn ? (entre 2 até 6) "))

            if tamanho_da_matriz <= 1 or tamanho_da_matriz >= 7:
                tamanho_da_matriz = 2
                print("Devido ao valor digitado ser inválido, a matriz será considerada {}x{}".format(tamanho_da_matriz,tamanho_da_matriz))

            ex_matriz(tamanho_da_matriz)

            return tamanho_da_matriz
        except ValueError:
            print("Valor digitado inválido")


def pega_matriz():
    tamanho_matriz = define_matriz()
    while True:
        try:

            nn = tamanho_matriz ** 2

            matriz = []
            temp_list = []

            volta = 0
            linha = 1
            coluna = 1

            for i in range(nn+1):
                
                if volta == tamanho_matriz:
                    volta = 0
                    linha += 1
                    coluna = 1

                    matriz.append(temp_list)
                    temp_list = []

                if i < nn:
                    getvalue = int(input("Digite o valor de a{}{}: ".format(linha, coluna)))
                    temp_list.append(getvalue)

                coluna += 1
                volta += 1 

            return matriz

        except ValueError:
            print("Valor digitado inválido")
