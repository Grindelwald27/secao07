vetor = []
while len(vetor) < 10:
    num = int(input('Digite um número: '))
    if num in vetor:
        print('Erro! Número repetido')
    else:
        vetor.append(num)
print(vetor)
