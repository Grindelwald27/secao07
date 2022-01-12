vetor = []
while len(vetor) < 10:
    num = float(input('Informe um número: '))
    vetor.append(num)

vetor.sort()

print(f'Os valores do vetor são: {vetor}')
