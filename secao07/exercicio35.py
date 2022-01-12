a = input('Primeiro número: ')
b = input('Segundo número: ')

A, B = list(a), list(b)  # criando as listas para guardar os algarismos

A.reverse()  # invertendo-as por facilidade na hora do loop
B.reverse()

for i in range(len(A)):  # transformado cada algarismo em int
    A[i] = int(A[i])

for j in range(len(B)):
    B[j] = int(B[j])

C = []  # vetor para guardar a soma
soma = 0  # variável para guardar o valor da soma de cada índice
check_soma = False  # variável para informar se a soma ultrapassou de 10

for i in range(min(len(A), len(B))):  # loop para construir o vetor C a partir do vetor com menos
    soma = A[i] + B[i]  # algarismos

    if check_soma:  # se a soma anterior tiver ultrapassado 10, será contado aqui
        soma += 1  # para i=0, não há soma anterior; por isso check_soma = False

    check_soma = False  # resetando a informação sobre a soma anterior para a soma atual

    if soma >= 10:  # atualizando a informação sobre a soma
        check_soma = True

    if check_soma:  # aqui ela será compensada caso tenha ultrapassado 10
        soma -= 10

    C.append(soma)

if len(A) > len(B):  # compensando os termos restantes, caso haja
    for j in range(len(C), len(A)):  # a mesma lógica se aplica
        soma = A[j]

        if check_soma:
            soma += 1

        check_soma = False

        if soma >= 10:
            check_soma = True

        if check_soma:
            soma -= 10

        C.append(soma)

elif len(B) > len(A):
    for j in range(len(C), len(B)):
        soma = B[j]

        if check_soma:
            soma += 1

        check_soma = False

        if soma >= 10:
            check_soma = True

        if check_soma:
            soma -= 10

        C.append(soma)

else:
    pass

if check_soma:  # se os vetores possuírem mesmo tamanho e a soma dos últimos
    C.append(1)  # elementos for maior que 10, basta adicionar 1 ao último
    # elemento de C (perceba que len(C) > len(A) e len(B) agora)
C.reverse()  # invertendo C para ser exibido na ordem correta

print(C)
