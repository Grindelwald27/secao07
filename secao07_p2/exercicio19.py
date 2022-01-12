import numpy as np
matriz = np.zeros([5, 4], int)
media_arit = 0
for l in range(5):
    matriz[l][0] = int(input(f'Aluno {l + 1}, informe o número de matrícula: '))

for l in range(5):
    matriz[l][1] = int(input(f'Aluno {l + 1}, informe sua média das provas: '))

for l in range(5):
    matriz[l][2] = int(input(f'Aluno {l + 1}, informe sua média dos trabalhos: '))

matriz[0][3] = matriz[0][1] + matriz[0][2]
matriz[1][3] = matriz[1][1] + matriz[1][2]
matriz[2][3] = matriz[2][1] + matriz[2][2]
matriz[3][3] = matriz[3][1] + matriz[3][2]
matriz[4][3] = matriz[4][1] + matriz[4][2]

print(matriz)
print()

if matriz[0][3] > matriz[1][3] and matriz[2][3] and matriz[3][3] and matriz[4][3]:
    print(f'A matrícula do aluno que obteve a maior nota final é {matriz[0][0]}')

if matriz[1][3] > matriz[0][3] and matriz[2][3] and matriz[3][3] and matriz[4][3]:
    print(f'A matrícula do aluno que obteve a maior nota final é {matriz[1][0]}')

if matriz[2][3] > matriz[1][3] and matriz[0][3] and matriz[3][3] and matriz[4][3]:
    print(f'A matrícula do aluno que obteve a maior nota final é {matriz[2][0]}')

if matriz[3][3] > matriz[1][3] and matriz[2][3] and matriz[0][3] and matriz[4][3]:
    print(f'A matrícula do aluno que obteve a maior nota final é {matriz[3][0]}')

if matriz[4][3] > matriz[1][3] and matriz[2][3] and matriz[3][3] and matriz[0][3]:
    print(f'A matrícula do aluno que obteve a maior nota final é {matriz[4][0]}')

for l in range(5):
    media_arit = (media_arit + matriz[l][3]) / 5
print(f'A média aritmética das notas finais é {media_arit:.2f}')
