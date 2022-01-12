import numpy as np
matriz1 = np.zeros([3, 3], int)
matriz2 = np.zeros([1, 3], int)

for l in range(3):
    for c in range(3):
        matriz1[l][c] = int(input(f'Número [{l + 1}, {c + 1}]: '))

matriz2[0][0] = matriz1[0][0] + matriz1[1][0] + matriz1[2][0]
matriz2[0][1] = matriz1[0][1] + matriz1[1][1] + matriz1[2][1]
matriz2[0][2] = matriz1[0][2] + matriz1[1][2] + matriz1[2][2]

print(matriz1)
print()
print(matriz2)
