from collections import Counter
vetor = [1, 2, 2, 4, 5, 6, 6, 8, 9, 10]
rep = Counter(vetor)
for n in rep:
    if rep[n] > 1:
        print(f'O número {n} foi informado {rep[n]} vezes')
