lista1 = []
lista2 = []
while len(lista1) < 6:
    num = float(input('Informe um número: '))
    lista1.append(num)
lista1.sort()

while len(lista2) < 5:
    num = float(input('Informe um número: '))
    lista2.append(num)
lista2.sort()
lista2.reverse()

vetor = lista1 + lista2

print(vetor)
