vetor = [1, 2, 3, 4, 5, 6, 7, 8]
print('Escolha dois números de 1 a 8')

x = vetor[int(input('Número: ')) - 1]
y = vetor[int(input('Número: ')) - 1]

print(f'O primeiro valor é {x}')
print(f'O segundo valor é {y}')

soma = x + y
print(f'A soma desses valores é {soma}')
