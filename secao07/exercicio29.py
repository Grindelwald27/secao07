vetor = []
par = []
impar = []
while len(vetor) < 6:
    num = int(input('Digite um número: '))
    vetor.append(num)
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)
print(vetor)
print(f'Os números pares são {par}')
print(f'A soma dos números pares é igual a {sum(par)}')
print(f'Os números ímpares são {impar}')
print(f'A quantidade de números ímpares é igual a {len(impar)}')
