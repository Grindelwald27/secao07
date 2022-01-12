from random import randint

vetor = []
vetor2 = []
cont = 0
i = 0
impar = 0
while cont < 10:
    vetor.append(randint(0, 50))
    cont += 1
print(vetor)
cont = 0
for n in vetor:
    if n % 2 != 0:
        vetor2.append(n)
        impar += 1
print(vetor2)

while cont < len(vetor) / 2:
    print(vetor[i], vetor[i + 1])
    cont += 1
    i += 1
cont = 0
i = 0
while cont < impar / 2:
    print(vetor2[i], vetor2[i + 1])
    cont += 1
    i += 1
