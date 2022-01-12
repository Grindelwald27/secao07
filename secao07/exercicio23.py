v1 = []
v2 = []
cont = 1
soma = 0
while cont <= 5:
    v1.append(int(input(f'Informe o {cont}° número para o primeiro vetor: ')))
    cont += 1

cont = 1
while cont <= 5:
    v2.append(int(input(f'Informe o {cont}° número para o segundo vetor: ')))
    cont += 1

for i in range(0, 5):
    p_escalar = v1[i] * v2[i]
    soma = soma + p_escalar
print(v1)
print(v2)
print(soma)
