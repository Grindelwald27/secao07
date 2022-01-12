import numpy as np
matriz = np.zeros([3, 3], int)
soma = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input('Número: '))

        soma = matriz[0][1] + matriz[0][2] + matriz[1][2]

print(matriz)
print(f'A soma é {soma}')
