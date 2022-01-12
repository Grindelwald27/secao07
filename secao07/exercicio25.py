vetor = []
cont = 0
for n in range(0, 130):
    if n % 7 != 0:
        if (n + 3) % 10 != 0:
            vetor.append(n)
print(vetor)
print(len(vetor))
