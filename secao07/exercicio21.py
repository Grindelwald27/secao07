a = []
b = []
c = []
cont = 1
while cont <= 10:
    a.append(int(input(f'Informe o valor {cont}/10 para A: ')))
    cont += 1
print(a)
cont = 1
while cont <= 10:
    b.append(int(input(f'Informe o valor {cont}/10 para B: ')))
    cont += 1
print(b)

for i in range(10):
    num = a[i] - b[i]
    c.append(num)
print(c)
