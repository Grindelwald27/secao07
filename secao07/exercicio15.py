from collections import Counter
vetor = []
repetidos = []
n_rep = []
cont = 0
while cont < 20:
    vetor.append(int(input('Informe um número: ')))
    cont += 1
rep = Counter(vetor)
for n in rep:
    if rep[n] > 1:
        repetidos.append(n)
    else:
        n_rep.append(n)
print(n_rep)
