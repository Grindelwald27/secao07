v = []
v1 = []
v2 = []
while len(v) < 10:
    num = int(input('Digite um número: '))
    v.append(num)
    if num % 2 == 0:
        v2.append(num)
    else:
        v1.append(num)
print('Os índices e seus respectivos valores ímpares são:')
for indice, numero in enumerate(v1):
    print(f'[{indice}] = {numero}')
print('Os índices e seus respectivos valores pares são:')
for indice, numero in enumerate(v2):
    print(f'[{indice}] = {numero}')
