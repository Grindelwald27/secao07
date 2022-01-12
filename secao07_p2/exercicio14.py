from random import randint
import numpy as np
matriz = np.zeros([5, 5], int)
for l in range(5):
    for c in range(5):
        matriz[l][c] = randint(0, 99)
print(matriz)
