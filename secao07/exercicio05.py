vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = []

for n in vetor:
    if n % 2 == 0:
        vetor2.append(n)
print(vetor2)
print(f'A quantidade de numeros pares é {len(vetor2)}')
