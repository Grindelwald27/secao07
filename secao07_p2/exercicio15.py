import numpy as np
matriz = np.zeros([5, 10], str)
gabarito = ['a', 'c', 'b', 'd', 'a', 'a', 'c', 'b', 'd', 'b']
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0
for l in range(5):
    for c in range(10):
        matriz[l][c] = str(input(f'Aluno {l + 1}, questão {c + 1} = resposta: '))

for c in range(10):
    if matriz[0][c] == gabarito[c]:
        nota1 += 1

    if matriz[1][c] == gabarito[c]:
        nota2 += 1

    if matriz[2][c] == gabarito[c]:
        nota3 += 1

    if matriz[3][c] == gabarito[c]:
        nota4 += 1

    if matriz[4][c] == gabarito[c]:
        nota5 += 1

print(matriz)
print()
print(gabarito)
print()
print(f'A nota do aluno 1 é: {nota1}')
print(f'A nota do aluno 2 é: {nota2}')
print(f'A nota do aluno 3 é: {nota3}')
print(f'A nota do aluno 4 é: {nota4}')
print(f'A nota do aluno 5 é: {nota5}')
