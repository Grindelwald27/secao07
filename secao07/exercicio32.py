x = []
y = []
while len(x) < 5:
    num = int(input('Digite um número para x: '))
    x.append(num)
x = set(x)

while len(y) < 5:
    num = int(input('Digite um número para y: '))
    y.append(num)
y = set(y)

print(x)
print(y)

for indice, numero in enumerate(x):
    for ind, num in enumerate(y):
        if indice == ind:
            soma = numero + num
            print(f'A soma dos elementos nos índices {indice} é {soma}')

print(x)
print(y)
for indice, numero in enumerate(x):
    for ind, num in enumerate(y):
        if indice == ind:
            mult = numero * num
            print(f'A multiplicação dos elementos nos índices {indice} é {mult}')

print(x)
print(y)
so_x = x.difference(y)
print(f'Os números que estão em X e que não estão em Y são: {so_x}')

print(x)
print(y)
ambos = x.intersection(y)
print(f'Os números que aparecem tanto em X quanto em Y são: {ambos}')

print(x)
print(y)
todos = x.union(y)
print(f'Todos os números são: {todos}')
