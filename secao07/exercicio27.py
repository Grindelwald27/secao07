vetor = []
cont = 0
i = 1
while len(vetor) < 10:
    num = int(input('Informe um número: '))
    vetor.append(num)
    cont += 1
for p, y in enumerate(vetor):
    while i <= y:
        if y % i == 0:
            cont += 1
            i += 1
        elif y % i != 0:
            i += 1
    if cont == 2:
        print(f'[{p}] = {y}')
        cont = 0
        i = 1
    if cont != 2:
        cont = 0
        i = 1
