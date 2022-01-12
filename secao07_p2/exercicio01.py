matriz = []
maior_10 = []
cont = 0
for l in range(0, 4):
    for c in range(0, 4):
        num = int(input(f'Informe o valor da linha {l + 1}, coluna {c + 1}: '))
        matriz.append(num)
print(f'[{matriz[0]}     {matriz[1]}     {matriz[2]}     {matriz[3]}]')
print(f'[{matriz[4]}     {matriz[5]}     {matriz[6]}     {matriz[7]}]')
print(f'[{matriz[8]}     {matriz[9]}    {matriz[10]}    {matriz[11]}]')
print(f'[{matriz[12]}    {matriz[13]}    {matriz[14]}    {matriz[15]}]')

for i in matriz:
    if i > 10:
        maior_10.append(i)
print(f'A quantidade de valores maior que 10 é: {len(maior_10)}, e esses números são: {maior_10}')
