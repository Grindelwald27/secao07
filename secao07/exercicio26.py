vetor = []
cont = 1
while cont <= 10:
    vetor.append(int(input(f'Informe o número {cont}/10: ')))
    cont += 1
print(vetor)
media = sum(vetor) / len(vetor)
dp = 0.5 ** (sum(vetor) * ((vetor[0] - media) ** 2) / len(vetor))
print(f'O desvio padrão é {dp}')
