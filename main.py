import numpy as np
from config import pega_matriz, determinante


if __name__ == '__main__':

    matriz_A = pega_matriz()
    print()
    print("Matriz A:")
    for i in matriz_A:
        print(i)

    print()
    matriz_A = np.array(matriz_A)

    print("Det(A) = {}".format(determinante(matriz_A)))
