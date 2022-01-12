matriz = []
m1 = []
cont = 1
indice = 0
maior = 0
for i in range(4):
    for j in range(4):
        num = int(input('Informe um número: '))
        m1.append(num)
        if num > maior:
            maior = num
    matriz.append(m1)
    m1 = []
print(f'O maior valor é {maior}')

for i in matriz:
    if maior in i:
        indice = i.index(maior)
        break
    cont += 1

for i in matriz:
    print(i)

print(f'O maior valor está na linha {cont} e coluna {indice + 1}')
