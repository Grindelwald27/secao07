import numpy as np
matriz = np.zeros([3, 3], int)
soma = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Número [linha {l + 1}, coluna {c + 1}]: '))

        soma = matriz[0][2] + matriz[1][1] + matriz[2][0]
print(matriz)
print(f'A soma é igual a {soma}')
