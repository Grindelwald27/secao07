import numpy as np
matriz = np.zeros([5, 3], int)
transposta = 0
for l in range(5):
    for c in range(3):
        matriz[l][c] = int(input(f'Número [linha {l + 1}, coluna {c + 1}]: '))
print(matriz)
print(matriz.T)
