vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = []
for i in range(0, 10):
    v_par, v_impar = vetor1[i], vetor2[i]
    vetor3.append(v_par)
    vetor3.append(v_impar)
print(vetor3)
