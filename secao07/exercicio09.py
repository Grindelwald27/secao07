vetor = []
cont = 0
while cont < 6:
    n = int(input('Informe um número par: '))
    while n % 2 != 0:
        n = int(input('Informe um número par: '))
    else:
        vetor.append(n)
    cont += 1
print(vetor[::-1])
