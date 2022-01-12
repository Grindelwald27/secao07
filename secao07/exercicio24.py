n_aluno = []
alt_aluno = []
cont = 1
while cont <= 10:
    n_aluno.append(int(input('Informe seu número: ')))
    alt_aluno.append(float(input('Informe sua altura: ')))
    cont += 1

baixo = alt_aluno.index(min(alt_aluno))
alto = alt_aluno.index(max(alt_aluno))
num_baixo = n_aluno[baixo]
num_alto = n_aluno[alto]

print(n_aluno)
print(alt_aluno)

print(f'O número do aluno mais baixo é {num_baixo} e a altura é {min(alt_aluno)}m')
print(f'O número do aluno mais alto é {num_alto} e a altura é {max(alt_aluno)}m')
