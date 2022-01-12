matriz1 = []
matriz2 = []
matriz3 = []
l1 = []
l2 = []
l3 = []
l4 = []
maior1 = []
maior2 = []
maior3 = []

for c in range(4):
    l1.append(int(input(f'Digite o número [1, {c + 1}]: ')))
matriz1.append(l1)

for c in range(4):
    l2.append(int(input(f'Digite o número [2, {c + 1}]: ')))
matriz1.append(l2)

for c in range(4):
    l3.append(int(input(f'Digite o número [3, {c + 1}]: ')))
matriz1.append(l3)

for c in range(4):
    l4.append(int(input(f'Digite o número [4, {c + 1}]: ')))
matriz1.append(l4)

l1 = []
l2 = []
l3 = []
l4 = []

for c in range(4):
    l1.append(int(input(f'Digite o número [1, {c + 1}]: ')))
matriz2.append(l1)

for c in range(4):
    l2.append(int(input(f'Digite o número [2, {c + 1}]: ')))
matriz2.append(l2)

for c in range(4):
    l3.append(int(input(f'Digite o número [3, {c + 1}]: ')))
matriz2.append(l3)

for c in range(4):
    l4.append(int(input(f'Digite o número [4, {c + 1}]: ')))
matriz2.append(l4)

l1 = []
l2 = []
l3 = []
l4 = []

print('Matriz 1:')
for n in matriz1:
    print(n)

print('Matriz 2:')
for n in matriz2:
    print(n)

for linha, valor_linha in enumerate(matriz1):
    for coluna, valor_coluna in enumerate(matriz1[linha]):
        maior1.append(valor_coluna)

for linha, valor_linha in enumerate(matriz2):
    for coluna, valor_coluna in enumerate(matriz2[linha]):
        maior2.append(valor_coluna)

for i in range(16):
    if maior1[i] > maior2[i]:
        maior3.append(maior1[i])
    else:
        maior3.append(maior2[i])

print('Matriz3:')
for ind, num in enumerate(maior3):
    if ind <= 3:
        l1.append(num)

    if 3 < ind <= 7:
        l2.append(num)

    if 7 < ind <= 11:
        l3.append(num)

    if 11 < ind <= 15:
        l4.append(num)
matriz3.append(l1)
matriz3.append(l2)
matriz3.append(l3)
matriz3.append(l4)

for n in matriz3:
    print(n)
