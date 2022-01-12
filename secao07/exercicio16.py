vetor = []
cont = 0
while cont < 5:
    vetor.append(int(input('Informe um número: ')))
    cont += 1
print('Escolha uma das opções abaixo')
print('1 - Mostrar na ordem direta \n2 - Mostrar de forma invertida \n0 - Encerrar programa')
opcao = int(input('Opção: '))
while opcao:
    if opcao == 1:
        print(vetor)
        opcao = int(input('Opção: '))
    elif opcao == 2:
        print(vetor[::-1])
        opcao = int(input('Opção: '))
    elif opcao == 0:
        print('Programa encerrado!')
