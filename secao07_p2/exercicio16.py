import numpy as np
matriz = np.zeros([3, 10], str)
mat1 = int(input('Informe sua matrícula: '))
mat2 = int(input('Informe sua matrícula: '))
mat3 = int(input('Informe sua matrícula: '))
gabarito = ['a', 'c', 'b', 'd', 'a', 'a', 'c', 'b', 'd', 'b']
nota1 = 0
nota2 = 0
nota3 = 0
apr = 0
resp1 = []
resp2 = []
resp3 = []
for l in range(3):
    for c in range(10):
        matriz[l][c] = str(input(f'Aluno {l + 1}, questão {c + 1}, resposta: '))

for c in range(10):
    if matriz[0][c]:
        resp1.append(matriz[0][c])

    if matriz[1][c]:
        resp2.append(matriz[1][c])

    if matriz[2][c]:
        resp3.append(matriz[2][c])

for c in range(10):
    if matriz[0][c] == gabarito[c]:
        nota1 += 1

    if matriz[1][c] == gabarito[c]:
        nota2 += 1

    if matriz[2][c] == gabarito[c]:
        nota3 += 1

if nota1 > 7:
    apr += 1

if nota2 > 7:
    apr += 1

if nota3 > 7:
    apr += 1
perc_apr = (apr * 100) / 3

print(matriz)
print()
print(gabarito)
print()
print('Aluno 1:')
print(f'  Matrícula: {mat1}')
print(f'  Respostas: {resp1}')
print(f'  Nota: {nota1}')
print()
print('Aluno 2: ')
print(f'  Matrícula: {mat2}')
print(f'  Resposta: {resp2}')
print(f'  Nota: {nota2}')
print()
print('Aluno 3:')
print(f'  Matrícula: {mat3}')
print(f'  Resposta: {resp3}')
print(f'  Nota: {nota3}')
print(f'A taxa de aprovados é de {perc_apr:.2f}%')
