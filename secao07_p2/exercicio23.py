import numpy as np
matriz_a = np.zeros([3, 3], int)
matriz_b = np.zeros([3, 3], int)

for l in range(3):
    for c in range(3):
        matriz_a[l][c] = int(input(f'número [{l + 1}, {c + 1}]: '))

matriz_b[0][0] = matriz_a[0][0] ** 2
matriz_b[0][1] = matriz_a[0][1] ** 2
matriz_b[0][2] = matriz_a[0][2] ** 2
matriz_b[1][0] = matriz_a[1][0] ** 2
matriz_b[1][1] = matriz_a[1][1] ** 2
matriz_b[1][2] = matriz_a[1][2] ** 2
matriz_b[2][0] = matriz_a[2][0] ** 2
matriz_b[2][1] = matriz_a[2][1] ** 2
matriz_b[2][2] = matriz_a[2][2] ** 2

print(matriz_a)
print()
print(matriz_b)