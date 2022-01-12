import numpy as np
matriz = np.zeros([3, 3], int)
soma = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input('Número: '))

        soma = matriz[1][0] + matriz[2][0] + matriz[2][1]
print(matriz)
print(f'A soma é {soma}')
