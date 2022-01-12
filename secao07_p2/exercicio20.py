import numpy as np
matriz = np.zeros([3, 6], int)
soma = 0
matriz1 = np.zeros([3, 6], int)
for l in range(3):
    for c in range(6):
        matriz[l][c] = int(input(f'Número [linha {l + 1}, coluna {c + 1}]: '))
print(matriz)
print()

# Soma das colunas ímpares
for l in range(3):
    for c in range(6):
        if c % 2 != 0:
            soma += matriz[l][c]
print(f'A soma é {soma}')
print()
soma = 0

# Média aritmética
for l in range(3):
    for c in range(6):
        if c == 2:
            soma += matriz[l][c]
        soma = soma
        if c == 4:
            soma += matriz[l][c]
        soma = soma
media = soma / 6
print(f'A média é {media}')
print()

# Substituição
matriz1 = matriz
matriz1[0][5] = matriz[0][0] + matriz[0][1]
matriz1[1][5] = matriz[1][0] + matriz[1][1]
matriz1[2][5] = matriz[2][0] + matriz[2][1]
print(matriz1)
