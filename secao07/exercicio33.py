vetor = []
while len(vetor) < 15:
    num = int(input('Digite um número: '))
    vetor.append(num)

for n in vetor:
    if n == 0:
        vetor.remove(n)

print(vetor)
