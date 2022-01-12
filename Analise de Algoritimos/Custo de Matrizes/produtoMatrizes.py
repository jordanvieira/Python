# atividade

m1 = [[2, 3],
      [1, 0],
      [4, 5]]

m2 = [[3, 1],
      [2, 4]]


def matmult(m1, m2):
    cont = 0
    mat1 = []
    mat2 = []
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums = 0
            for k in range(len(m2)):
                sums = sums + (m1[i][k]*m2[k][j])

            mat1.append(sums)
            cont += 1
        mat2.append(mat1)
        mat1 = []
    print(mat2)
    print(f"Numero de operações {cont}")


matmult(m1, m2)
