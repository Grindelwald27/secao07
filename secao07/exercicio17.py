vetor = []
cont = 0
while cont < 10:
    i = vetor.append(int(input('Informe um número: ')))
    cont += 1
for n in vetor:
    if n < 0:
        n = 0
    print(n)
