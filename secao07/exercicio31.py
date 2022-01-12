vetor = []
vetor2 = []
while len(vetor) < 10:
    num = int(input('Digite um número pro vetor 1: '))
    vetor.append(num)
vetor = set(vetor)
print(vetor)

while len(vetor2) < 10:
    num = int(input('Digite um número pro vetor 2: '))
    vetor2.append(num)
vetor2 = set(vetor2)
print(vetor2)

vetor3 = vetor.union(vetor2)
print(vetor3)
