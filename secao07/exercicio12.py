vetor = []
cont = 1
quant = 5
while cont <= 5:
    vetor.append(int(input('Informe um número: ')))
    cont += 1
media = sum(vetor) / quant
print(vetor)
print(f'O maior valor é {max(vetor)}')
print(f'O menor valor é {min(vetor)}')
print(f'A média dos valores é {media}')
