vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult = []
x = int(input('Informe um valor: '))
for n in vetor:
    if x % n == 0:
        mult.append(n)
print(f'Os múltiplos de {x} de 1 a 10 são: {mult}')
