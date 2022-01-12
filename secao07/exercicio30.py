vetor = []
vetor2 = []

while len(vetor) < 10:
    num = int(input('Digite um número para o conjunto 1: '))
    vetor.append(num)
vetor = set(vetor)

while len(vetor2) < 10:
    num = int(input('Digite um número para o conjunto 2: '))
    vetor2.append(num)
vetor2 = set(vetor2)

vetor3 = list(vetor.intersection(vetor2))
print(vetor)
print(vetor2)
print(f'Os números presentes em ambos os vetores são {vetor3}')
