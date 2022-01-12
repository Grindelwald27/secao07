vetor = []
cont = 1
while cont <= 10:
    vetor.append(int(input(f'Informe o número {cont}°/10: ')))
    cont += 1
print(vetor)
print(f' O maior valor é {max(vetor)}')
print(f' O menor valor é {min(vetor)}')
