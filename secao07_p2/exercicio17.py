import numpy as np
matriz = np.zeros([10, 3], int)

pior1 = 0
pior2 = 0
pior3 = 0

for l in range(10):
    for c in range(3):
        matriz[l][c] = int(input(f'Informe a nota da {c + 1}º prova do aluno {l + 1}: '))

if matriz[0][0] < matriz[0][1] and matriz[0][2]:
    pior1 += 1
if matriz[0][1] < matriz[0][0] and matriz[0][2]:
    pior2 += 1
if matriz[0][2] < matriz[0][0] and matriz[0][1]:
    pior3 += 1

if matriz[1][0] < matriz[1][1] and matriz[1][2]:
    pior1 += 1
if matriz[1][1] < matriz[1][0] and matriz[1][2]:
    pior2 += 1
if matriz[1][2] < matriz[1][0] and matriz[1][1]:
    pior3 += 1

if matriz[2][0] < matriz[2][1] and matriz[2][2]:
    pior1 += 1
if matriz[2][1] < matriz[2][0] and matriz[2][2]:
    pior2 += 1
if matriz[2][2] < matriz[2][0] and matriz[2][1]:
    pior3 += 1

if matriz[3][0] < matriz[3][1] and matriz[3][2]:
    pior1 += 1
if matriz[3][1] < matriz[3][0] and matriz[3][2]:
    pior2 += 1
if matriz[3][2] < matriz[3][0] and matriz[3][1]:
    pior3 += 1

if matriz[4][0] < matriz[4][1] and matriz[4][2]:
    pior1 += 1
if matriz[4][1] < matriz[4][0] and matriz[4][2]:
    pior2 += 1
if matriz[4][2] < matriz[4][0] and matriz[4][1]:
    pior3 += 1

if matriz[5][0] < matriz[5][1] and matriz[5][2]:
    pior1 += 1
if matriz[5][1] < matriz[5][0] and matriz[5][2]:
    pior2 += 1
if matriz[5][2] < matriz[5][0] and matriz[5][1]:
    pior3 += 1

if matriz[6][0] < matriz[6][1] and matriz[6][2]:
    pior1 += 1
if matriz[6][1] < matriz[6][0] and matriz[6][2]:
    pior2 += 1
if matriz[6][2] < matriz[6][0] and matriz[6][1]:
    pior3 += 1

if matriz[7][0] < matriz[7][1] and matriz[7][2]:
    pior1 += 1
if matriz[7][1] < matriz[7][0] and matriz[7][2]:
    pior2 += 1
if matriz[7][2] < matriz[7][0] and matriz[7][1]:
    pior3 += 1

if matriz[8][0] < matriz[8][1] and matriz[8][2]:
    pior1 += 1
if matriz[8][1] < matriz[8][0] and matriz[8][2]:
    pior2 += 1
if matriz[8][2] < matriz[8][0] and matriz[8][1]:
    pior3 += 1

if matriz[9][0] < matriz[9][1] and matriz[9][2]:
    pior1 += 1
if matriz[9][1] < matriz[9][0] and matriz[9][2]:
    pior2 += 1
if matriz[9][2] < matriz[9][0] and matriz[9][1]:
    pior3 += 1

print(matriz)
print()
print(f'O número de alunos cuja pior nota foi na prova 1 é {pior1}')
print(f'O número de alunos cuja pior nota foi na prova 2 é {pior2}')
print(f'O número de alunos cuja pior nota foi na prova 3 é {pior3}')
print()
if pior1 + pior2 + pior3 != 10:
    print('Tem algo errado!')
else:
    print('Você arrasou!')
