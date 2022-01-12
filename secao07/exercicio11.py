vetor = [-5, 2, 10, -8, -7, 15, -45, 45, -3, 4]
pos = []
neg = []
for n in vetor:
    if n > 0:
        pos.append(n)
    else:
        neg.append(n)
print(f'A quantidade de números negativos é {len(neg)}')
print(f'A soma dos números positivos é {sum(pos)}')
