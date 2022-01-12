matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
for i in matriz:
    print(i)

x = int(input('Buscar número: '))
cond = False
for linha, valor_linha in enumerate(matriz):
    for coluna, valor_coluna in enumerate(matriz[linha]):
        if matriz[linha][coluna] == x:
            cond = True
            print(f'Linha: {linha + 1}, coluna: {coluna + 1}')
if not cond:
    print(f'Número {x} não encontrado')
