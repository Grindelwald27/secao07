notas = []
cont = 1
soma = 0
while cont <= 15:
    nota = notas.append(int(input(f'Informe a nota do {cont}° aluno: ')))
    cont += 1
soma = sum(notas)
media = soma / 15
print(f'A média de toda a turma é {media}')
