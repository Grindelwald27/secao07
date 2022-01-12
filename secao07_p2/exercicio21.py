import numpy as np
matriz1 = np.zeros([2, 2], int)
matriz2 = np.zeros([2, 2], int)
matriz3 = np.zeros([2, 2], int)

for l in range(2):
    for c in range(2):
        matriz1[l][c] = int(input(f'Matriz 1 - número [{l + 1}, {c + 1}]: '))

for l in range(2):
    for c in range(2):
        matriz2[l][c] = int(input(f'Matriz 2 - número [{l + 1}, {c + 1}]: '))

print(matriz1)
print()
print(matriz2)
print()
print('Escolha uma das opções abaixo:')
print('1 - somar as duas matrizes')
print('2 - subtrair a primeira matriz da segunda')
print('3 - adicionar uma constantes ás duas matrizes')
opcao = int(input('Opção: '))
while opcao > 3 or opcao < 1:
    opcao = int(input('Opção: '))

print()
if opcao == 1:
    matriz3[0][0] = matriz1[0][0] + matriz2[0][0]
    matriz3[0][1] = matriz1[0][1] + matriz2[0][1]
    matriz3[1][0] = matriz1[1][0] + matriz2[1][0]
    matriz3[1][1] = matriz1[1][1] + matriz2[1][1]
    print('Resultado da escolha 1:')
    print(matriz3)

if opcao == 2:
    matriz3[0][0] = matriz1[0][0] - matriz2[0][0]
    matriz3[0][1] = matriz1[0][1] - matriz2[0][1]
    matriz3[1][0] = matriz1[1][0] - matriz2[1][0]
    matriz3[1][1] = matriz1[1][1] - matriz2[1][1]
    print('Resultado da escolha 2:')
    print(matriz3)

if opcao == 3:
    matriz1[0][1] = 50
    matriz2[0][1] = 50
    print('Resultado da escolha 3:')
    print(matriz1)
    print()
    print(matriz2)
