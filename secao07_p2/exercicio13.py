import numpy as np
from random import randint
matriz = np.zeros([4, 4], int)
for l in range(4):
    for c in range(4):
        matriz[l][c] = randint(1, 20)
print(matriz)
matriz_t = matriz
matriz_t[0][1] = 0
matriz_t[0][2] = 0
matriz_t[0][3] = 0
matriz_t[1][2] = 0
matriz_t[1][3] = 0
matriz_t[2][3] = 0
print()
print(matriz_t)
